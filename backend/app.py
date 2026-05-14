from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os
import json
import glob

app = Flask(__name__)

CORS(app)

DB_PATH = "instance/questions.db"

# CREATE DATABASE + LOAD QUESTIONS
def init_db():

    os.makedirs("instance", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS questions (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        domain TEXT,

        subtopic TEXT,

        difficulty TEXT,

        question TEXT,

        ideal_answer TEXT,

        keywords TEXT

    )

    """)

    # DELETE OLD DATA
    cursor.execute("DELETE FROM questions")

    # LOAD ALL JSON FILES
    json_files = glob.glob("questions/*.json")

    for file in json_files:

        with open(file, "r") as f:

            data = json.load(f)

            for q in data:

                cursor.execute("""

                INSERT INTO questions (

                    domain,
                    subtopic,
                    difficulty,
                    question,
                    ideal_answer,
                    keywords

                )

                VALUES (?, ?, ?, ?, ?, ?)

                """, (

                    q["domain"],
                    q["subtopic"],
                    q["difficulty"],
                    q["question"],
                    q["ideal_answer"],
                    ",".join(q["keywords"])

                ))

    conn.commit()

    conn.close()

# INITIALIZE DATABASE
init_db()

# GENERATE QUESTION
@app.route('/generate-question', methods=['POST'])
def generate_question():

    data = request.json

    domain = data['domain'].lower()

    subtopic = data['subtopic'].lower()

    difficulty = data['difficulty'].lower()

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""

    SELECT question, ideal_answer, keywords

    FROM questions

    WHERE domain=?
    AND subtopic=?
    AND difficulty=?

    ORDER BY RANDOM()

    LIMIT 1

    """, (domain, subtopic, difficulty))

    result = cursor.fetchone()

    conn.close()

    if result:

        return jsonify({

            "question": result[0],
            "ideal_answer": result[1],
            "keywords": result[2]

        })

    return jsonify({

        "question": "No questions found.",

        "ideal_answer": "",

        "keywords": ""

    })

# EVALUATE ANSWER
@app.route('/evaluate-answer', methods=['POST'])
def evaluate_answer():

    data = request.json

    user_answer = data['user_answer'].lower()

    keywords = data['keywords'].lower().split(",")

    matched = []

    missing = []

    for keyword in keywords:

        keyword = keyword.strip()

        if keyword in user_answer:

            matched.append(keyword)

        else:

            missing.append(keyword)

    total = len(keywords)

    score = round((len(matched) / total) * 10)

    return jsonify({

        "feedback": {

            "score": f"{score}/10",

            "matched_keywords": matched,

            "missing_keywords": missing,

            "suggestion": "Include missing keywords for better score."

        }

    })

# RUN SERVER
if __name__ == '__main__':

    app.run(debug=True)