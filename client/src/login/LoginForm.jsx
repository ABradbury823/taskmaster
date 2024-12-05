import { Button, Card, CardHeader, Form, FormGroup, FormText, Input, Label } from 'reactstrap'
import "./LoginForm.css"

// TODO: move styles to css
export default function LoginForm() {
  return (
    <Card>
      <CardHeader tag="h2">TaskMaster Login</CardHeader>
      <Form className='m-4'>
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
          <FormText className="sign-up" tabIndex={0}>
            Sign up
          </FormText>
        </FormGroup>
      </Form>
    </Card>
  );  
}