# Voxy Job Process Challenge: Word Count API

Welcome to the Voxy Job Process Challenge repository! This project showcases a simple API with a backend written in Python using FastAPI, accompanied by a straightforward frontend utilizing vanilla JavaScript. The main functionality of this project is to count how many words therein a string while considering a list of delimiters selected by the user.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Setting Up the Backend](#setting-up-the-backend)
- [Usage](#usage)

- [License](#license)S

## Introduction

This repository contains a solution to the Voxy Job Process Challenge. The challenge involves building a simple web application consisting of a backend API that counts the occurrences of a given word within a string, considering a set of delimiters. The frontend provides an interface to interact with the API and display the results.

## Features

- Backend API built using FastAPI and Python
- Single endpoint `/count` to process word counting
- Flexible delimiter list for enhanced word counting
- Interactive frontend using vanilla JavaScript

## Technologies Used

- Python
- FastAPI
- Vanilla JavaScript
- Docker
- Git
- uvicorn

## Getting Started

### Setting Up the Backend

1. Clone this repository to your local machine.
2. Build the docker container:
   ```
   docker build -t voxy .
   ```
3. Run the container:
   ```
   docker run -p 7070:7070 voxy
   ```

## Usage

1. Access the frontend by opening a web browser and navigating to `http://localhost:7070`.
2. Enter a word and a select the delimeter you desire in the checkboxes.
3. Click the "submit" button to trigger the API request.
4. The result will be displayed on the webpage, showing the word count within the provided string.

## License

This project is licensed under the [MIT License](LICENSE).

---

We hope you enjoy exploring and using the Voxy Job Process Challenge project. If you have any questions or feedback, please don't hesitate to get in touch. Happy coding! 🚀
