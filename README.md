# SimpleNotes
Video Demo: (https://www.youtube.com/watch?v=7OwIYNpOutc)>


Introduction
Simple Notes is a lightweight, web-based note-taking application that I developed as my Final Project for CS50x, Harvard University’s Introduction to Computer Science. The main goal of this project was to create something small, easy to understand, and functional that demonstrates the three core layers of full-stack web development: the frontend, the backend, and the database.

This project combines Python (using the Flask framework), SQLite for data storage, and JavaScript for client-side interaction. It allows users to create, view, and delete short notes instantly from their browser without refreshing the page. Everything is saved locally in an SQLite database, so notes persist even when the server is restarted.

When I began this project, I wanted something simple but not trivial. I wanted it to feel like a real application that someone could actually use every day, while keeping it small enough to finish and understand fully within the timeframe of the course. I also wanted to make sure it reflected the fundamental skills that CS50 taught: problem solving, logical thinking, code organization, and clear documentation.

Inspiration and Motivation
I live in a developing country, and one of the things that inspired me to take CS50 was the idea that world-class education is now accessible online. Having access to Harvard-level teaching from anywhere in the world is truly lucky, especially for students who may not have formal computer science programs available locally.

The motivation behind Simple Notes came from a personal habit — I often open a text file or phone app just to jot down small reminders or ideas. Most of those tools are either too bloated or require sign-ins, syncing, and features I don’t need. I wanted something extremely minimal: just type, save, and delete. No account, no clutter, no waiting. That’s how Simple Notes was born — a project that reflects both simplicity and the power of connecting backend and frontend through code.

Overview of the Application
When you start the Flask server by running python app.py, it launches a local web server that serves both the HTML page and a set of JSON API routes. The main interface is a single page that displays an input field, an “Add” button, and a list of saved notes.

When a user types a message and clicks Add, the text is sent to the Flask server using a JavaScript fetch() POST request.
The server receives that text, inserts it into the SQLite database, and returns the newly created note in JSON format.
The frontend JavaScript then updates the note list immediately without reloading the page.
When the user clicks the × button, a DELETE request is sent to the backend, which removes that note from the database and updates the display.
Every note includes an automatically generated timestamp (using CURRENT_TIMESTAMP in SQLite). The interface is simple, responsive, and runs smoothly even with dozens of notes.

Technologies Used
1. Python and Flask
Flask is the lightweight web framework used for the backend. It’s responsible for handling routes, database operations, and serving both static files and templates. Flask was perfect for this project because it is simple, minimal, and yet powerful enough to handle API endpoints.

I learned how Flask uses Jinja templates to render HTML and how routes can return either HTML pages or JSON data. Flask’s flexibility made it easy to build the project in small steps, testing one route at a time.

2. SQLite
SQLite was used as the database because it’s file-based, fast, and doesn’t require setting up a separate server. The database is stored in a single file called notes.db, created automatically by running python app.py --initdb. The database contains one table named notes with three fields:

id — an integer primary key that auto-increments
text — the note’s content
created_at — a timestamp indicating when the note was created
3. JavaScript
The JavaScript file (static/main.js) handles all the asynchronous actions on the client side. It communicates with the backend through the Fetch API and dynamically updates the DOM without needing a full page reload. This approach demonstrates the concept of AJAX and how modern web applications operate interactively.

4. HTML and CSS
The visual part of the app is built using standard HTML and styled with CSS. I used a dark theme with soft contrast, rounded corners, and simple layouts. The goal was to keep it visually pleasant but not distracting.

Project Structure
app.py
This file contains the main logic of the web application. It defines:

The Flask app configuration.
Database connection helpers.
API routes for creating, listing, and deleting notes.
A command line argument (--initdb) to initialize the database schema.
schema.sql
Contains SQL commands for creating the database table. It ensures the database is set up consistently and can be reinitialized if needed.

templates/index.html
Defines the page structure. It includes an input field, button, note list, and references to the JavaScript and CSS files.

static/main.js
This script loads the notes, listens for form submissions, and handles deletion. It’s the part of the app that gives it an interactive, “instant update” feeling.

static/styles.css
Defines the color scheme and layout. I chose a dark background with bright accent colors for readability.

requirements.txt
Lists the dependencies needed to run the project. This makes it easy for others to install the same versions I used.

Step-by-Step Usage
Clone the repository or copy the project folder.
Create a virtual environment (optional but recommended):
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
