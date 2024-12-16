import { Button, Card, CardHeader, Form, FormGroup, FormText, Input, Label } from 'reactstrap'
import "./LoginForm.css"
import NewUserForm from "../NewUserForm/NewUserForm";
import { useState } from "react";
import { useNavigate, useOutletContext } from 'react-router';

export default function LoginForm() {
  // Form with field validation for new user creation
  const [newUserModal, setNewUserModal] = useState(false);
  const { setUser } = useOutletContext();
  const navigate = useNavigate();

  function toggleNewUserModal() {
    setNewUserModal(!newUserModal);
  }

  // Start a new user session given a username and password
  function login(username, password) {
    const expireDate = new Date();
    expireDate.setSeconds(expireDate.getSeconds() + 300);
    fetch('http://localhost:4500/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: username,
        password: password,
        expires_at: expireDate.toISOString()
      })
    }).then(res => res.json())
    .then(resData => {
      if (resData.session_id) {
        document.cookie = `session=${resData.session_id};`
        sessionStorage.setItem('username', username)
        sessionStorage.setItem('user_id', resData.user_id)
        sessionStorage.setItem('session_expires_at', new Date(resData.expires_at));
        setUser(username)
        navigate('/taskboard')
      } else {
        alert(resData.message)
      }
    })
    .catch(err => {
      alert('Something went wrong...')
      console.error(err)
    })
  }

  return (
    <Card>
      <CardHeader tag="h2">TaskMaster Login</CardHeader>
      <Form onSubmit={(e) => {
        e.preventDefault()
        const data = new FormData(e.target);
        const username = data.get('username');
        const password = data.get('password');
        login(username, password)
        }} className='m-4'>
        <FormGroup floating>
          <Input
            id="username"
            name="username"
            placeholder="Username"
            type="text"
          />
          <Label for="username">
            Username
          </Label>
        </FormGroup>
        <FormGroup floating>
          <Input
            id="password"
            name="password"
            placeholder="Password"
            type="password"
          />
          <Label for="password">
            Password
          </Label>
        </FormGroup>
        <FormGroup className="py-3">
          <Button 
            block 
            type="submit"
            >
              Sign In
          </Button>
        </FormGroup>
        <FormGroup>
          <FormText tag="span">
            New user?
          </FormText>
          {" "}
          <FormText className="sign-up" tabIndex={0} onClick={toggleNewUserModal}>
            Sign up
          </FormText>
          <NewUserForm
            open={newUserModal}
            onSubmit={(e) => {
              e.preventDefault();
              const data = new FormData(e.target.parentElement.parentElement.children[1].children[0]);
              const body = {
                name: data.get('new-username'),
                password: data.get('new-password'),
                email: data.get('new-email'),
                display_name: data.get('new-display_name'),
                bio: data.get('new-bio'),
              };
              fetch('http://localhost:4500/users', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(body)
              }).then(res => res.json())
              .then(resData => {
                if (resData?.name === body.name) {
                  const username = data.get('new-username');
                  const password = data.get('new-password');
                  login(username, password)
                } else {
                  alert('Failed')
                }
              })
              .catch(err => console.error(err))
              toggleNewUserModal();
            }}
            onToggle={toggleNewUserModal}
          />
        </FormGroup>
      </Form>
    </Card>
  );  
}