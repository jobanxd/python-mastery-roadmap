# 🐍 Python Mastery Roadmap – Daily Challenges (90 Days)

A collection of one problem per day following my 90-day Python learning journey. Each challenge is designed to take around 10–30 minutes.

---

## 🔰 Phase 1: Python Foundations (Days 1–20)

### Week 1: Basics

- **Day 1:** Write a script that prints your name, age, and favorite programming language using variables.
- **Day 2:** Create a function that takes user input and tells the data type of each input (use `type()` and casting).
- **Day 3:** Make a calculator that performs +, -, *, /, //, %, ** on two user inputs.
- **Day 4:** Build a simple age checker – if age < 13: kid, <18: teen, <60: adult, else: senior.
- **Day 5:** Print the first 10 multiples of 3 using both `for` and `while` loops.
- **Day 6:** Create a function to check if a number is prime. Use arguments and return values.
- **Day 7:** Build a mini app that takes a number and prints "Fizz", "Buzz", or "FizzBuzz".

### Week 2: Data Structures

- **Day 8:** Create a list of 5 items and perform slicing, append, remove, and sort.
- **Day 9:** Write a program that uses a dictionary to store and lookup contact details.
- **Day 10:** Create a dictionary from a list of numbers (1–5) where the value is the square using comprehension.
- **Day 11:** Take a sentence and output the number of vowels using string manipulation.
- **Day 12:** Handle a division-by-zero error using `try/except/finally`.
- **Day 13:** Read a file and count the number of lines. If the file doesn't exist, handle the error.
- **Day 14:** Build a word frequency counter from a text file.

---

## 🧰 Phase 2: Intermediate Python (Days 21–40)

### Week 3: Object-Oriented Programming (OOP)

- **Day 15:** Create a `Car` class with `make`, `model`, and `year` attributes.
- **Day 16:** Extend the `Car` class to include methods like `start()` and `stop()`.
- **Day 17:** Create a `Vehicle` base class and `Car` and `Bike` subclasses. Demonstrate inheritance.
- **Day 18:** Use name mangling to make an attribute private, and create getter/setter methods.
- **Day 19:** Add a `__str__()` method to your `Car` class that returns a readable description.
- **Day 20:** Build a basic banking system with account creation and balance updates.

### Week 4: Modules & Advanced Features

- **Day 21:** Use `datetime` and `os` modules to create a script that lists all `.txt` files modified today.
- **Day 22:** Use `map()` to square a list of numbers, `filter()` to get even numbers.
- **Day 23:** Create a generator that yields Fibonacci numbers up to n.
- **Day 24:** Write a decorator that logs the execution time of a function.
- **Day 25:** Use a context manager (`with`) to read and write to a file.
- **Day 26:** Create a virtual environment, install `requests`, and show how to list installed packages.
- **Day 27:** Write a unit test for a simple function using `unittest`.
- **Day 28:** Build a CLI-based to-do app that saves tasks to a file.

---

## 🧱 Phase 3: Popular Libraries (Days 41–60)

### Week 5: Data Science

- **Day 29:** Create a NumPy array and compute its mean, max, and reshape it.
- **Day 30:** Use broadcasting to subtract a vector from each row of a matrix.
- **Day 31:** Load a CSV file with Pandas and display basic info (head, describe).
- **Day 32:** Filter rows based on a condition and group by a column in a Pandas DataFrame.
- **Day 33:** Create a line chart and bar plot using Matplotlib and Seaborn.
- **Day 34:** Analyze a dataset (Iris/Titanic) and show summary stats.
- **Day 35:** Perform EDA on a sample dataset – nulls, uniques, correlation.

### Week 6: Web Scraping & APIs

- **Day 36:** Scrape titles and links from a blog using `requests` + `BeautifulSoup`.
- **Day 37:** Use `selenium` to auto-fill and submit a form on a test site.
- **Day 38:** Fetch and display current weather using a public API (e.g., OpenWeatherMap).
- **Day 39:** Create a simple Flask app with one route returning JSON data.
- **Day 40:** Build a Reddit scraper that gets top posts from a subreddit.

---

## 🌐 Phase 4: Web Development (Days 61–75)

### Week 7: Flask & Django

- **Day 41:** Build a Flask app that displays a welcome message on the homepage.
- **Day 42:** Add a contact form to your Flask app and process the data.
- **Day 43:** Set up a new Django project and add a model called `Article`.
- **Day 44:** Create a Django view to display all `Article` objects in a template.
- **Day 45:** Implement full CRUD for `Article` in Django.

### Week 8: REST APIs & FastAPI

- **Day 46:** Design a simple JSON-based REST API structure for a book collection.
- **Day 47:** Build a Flask REST API to list, add, and delete books.
- **Day 48:** Create a FastAPI endpoint that returns a list of users.
- **Day 49:** Use Pydantic to validate FastAPI input data for a user signup form.
- **Day 50:** Build a simple Blog API with FastAPI or Django REST Framework.

### Week 9: Database

- **Day 51:** Write SQL queries: Create table, insert data, basic SELECT with WHERE.
- **Day 52:** Use SQLAlchemy to define a model and insert/query records.
- **Day 53:** Use Django ORM to filter records from a model based on conditions.
- **Day 54:** Create a CLI Inventory Manager that connects to SQLite and performs CRUD.

---

## 🧠 Phase 5: Advanced Python & Specialization (Days 76–90)

### Week 10: Special Topics

- **Day 55:** Write a program that uses `threading` to run 3 tasks in parallel.
- **Day 56:** Create an async function that fetches 3 URLs concurrently using `asyncio`.
- **Day 57:** Set up a FastAPI WebSocket to echo messages from the client.
- **Day 58:** Write a `Dockerfile` for a simple Python web app.
- **Day 59:** Set up a basic GitHub Actions workflow to run tests on push.

### Week 11: AI/ML Intro

- **Day 60:** Use Scikit-learn to train a classifier on the Iris dataset.
- **Day 61:** Load a dataset and separate it into training and test sets. Explain the split.
- **Day 62:** Create a simple TensorFlow model to predict housing prices.
- **Day 63:** Build a Keras neural network to classify digits from MNIST.
- **Day 64:** Use HuggingFace Transformers to run a sentiment analysis on a sentence.

### Week 12: Capstone Projects

- **Days 65–90:** Choose 2–3 of the following and build them over the final weeks:
  - 🌐 Web App with Django or Flask
  - 🔌 REST API with FastAPI
  - 📊 Data Dashboard with Streamlit
  - 🧠 AI App with TensorFlow or PyTorch
  - 🤖 Automation Bot using Selenium + Schedule

---

> 💡 Tip: Use Git commits to track daily progress and document solutions in a `/solutions` folder.
