# TaskMaster

[![codecov](https://codecov.io/gh/ABradbury823/taskmaster/graph/badge.svg?token=PUSZZCXJRH)](https://codecov.io/gh/ABradbury823/taskmaster)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A task-managing application for small teams to collaborate and develop from inception to completion. 

## Installation
Install the Python dependencies on the project's root directory
```
pip install -r requirements.txt
```
Start the application server on the project's root directory
```
python src/server.py
```
Install React dependencies on the `/client` directory
```
npm install
```
Start the React application on the `/client` directory
```
npm start
```

## Usage
Once the server is running, the taskmaster database can be
accessed through the Flask-RESTful application server.

Once the React web application is running in a browser,
navigate to the following sub-domains to access current progress.
```
http://localhost:3000/
http://localhost:3000/login
http://localhost:3000/user
```

## Acknowledgments
Thank you to Dr. Newman for providing helpful code for DB access. This project was made for SWEN-610: Foundations of Software Development.
