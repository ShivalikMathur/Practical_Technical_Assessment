# Practical_Technical_Assessment
Here is the code I have written to solve the Practical Technical
Assessment problems.

The practical technical assessment involves solving problems on Python,
FastAPI, React, data processing, debugging and machine learning.

Technical Assessment Project Structure

technical-assessment/
│
├── README.md
├── .gitignore
│
├── theory/
│   └── answers.md
│
├── q1_transaction_api/
│   └── main.py
│
├── q2_duplicates/
│   └── solution.py
│
├── q3_data_processing/
│   ├── process.py
│   └── users.json
│
├── q4_react_search/
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   ├── server.cjs
│   └── src/
│       └── App.jsx
│
├── q5_react_bug_fix/
│   ├── package.json
│   ├── package-lock.json
│   └── src/
│       └── App.jsx
│
└── q6_ml_classification/
    ├── train.py
    └── churn.csv

Section 1 - Theory

The theory section consists of the answers for the following questions:

What is RAG and when would you use it?

What is the difference between AI, Machine Learning and Generative AI?

What is a prompt in AI?

Section 2 – Practical Questions

Q1 – Transaction Processing API

Description

In this question, I implement a basic transaction-processing API using
FastAPI.

The functionality provided includes:

Adding transactions

Getting transactions for a user

Getting a transaction summary

Amount validation

Type validation

Timestamp validation

Types of transactions include:

credit

debit

Endpoints

POST /transactions
GET /transactions/{user_id}
GET /transactions/{user_id}/summary

Requirements

A transaction is of the form:

{
    "user_id": "U1001",
    "amount": 1500,
    "type": "credit",
    "timestamp": "2026-09-18T10:30:00"
}

The transaction summary takes this form:

{
    "total_credit": 5000,
    "total_debit": 2500,
    "balance": 2500
}

To run

Open a terminal window inside the Q1 directory:

cd q1_transaction_api

Install the required dependencies:

pip install fastapi uvicorn

Start the API:

uvicorn main:app --reload

Access the API documentation:

http://127.0.0.1:8000/docs

Design Choice

An in-memory Python list was used to store the transactions as the
assessment did not mandate the use of any databases.

Also, Python's native datetime module was used to validate the
transaction timestamp.

Assumptions

The transactions should persist as long as the application is running.

The user ids will be considered as strings.

Transaction amounts must be positive numbers.

Types are limited to credit and debit.

Q2 - Duplicate Detection

Problem Description

In this problem, the task is to correct the function implemented in Python
that determines duplicates within a list.

For example:

[1, 2, 3, 2, 4, 1, 5, 2]

The expected output:

[1, 2]

The initial implementation may add the same duplicate several times since
it checked each occurrence of the element.

Execution Instructions

cd q2_duplicates
python solution.py

Design Decision

The solution maintains the record of the previously seen values and ensures
that a duplicate is added only once.

Q3 - Python Data Processing

Problem Description

This problem involves processing of the provided JSON file which stores user data.

The program:

Opens the provided JSON file.

Removes duplicate user ids.

Removes users who have a score lower than 50.

Determines the average score.

Determines the maximum score.

Determines the minimum score.

Determines the top 10 users sorted by their score.

Input

The input file is:

q3_data_processing/users.json

Output

The output result will contain:

{
    "average_score": 0,
    "maximum_score": 0,
    "minimum_score": 0,
    "top_10_users": []
}

Of course, the actual values depend on the content of users.json.

Execution Instructions

cd q3_data_processing
python process.py

Design Choice

The built-in json module in Python is employed to read the data from the file.

A dictionary is used to tackle duplicate user_ids, while the rest of the records
are handled using regular Python lists.

Assumptions

In case a duplicate user_id is found, only one record will be kept.

Users who have a score less than 50 are removed before computing statistics.

Q4 - React Search and Debouncing

Description

This problem statement creates a React search component.

It uses:

GET /api/users?search=<query>

It has:

Search input

Debouncing

Loading state

Error state

No results message

Search results

Handling of stale requests

Why Debouncing is Used

Without debouncing, the search:

Rahul

may make requests:

R
Ra
Rah
Rahu
Rahul

There will be a different request made for each keystroke.

As a result, the search waits for some time after the user stopped
typing before making the request.

How to run

One terminal window:

cd q4_react_search
npm install
npm run dev

Another terminal window:

node server.cjs

Open the Vite link, usually:

http://localhost:5173

Design Decisions

There is a short debounce time used to avoid extra API calls.

Additionally, there is an AbortController that allows cancelling the
older search in case of a new search.

Assumptions

The API is running on the local machine.

The front end communicates with the API via /api route.

The example users' information is stored on the local server.

Q5 - React Bug Fixing

Description

For this question, we have been provided with a React component with several bugs.

The component enables selection of the users from the list with a Clear button.

Bugs Fixed Include:

Import statements missing for React hooks

Missing dependency array in useEffect

Missing key in the render function

Clickable div instead of using a button

Selection of a user is not shown

How to Run

cd q5_react_bug_fix
npm install
npm run dev

Navigate to the URL generated by Vite, typically:

http://localhost:5173

Design Decision

A simple component is used in this question since the aim here is to spot and fix the bugs in React and not create an application.

The useEffect dependency array includes selectedUser to ensure that the effect gets triggered whenever there is a change in the selected user and not after each render.

Additionally, a unique key is provided while rendering users.

Q6 - Machine Learning Classification

Description

In this assignment, I created a classification model to predict whether a customer will churn.

The following features can be considered:

Age
income
number_of_logins
purchase_count
last_login_days
subscription

The target variable is:

will_churn

Pipeline

Data loading →
Data cleaning →
Train/test split →
Feature processing →
Model training →
Model evaluation

Model

The classification algorithm used here is Logistic Regression.

I chose to use Logistic Regression because I am working with a
binary classification problem that needs an easy to understand,
fast and interpretable baseline model.

The model is evaluated based on the following metrics:

Accuracy

Precision

Recall

The values are obtained by running the training code on the
dataset.

How to run

cd q6_ml_classification

Install the necessary libraries:

pip install pandas scikit-learn

Run the training script:

python train.py

Overfitting

Overfitting is when a model becomes overly fit for the training
data and performs poorly on new data.

For instance, the training accuracy of the model might be high,
but its testing accuracy is low.

Improvement possibilities

There are several possibilities for improving the code like:

Adding more training data

Using various classification algorithms

Feature selection

Hyperparameter tuning

Cross validation

Class imbalance handling

Creation
What is the latest OpenAI AI model?

What is the difference between AI and
