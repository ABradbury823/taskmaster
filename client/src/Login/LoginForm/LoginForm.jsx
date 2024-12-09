import { Button, Card, CardHeader, Form, FormGroup, FormText, Input, Label } from 'reactstrap'
import "./LoginForm.css"
import NewUserForm from "../NewUserForm/NewUserForm";
import { useState } from "react";
import { useOutletContext } from 'react-router';

export default function LoginForm() {
  const [newUserModal, setNewUserModal] = useState(false);
  const { setUser } = useOutletContext();

  function toggleNewUserModal() {
    setNewUserModal(!newUserModal);
  }

  return (
    <Card>
      <CardHeader tag="h2">TaskMaster Login</CardHeader>
      <Form onSubmit={(e) => {
        // TODO: Verify in data and set user context
        e.preventDefault();
        const data = new FormData(e.target);
        setUser(data.get('username'));
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
            onSubmit={() => {console.log("Create new user"); toggleNewUserModal();}}
            onToggle={toggleNewUserModal}
          />
        </FormGroup>
      </Form>
    </Card>
  );  
}