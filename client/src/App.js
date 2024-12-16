import { Col, Container, Row } from "reactstrap";
import './App.css';

function App() {
  return (
    <Container className="App">
      <Row>
        <Col className="app-col col-1">
          <header className="App-header">
            <h1>Welcome to TaskMaster</h1>
            <h3>A comprehensive task management application designed to help 
              users organize, track, and complete their tasks efficiently.</h3>
          </header>
        </Col>
        <Col className="app-col col-2">
          <Container className="feature-list">
            <Row>
              <Col className="feature" xs="12" md="6">
                 <img width="33" height="33" src="https://img.icons8.com/android/24/user.png" alt="user"/>
                 <span>User registration and authentication</span>
              </Col>
              <Col className="feature" xs="12" md="6">
              <img width="33" height="33" src="https://img.icons8.com/ios-filled/50/checklist--v1.png" alt="checklist--v1"/>
                <span>Access and manage tasks in Taskboards</span>
              </Col>
              <Col className="feature" xs="12" md="6">
              <img width="33" height="33" src="https://img.icons8.com/ios-filled/50/postgreesql.png" alt="postgreesql"/>
                <span>Data persistence with PostgresSQL</span>
              </Col>
              <Col className="feature" xs="12" md="6">
              <img width="33" height="33" src="https://img.icons8.com/ios-filled/50/acid-flask.png" alt="acid-flask"/>
                <span>Client-server communication with Flask</span>
              </Col>
            </Row>
          </Container>
        </Col>
      </Row>
    </Container>
  );
}

export default App;
