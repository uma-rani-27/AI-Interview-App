import './App.css';
import { useState } from 'react';

function App() {

  const [name, setName] = useState("");

  const [loggedIn, setLoggedIn] = useState(false);

  const [domain, setDomain] = useState("");

  const [subtopic, setSubtopic] = useState("");

  const [difficulty, setDifficulty] = useState("");

  const [question, setQuestion] = useState("");

  const [, setIdealAnswer] = useState("");

  const [keywords, setKeywords] = useState("");

  const [userAnswer, setUserAnswer] = useState("");

  const [feedback, setFeedback] = useState("");

  // LOGIN
  const loginUser = () => {

    if(name !== "") {

      setLoggedIn(true);

    }

  };

  // GENERATE QUESTION
  const generateQuestion = async () => {

    const response = await fetch(
      "https://umarani.pythonanywhere.com/generate-question",
      {

        method: "POST",

        headers: {
          "Content-Type": "application/json"
        },

        body: JSON.stringify({

          domain: domain.toLowerCase(),

          subtopic: subtopic.toLowerCase(),

          difficulty: difficulty.toLowerCase()

        })

      }
    );

    const data = await response.json();

    setQuestion(data.question || "No questions found.");

    setIdealAnswer(data.ideal_answer || "");

    setKeywords(data.keywords || "");

    setFeedback("");

    setUserAnswer("");

  };

  // EVALUATE ANSWER
  const evaluateAnswer = async () => {

    const response = await fetch(
      "https://umarani.pythonanywhere.com/evaluate-answer",
      {

        method: "POST",

        headers: {
          "Content-Type": "application/json"
        },

        body: JSON.stringify({

          user_answer: userAnswer,

          keywords: keywords

        })

      }
    );

    const data = await response.json();

    setFeedback(

      `
Score: ${data.feedback.score}

Matched Keywords:
${data.feedback.matched_keywords.join(", ")}

Missing Keywords:
${data.feedback.missing_keywords.join(", ")}

Suggestion:
${data.feedback.suggestion}
`

    );

  };

  // NEXT QUESTION
  const nextQuestion = async () => {

    generateQuestion();

  };

  // LOGIN PAGE
  if(!loggedIn) {

    return (

      <div className="container">

        <div className="card">

          <h1>AI Interview Copilot</h1>

          <input
            type="text"
            placeholder="Enter your name"
            onChange={(e) =>
              setName(e.target.value)
            }
          />

          <br /><br />

          <button onClick={loginUser}>
            Continue
          </button>

        </div>

      </div>
    );

  }

  // MAIN PAGE
  return (

    <div className="container">

      <div className="card">

        <h1>Welcome, {name}</h1>

        <h2>Interview Platform</h2>

        {/* DOMAIN */}
        <select
          value={domain}
          onChange={(e) => {

            setDomain(e.target.value);

            setSubtopic("");

          }}
        >

          <option value="">
            Select Domain
          </option>

          <option value="HR">
            HR
          </option>

          <option value="Python">
            Python
          </option>

          <option value="SQL">
            SQL
          </option>

          <option value="Java">
            Java
          </option>

          <option value="Projects">
            Projects
          </option>

        </select>

        <br /><br />

        {/* SUBTOPIC */}
        <select
          value={subtopic}
          onChange={(e) =>
            setSubtopic(e.target.value)
          }
        >

          <option value="">
            Select Subtopic
          </option>

          {domain === "Python" && (
            <>
              <option value="OOPS">OOPS</option>
              <option value="Functions">Functions</option>
              <option value="Lists">Lists</option>
              <option value="Dictionary">Dictionary</option>
              <option value="Exception Handling">Exception Handling</option>
            </>
          )}

          {domain === "SQL" && (
            <>
              <option value="Joins">Joins</option>
              <option value="Normalization">Normalization</option>
              <option value="Queries">Queries</option>
              <option value="Primary Key">Primary Key</option>
            </>
          )}

          {domain === "Java" && (
            <>
              <option value="OOPS">OOPS</option>
              <option value="Collections">Collections</option>
              <option value="Exception Handling">Exception Handling</option>
              <option value="Multithreading">Multithreading</option>
            </>
          )}

          {domain === "HR" && (
            <>
              <option value="Self Introduction">Self Introduction</option>
              <option value="Strengths">Strengths</option>
              <option value="Weakness">Weakness</option>
            </>
          )}

          {domain === "Projects" && (
            <>
              <option value="Projects">Projects</option>
              <option value="Mini Projects">Mini Projects</option>
              <option value="Final Year Projects">Final Year Projects</option>
            </>
          )}

        </select>

        <br /><br />

        {/* DIFFICULTY */}
        <select
          value={difficulty}
          onChange={(e) =>
            setDifficulty(e.target.value)
          }
        >

          <option value="">
            Select Difficulty
          </option>

          <option value="Easy">
            Easy
          </option>

          <option value="Medium">
            Medium
          </option>

          <option value="Hard">
            Hard
          </option>

        </select>

        <br /><br />

        {/* GENERATE QUESTION */}
        <button onClick={generateQuestion}>
          Generate Question
        </button>

        <br /><br />

        {/* QUESTION */}
        <h2>{question}</h2>

        {/* ANSWER BOX */}
        <textarea
          rows="6"
          placeholder="Type your answer..."
          value={userAnswer}
          onChange={(e) =>
            setUserAnswer(e.target.value)
          }
        ></textarea>

        <br />

        {/* SUBMIT ANSWER */}
        <button onClick={evaluateAnswer}>
          Submit Answer
        </button>

        <br /><br />

        {/* FEEDBACK */}
        <pre className="feedback-box">

          {feedback}

        </pre>

        {/* NEXT QUESTION */}
        {feedback && (

          <button onClick={nextQuestion}>

            Next Question

          </button>

        )}

      </div>

    </div>
  );

}

export default App;