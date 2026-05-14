import json
import os

os.makedirs("questions", exist_ok=True)

# QUESTIONS
question_templates = {

    # =========================
    # HR SELF INTRODUCTION
    # =========================

    "hr_self introduction_easy": {
        "questions": [
            "Tell me about yourself.",
            "Introduce yourself briefly.",
            "Can you give a short self introduction?",
            "Describe your educational background.",
            "Tell me about your strengths and interests."
        ],
        "keywords": [
            "education",
            "skills",
            "career goals",
            "strengths",
            "background"
        ]
    },

    # =========================
    # HR STRENGTHS
    # =========================

    "hr_strengths_easy": {
        "questions": [
            "What are your strengths?",
            "Describe your main strengths.",
            "How do your strengths help you?",
            "What strength are you most confident about?",
            "How does teamwork help you succeed?"
        ],
        "keywords": [
            "communication",
            "teamwork",
            "confidence",
            "motivation",
            "problem solving"
        ]
    },

    # =========================
    # HR WEAKNESS
    # =========================

    "hr_weakness_easy": {
        "questions": [
            "What is your weakness?",
            "Describe one weakness you are improving.",
            "How do you handle your weaknesses?",
            "What personal weakness do you want to overcome?",
            "How are you improving your weak areas?"
        ],
        "keywords": [
            "improvement",
            "learning",
            "adaptability",
            "communication",
            "confidence"
        ]
    },

    # =========================
    # PYTHON OOPS
    # =========================

    "python_oops_easy": {
        "questions": [
            "What is a class in Python?",
            "What is an object in Python?",
            "Explain inheritance.",
            "What is polymorphism?",
            "What is encapsulation?"
        ],
        "keywords": [
            "class",
            "object",
            "inheritance",
            "polymorphism",
            "encapsulation"
        ]
    },

    "python_oops_medium": {
        "questions": [
            "Explain inheritance with example.",
            "How does polymorphism improve flexibility?",
            "Explain abstraction with real-time example.",
            "What is encapsulation and why is it important?",
            "Difference between method overloading and overriding."
        ],
        "keywords": [
            "inheritance",
            "polymorphism",
            "encapsulation",
            "abstraction",
            "constructor"
        ]
    },

    "python_oops_hard": {
        "questions": [
            "Explain polymorphism in Python.",
            "What is abstraction in Python OOPS?",
            "Explain inheritance with real-time example.",
            "What is encapsulation in Python?",
            "Differentiate method overloading and overriding."
        ],
        "keywords": [
            "inheritance",
            "polymorphism",
            "encapsulation",
            "abstraction",
            "constructor"
        ]
    },

    # =========================
    # PYTHON FUNCTIONS
    # =========================

    "python_functions_easy": {
        "questions": [
            "What is a function in Python?",
            "Why are functions used?",
            "What is a parameter?",
            "What is an argument?",
            "Explain return statement."
        ],
        "keywords": [
            "functions",
            "parameters",
            "arguments",
            "return",
            "lambda"
        ]
    },

    "python_functions_medium": {
        "questions": [
            "Explain recursion with example.",
            "Difference between lambda and normal functions.",
            "How do default arguments work?",
            "Explain variable scope in Python.",
            "What are anonymous functions?"
        ],
        "keywords": [
            "recursion",
            "lambda",
            "scope",
            "anonymous",
            "modularity"
        ]
    },

    "python_functions_hard": {
        "questions": [
            "Explain advanced recursion in Python.",
            "How do higher-order functions work internally?",
            "Explain closures in Python.",
            "Difference between generators and normal functions.",
            "How does memory management work in functions?"
        ],
        "keywords": [
            "closures",
            "higher order",
            "generators",
            "memory",
            "advanced functions"
        ]
    },

    # =========================
    # PYTHON LISTS
    # =========================

    "python_lists_easy": {
        "questions": [
            "What is a list in Python?",
            "How do you create a list?",
            "Explain append() method.",
            "Explain insert() method.",
            "Difference between remove() and pop()."
        ],
        "keywords": [
            "list",
            "append",
            "insert",
            "remove",
            "pop"
        ]
    },

    "python_lists_medium": {
        "questions": [
            "Explain list comprehension.",
            "How do you copy a list?",
            "Difference between shallow copy and deep copy.",
            "Explain nested lists with examples.",
            "How do you iterate through lists?"
        ],
        "keywords": [
            "list comprehension",
            "copy",
            "deep copy",
            "nested list",
            "iteration"
        ]
    },

    "python_lists_hard": {
        "questions": [
            "Explain advanced list comprehension.",
            "How do lists work internally in Python?",
            "Explain memory allocation in lists.",
            "Difference between arrays and lists.",
            "How do you optimize list operations?"
        ],
        "keywords": [
            "memory allocation",
            "dynamic resizing",
            "optimization",
            "arrays",
            "performance"
        ]
    },

    # =========================
    # PYTHON DICTIONARY
    # =========================

    "python_dictionary_easy": {
        "questions": [
            "What is a dictionary in Python?",
            "How do you create a dictionary?",
            "What are keys and values?",
            "Explain get() method.",
            "What is nested dictionary?"
        ],
        "keywords": [
            "dictionary",
            "keys",
            "values",
            "get",
            "nested dictionary"
        ]
    },

    "python_dictionary_medium": {
        "questions": [
            "Explain dictionary comprehension.",
            "How does hashing work in dictionaries?",
            "Difference between dictionary and set.",
            "Explain nested dictionaries.",
            "How do you merge dictionaries?"
        ],
        "keywords": [
            "dictionary comprehension",
            "hashing",
            "nested dictionary",
            "merge",
            "optimization"
        ]
    },

    "python_dictionary_hard": {
        "questions": [
            "Explain internal working of dictionaries.",
            "How does hashing optimize dictionaries?",
            "Explain collision handling in dictionaries.",
            "How do dictionaries manage memory?",
            "Explain advanced dictionary comprehension."
        ],
        "keywords": [
            "hashing",
            "collision",
            "memory",
            "optimization",
            "internal working"
        ]
    },

    # =========================
    # PYTHON EXCEPTION HANDLING
    # =========================

    "python_exception handling_easy": {
        "questions": [
            "What is exception handling in Python?",
            "Why is exception handling important?",
            "Explain try block.",
            "Explain except block.",
            "What is finally block?"
        ],
        "keywords": [
            "exception",
            "try",
            "except",
            "finally",
            "raise"
        ]
    },

    "python_exception handling_medium": {
        "questions": [
            "Explain custom exceptions.",
            "How do nested try blocks work?",
            "Explain multiple except blocks.",
            "How does finally block improve reliability?",
            "Explain exception propagation."
        ],
        "keywords": [
            "custom exceptions",
            "nested try",
            "multiple except",
            "finally",
            "propagation"
        ]
    },

    "python_exception handling_hard": {
        "questions": [
            "Explain advanced exception handling in Python.",
            "How does exception propagation work internally?",
            "Explain custom exception classes.",
            "How do large systems manage exceptions?",
            "Explain exception chaining professionally."
        ],
        "keywords": [
            "advanced exception handling",
            "propagation",
            "custom exceptions",
            "logging",
            "debugging"
        ]
    },

    # =========================
    # JAVA OOPS
    # =========================

    "java_oops_easy": {
        "questions": [
            "What is OOPS in Java?",
            "What is a class in Java?",
            "What is an object in Java?",
            "Explain inheritance in Java.",
            "What is polymorphism?"
        ],
        "keywords": [
            "class",
            "object",
            "inheritance",
            "polymorphism",
            "encapsulation"
        ]
    },

    "java_oops_medium": {
        "questions": [
            "Explain abstraction with example.",
            "Difference between method overloading and overriding.",
            "How does inheritance improve reusability?",
            "Explain constructor types in Java.",
            "What is dynamic polymorphism?"
        ],
        "keywords": [
            "abstraction",
            "overloading",
            "overriding",
            "constructors",
            "dynamic polymorphism"
        ]
    },

    "java_oops_hard": {
        "questions": [
            "Explain runtime polymorphism internally.",
            "How does JVM manage objects?",
            "Difference between abstract class and interface.",
            "Explain multiple inheritance using interfaces.",
            "How does encapsulation improve security?"
        ],
        "keywords": [
            "runtime polymorphism",
            "jvm",
            "interface",
            "abstract class",
            "security"
        ]
    },

    # =========================
    # JAVA COLLECTIONS
    # =========================

    "java_collections_easy": {
        "questions": [
            "What is Collection Framework in Java?",
            "Difference between List and Set.",
            "What is ArrayList?",
            "What is HashSet?",
            "What is HashMap?"
        ],
        "keywords": [
            "collection",
            "arraylist",
            "hashset",
            "hashmap",
            "list"
        ]
    },

    "java_collections_medium": {
        "questions": [
            "Difference between ArrayList and LinkedList.",
            "How does HashMap work?",
            "Explain Iterator in Java.",
            "Difference between Set and Map.",
            "Explain TreeSet."
        ],
        "keywords": [
            "arraylist",
            "linkedlist",
            "hashmap",
            "iterator",
            "treeset"
        ]
    },

    "java_collections_hard": {
        "questions": [
            "Explain internal working of HashMap.",
            "How does hashing improve performance?",
            "Difference between fail-fast and fail-safe iterators.",
            "How are collections synchronized?",
            "Explain ConcurrentHashMap."
        ],
        "keywords": [
            "hashmap",
            "hashing",
            "fail fast",
            "synchronization",
            "concurrenthashmap"
        ]
    },

    # =========================
    # JAVA EXCEPTION HANDLING
    # =========================

    "java_exception handling_easy": {
        "questions": [
            "What is exception handling in Java?",
            "Explain try and catch blocks.",
            "What is finally block?",
            "Difference between checked and unchecked exceptions.",
            "What is throw keyword?"
        ],
        "keywords": [
            "exception",
            "try",
            "catch",
            "finally",
            "throw"
        ]
    },

    "java_exception handling_medium": {
        "questions": [
            "Explain custom exceptions in Java.",
            "Difference between throw and throws.",
            "How does exception propagation work?",
            "Explain nested try blocks.",
            "How does finally improve reliability?"
        ],
        "keywords": [
            "custom exception",
            "throw",
            "throws",
            "propagation",
            "nested try"
        ]
    },

    "java_exception handling_hard": {
        "questions": [
            "Explain JVM exception handling internally.",
            "How do enterprise applications manage exceptions?",
            "Explain exception chaining.",
            "How does exception handling affect performance?",
            "Explain best practices for exception handling."
        ],
        "keywords": [
            "jvm",
            "exception chaining",
            "enterprise",
            "performance",
            "best practices"
        ]
    },

    # =========================
    # JAVA MULTITHREADING
    # =========================

    "java_multithreading_easy": {
        "questions": [
            "What is multithreading in Java?",
            "What is a thread?",
            "How do you create a thread in Java?",
            "Difference between process and thread.",
            "What is thread lifecycle?"
        ],
        "keywords": [
            "multithreading",
            "thread",
            "process",
            "lifecycle",
            "java"
        ]
    },

    "java_multithreading_medium": {
        "questions": [
            "Difference between Runnable and Thread class.",
            "Explain thread synchronization.",
            "What is deadlock?",
            "Explain inter-thread communication.",
            "What is thread scheduling?"
        ],
        "keywords": [
            "runnable",
            "synchronization",
            "deadlock",
            "communication",
            "scheduling"
        ]
    },

    "java_multithreading_hard": {
        "questions": [
            "How does JVM manage threads internally?",
            "Explain thread pool architecture.",
            "Difference between synchronized block and synchronized method.",
            "Explain concurrency in Java.",
            "How do enterprise systems optimize multithreading?"
        ],
        "keywords": [
            "jvm",
            "thread pool",
            "synchronized",
            "concurrency",
            "optimization"
        ]
    },

    # =========================
    # SQL JOINS
    # =========================

    "sql_joins_easy":
{
        "questions": [
            "What is JOIN in SQL?",
            "Why are joins used?",
            "Explain INNER JOIN.",
            "Explain LEFT JOIN.",
            "Explain RIGHT JOIN."
        ],
        "keywords": [
            "join",
            "inner join",
            "left join",
            "right join",
            "database"
        ]
    },

    "sql_joins_medium": {
        "questions": [
            "Explain different types of joins with examples.",
            "How does INNER JOIN work internally?",
            "Difference between LEFT JOIN and RIGHT JOIN.",
            "Explain SELF JOIN with real-time example.",
            "How does FULL OUTER JOIN work?"
        ],
        "keywords": [
            "inner join",
            "outer join",
            "self join",
            "cross join",
            "optimization"
        ]
    },

    "sql_joins_hard": {
        "questions": [
            "Explain join optimization techniques.",
            "How do SQL engines process joins internally?",
            "Difference between hash join and nested loop join.",
            "Explain join execution plans.",
            "How do joins affect database performance?"
        ],
        "keywords": [
            "optimization",
            "hash join",
            "nested loop join",
            "execution",
            "performance"
        ]
    },

    # =========================
    # SQL NORMALIZATION
    # =========================

    "sql_normalization_easy": {
        "questions": [
            "What is normalization?",
            "Why is normalization important?",
            "Explain 1NF.",
            "Explain 2NF.",
            "Explain 3NF."
        ],
        "keywords": [
            "normalization",
            "1NF",
            "2NF",
            "3NF",
            "redundancy"
        ]
    },

    "sql_normalization_medium": {
        "questions": [
            "Explain normalization with examples.",
            "Difference between 2NF and 3NF.",
            "Explain Boyce-Codd Normal Form.",
            "How does normalization remove anomalies?",
            "Explain transitive dependency."
        ],
        "keywords": [
            "BCNF",
            "dependency",
            "anomalies",
            "database design",
            "normalization"
        ]
    },

    "sql_normalization_hard": {
        "questions": [
            "Explain advanced normalization techniques.",
            "Difference between BCNF and 4NF.",
            "Explain multivalued dependency.",
            "How does normalization impact performance?",
            "Explain normalization trade-offs."
        ],
        "keywords": [
            "advanced normalization",
            "BCNF",
            "4NF",
            "performance",
            "dependency"
        ]
    },

    # =========================
    # SQL QUERIES
    # =========================

    "sql_queries_easy": {
        "questions": [
            "What is SQL query?",
            "Explain SELECT statement.",
            "What is WHERE clause?",
            "Explain ORDER BY.",
            "What is GROUP BY?"
        ],
        "keywords": [
            "select",
            "where",
            "group by",
            "order by",
            "query"
        ]
    },

    "sql_queries_medium": {
        "questions": [
            "Explain subqueries in SQL.",
            "Difference between correlated and non-correlated subqueries.",
            "How do aggregate functions work?",
            "Explain nested queries.",
            "What is query optimization?"
        ],
        "keywords": [
            "subquery",
            "aggregate",
            "optimization",
            "nested queries",
            "sql"
        ]
    },

    "sql_queries_hard": {
        "questions": [
            "Explain SQL query optimization techniques.",
            "How does indexing improve query performance?",
            "Explain query execution plans.",
            "Difference between clustered and non-clustered indexes.",
            "Explain partitioning in databases."
        ],
        "keywords": [
            "query optimization",
            "indexing",
            "execution plan",
            "partitioning",
            "performance"
        ]
    },

    # =========================
    # SQL PRIMARY KEY
    # =========================

    "sql_primary key_easy": {
        "questions": [
            "What is a primary key?",
            "Why is primary key important?",
            "Can a table have multiple primary keys?",
            "Difference between primary key and unique key.",
            "Can primary key contain NULL values?"
        ],
        "keywords": [
            "primary key",
            "unique key",
            "null",
            "constraints",
            "database"
        ]
    },

    "sql_primary key_medium": {
        "questions": [
            "Explain composite primary keys with examples.",
            "How do foreign keys maintain relationships?",
            "Difference between primary key and indexing.",
            "Explain referential integrity.",
            "How are keys used in normalization?"
        ],
        "keywords": [
            "foreign key",
            "referential integrity",
            "normalization",
            "indexing",
            "relationships"
        ]
    },

    "sql_primary key_hard": {
        "questions": [
            "Explain advanced key management in databases.",
            "Difference between UUID and AUTO_INCREMENT keys.",
            "Explain indexing strategies for primary keys.",
            "How do distributed systems maintain key integrity?",
            "Explain clustered indexing with primary keys."
        ],
        "keywords": [
            "uuid",
            "auto increment",
            "indexing",
            "distributed systems",
            "clustered indexing"
        ]
    }
        ,

    # =========================
    # PROJECTS
    # =========================

    "projects_easy": {
        "questions": [
            "Explain your project briefly.",
            "What was your role in the project?",
            "What technologies were used in your project?",
            "What problem does your project solve?",
            "Why did you choose this project?"
        ],
        "keywords": [
            "project",
            "role",
            "technology",
            "problem solving",
            "implementation"
        ]
    },

    "projects_medium": {
        "questions": [
            "Explain your project architecture.",
            "What challenges did you face in the project?",
            "How did you overcome project difficulties?",
            "Explain the workflow of your project.",
            "How does your project work technically?"
        ],
        "keywords": [
            "architecture",
            "workflow",
            "technical",
            "challenges",
            "implementation"
        ]
    },

    "projects_hard": {
        "questions": [
            "Explain your project in detail technically.",
            "How can your project be improved further?",
            "What are the scalability challenges in your project?",
            "How does your project handle performance optimization?",
            "Explain the real-time impact of your project."
        ],
        "keywords": [
            "scalability",
            "optimization",
            "performance",
            "real time",
            "technical architecture"
        ]
    },

    # =========================
    # MINI PROJECTS
    # =========================

    "mini projects_easy": {
        "questions": [
            "Explain your mini project.",
            "What was the objective of the mini project?",
            "Which tools were used in the mini project?",
            "What did you learn from the mini project?",
            "What challenges did you face?"
        ],
        "keywords": [
            "mini project",
            "objective",
            "tools",
            "learning",
            "implementation"
        ]
    },

    "mini projects_medium": {
        "questions": [
            "Explain the workflow of your mini project.",
            "How did you divide tasks in the project?",
            "What technologies were integrated?",
            "How was testing performed in your project?",
            "Explain project execution step by step."
        ],
        "keywords": [
            "workflow",
            "testing",
            "execution",
            "integration",
            "project management"
        ]
    },

    "mini projects_hard": {
        "questions": [
            "Explain the technical architecture of your mini project.",
            "How would you improve the project scalability?",
            "Explain optimization techniques used in your project.",
            "How does your project handle errors?",
            "What advanced features can be added?"
        ],
        "keywords": [
            "architecture",
            "optimization",
            "error handling",
            "advanced features",
            "scalability"
        ]
    },

    # =========================
    # FINAL YEAR PROJECTS
    # =========================

    "final year projects_easy": {
        "questions": [
            "Explain your final year project.",
            "What inspired your final year project?",
            "What technologies were used?",
            "What was your contribution in the project?",
            "What are the benefits of your project?"
        ],
        "keywords": [
            "final year project",
            "technologies",
            "contribution",
            "benefits",
            "implementation"
        ]
    },

    "final year projects_medium": {
        "questions": [
            "Explain the modules in your final year project.",
            "What challenges did you face during development?",
            "How was your project tested?",
            "Explain project implementation in detail.",
            "How does your project solve real-world problems?"
        ],
        "keywords": [
            "modules",
            "testing",
            "development",
            "real world",
            "implementation"
        ]
    },

    "final year projects_hard": {
        "questions": [
            "Explain the complete architecture of your final year project.",
            "How can your project be deployed in real-time?",
            "What optimization techniques were used?",
            "How does your project ensure scalability?",
            "Explain future enhancements of your project."
        ],
        "keywords": [
            "architecture",
            "deployment",
            "optimization",
            "scalability",
            "future enhancements"
        ]
    }

}

# GENERATE FILES
for filename, content in question_templates.items():

    parts = filename.split("_")

    domain = parts[0]

    subtopic = " ".join(parts[1:-1])

    difficulty = parts[-1]

    questions = []

    for q in content["questions"]:

        question = {

            "domain": domain,
            "subtopic": subtopic,
            "difficulty": difficulty,
            "question": q,
            "ideal_answer": "Provide professional detailed explanation.",
            "keywords": content["keywords"]

        }

        questions.append(question)

    with open(f"questions/{filename}.json", "w") as f:

        json.dump(questions, f, indent=2)

    print(f"{filename}.json generated successfully.")