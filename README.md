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
navigate to the following sub-directories to access current progress.
```
http://localhost:3000/login
http://localhost:3000/taskboard
```

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
- Implement remaining REST resources/endpoints
- Build out a client application using React
- Connect client with backend
- ???
- Profit

## Acknowledgments
Thank you to Dr. Newman for providing helpful code for DB access.

## License
For open source projects, say how it is licensed.
