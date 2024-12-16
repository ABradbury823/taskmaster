# TaskMaster

A task-managing application for small teams to collaborate and
develop for inception to completion.

## Installation
To install Python dependencies use the command
```
pip install -r requirements.txt
```
Start the application server with the following command
from the project's root directory
```
python src/server.py
```
To install React dependencies use the following command
from the project's `/client` directory
```
npm install
```
Start the React application with the following command
from the project's `/client` directory
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

## Roadmap
- ~~Implement remaining REST resources/endpoints~~
- ~~Build out a client application using React~~
- ~~Connect client with backend~~
- Implement update and delete methods in Table class
- Implement teams and categories APIs on server
- Build out team parameterized endpoints
- Add UI for task filters

## Acknowledgments
Thank you to Dr. Newman for providing helpful code for DB access.
