import { Button, Card, CardHeader, Form, FormGroup, FormText, Input, Label } from 'reactstrap'

// TODO: move styles to css
export default function LoginForm() {
  return (
    <Card style={{"border": "1px solid #ddd"}}>
      <CardHeader tag="h4" className="text-center p-3">Login to TaskMaster</CardHeader>
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
            color="success"
            style={{"borderRadius": "2rem"}}
            >
              Sign In
          </Button>
        </FormGroup>
        <FormGroup className="text-center">
          <FormText tag="span">
            New user?
          </FormText>
          {" "}
          <FormText tag="a">
            Sign up
          </FormText>
        </FormGroup>
      </Form>
    </Card>
  );  
}