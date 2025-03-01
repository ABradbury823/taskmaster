import { Col, Container, Row } from "reactstrap";
import LoginForm from "./LoginForm/LoginForm";
import './Login.css'
import { useEffect, useContext } from 'react';
import { AuthContext } from '../Context';
import { useNavigate } from 'react-router';

export default function Login() {
  // Layout component for Login form
  const user = useContext(AuthContext);
  const navigate = useNavigate();

  useEffect(() => {
      if (user !== null) {
        navigate('/user');
        return;
      }
    }, [user, navigate]);

  return (
    <Container className="Login">
      <Row>
        <Col xs="1" sm="2" md="3" xxl="4"></Col>
        <Col xs="10" sm="8" md="6" xxl="4">
          <LoginForm/>
        </Col>
        <Col xs="1" sm="2" md="3" xxl="4"></Col>
      </Row>
    </Container>
  );  
}