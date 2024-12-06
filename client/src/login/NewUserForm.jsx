import {useState} from "react";
import { Button, Form, FormGroup, FormText, Input, Label, Modal, ModalBody, ModalFooter, ModalHeader } from "reactstrap";

export default function NewUserForm({open, onSubmit, onToggle}) {
  const [username, setUsername] = useState("");
  const [displayName, setDisplayName] = useState("");

  const updateUsername = e => setUsername(e.target.value);
  const updateDisplayName = e => setDisplayName(e.target.value);

  function resetValues() {
    setUsername("");
    setDisplayName("");
  }

  function handleToggle() {
    resetValues();
    onToggle();
  }

  // TODO: validate data
  function handleSubmit() {
    onSubmit();
    
    resetValues();
  }

  return (
    <Modal isOpen={open} toggle={handleToggle} centered> 
      <ModalHeader toggle={handleToggle}>TaskMaster Sign Up</ModalHeader>
      <ModalBody>
        <Form>
          <FormGroup floating>
            <Input
              id="new-username"
              name="new-username"
              placeholder="Username"
              type="text"
              onChange={updateUsername}
              required
            />
            <Label for="new-username">Username</Label>
          </FormGroup>
          <FormGroup floating>
            <Input
              id="new-email"
              name="new-email"
              placeholder="Email"
              type="email"
              required
            />
            <Label for="new-email">Email</Label>
          </FormGroup>
          <FormGroup floating>
            <Input
              id="new-password"
              name="new-password"
              placeholder="Password"
              type="password"
              required
            />
            <Label for="new-password">Password</Label>
          </FormGroup>
          <FormGroup floating>
            <Input
              id="retype-password"
              name="retype-password"
              placeholder="Re-type Password"
              type="password"
              required
            />
            <Label for="retype-password">Re-Type Password</Label>
          </FormGroup>
          <FormGroup floating>
            <Input
              id="new-display-name"
              name="new-display-name"
              placeholder="Display Name (Optional)"
              type="text"
              onChange={updateDisplayName}
            />
            <Label for="new-display-name">Display Name (Optional)</Label>
            <FormText>
              This is the name other people will see you as:{" "}
              {
                <FormText color="success">
                  {displayName !== "" ? displayName : username}
                </FormText>
              }
            </FormText>
          </FormGroup>
          <FormGroup floating>
            <Input
              id="new-bio"
              name="new-bio"
              placeholder="About me..."
              type="text"
            />
            <Label for="new-bio">About Me (Optional)</Label>
            <FormText>
              Tell us a little bit about yourself!
            </FormText>
          </FormGroup>
        </Form>
      </ModalBody>
      <ModalFooter>
        <Button type="submit" onClick={handleSubmit}>
          Submit
        </Button>
        {" "}
        <Button color="secondary" onClick={handleToggle}>
          Cancel
        </Button>
      </ModalFooter>
    </Modal>
  )
}