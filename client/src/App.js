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
          Column 2
        </Col>
      </Row>
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
    </Container>
  );
}

export default App;
