import { Col, Container, Row } from "reactstrap";
import LoginForm from "./LoginForm";
import './Login.css'

export default function Login() {
  return (
    <Container>
      <Row>
        <Col xs="1" sm="2" md="3" lg="4"></Col>
        <Col xs="10" sm="8" md="6" lg="4">
          <LoginForm/>
        </Col>
        <Col xs="1" sm="2" md="3" lg="4"></Col>
      </Row>
    </Container>
    // </div>
  );  
}