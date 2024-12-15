import {useState} from "react";
import { Button, Form, FormFeedback, FormGroup, FormText, Input, Label, Modal, ModalBody, ModalFooter, ModalHeader } from "reactstrap";

export default function NewUserForm({open, onSubmit, onToggle}) {
  // maybe this could be simplified down to one state object for the whole form?
  const [username, setUsername] = useState({value: "", invalid: false, feedback: ""});
  const [email, setEmail] = useState({value: "", invalid: false, feedback: ""});
  const [password, setPassword] = useState({value: "", invalid: false, feedback: ""});
  const [confirmPassword, setConfirmPassword] = useState({value: "", invalid: false, feedback: ""});
  const [displayName, setDisplayName] = useState("");
  const [bio, setBio] = useState("");
  const [invalidSubmit, setInvalidSubmit] = useState(false);
  const [submitMessage, setSubmitMessage] = useState("");

  function updateUsername(input) { 
    const newUsername = {...username};
    newUsername.value = input;
    if(input === "") {
      newUsername.invalid = true;
      newUsername.feedback = "Username is required"
    } else if (username.invalid && input !== "") {
      newUsername.invalid = false;
      newUsername.feedback = "";
    }
    setUsername(newUsername);
  }
  function updateEmail(input) {
    const newEmail = {...email};
    newEmail.value = input;
    if(input === "") {
      newEmail.invalid = true;
      newEmail.feedback = "Email is required"
    } else if (email.invalid && input !== "") {
      newEmail.invalid = false;
      newEmail.feedback = "";
    }
    setEmail(newEmail);
  }
  function updatePassword(input) { 
    const newPassword = {...password};
    newPassword.value = input;
    if(input === "") {
      newPassword.invalid = true;
      newPassword.feedback = "Password is required"
    } else if (password.invalid && input !== "") {
      newPassword.invalid = false;
      newPassword.feedback = "";
    }
    setPassword(newPassword);
  }
  function updateConfirmPassword(input) { 
    const newRetype = {...confirmPassword};
    newRetype.value = input;
    if(input !== password.value) {
      newRetype.invalid = true;
      newRetype.feedback = "Passwords do not match";
    } else if (input === password.value || password.value === "" || input === "") {
      newRetype.invalid = false;
      newRetype.feedback = "";
    }
    setConfirmPassword(newRetype); 
  }
  const updateDisplayName = input => { setDisplayName(input); }
  const updateBio = input => { setBio(input); }

  function resetValues() {
    setUsername({value: "", invalid: false, feedback: ""});
    setDisplayName({value: "", invalid: false, feedback: ""});
    setPassword({value: "", invalid: false, feedback: ""});
    setConfirmPassword({value: "", invalid: false, feedback: ""});
    setDisplayName("");
    setBio("");
    setInvalidSubmit(false);
    setSubmitMessage("");
  }

  function handleToggle() {
    onToggle();
    resetValues();
  }

  // TODO: validate data
  function handleSubmit(e) {

    if(username.value === "" || email.value === "" ||
      password.value === "" || confirmPassword === ""
    ) {
      setInvalidSubmit(true);
      setSubmitMessage("Please fill the required field(s)");
      return;
    } else if(username.invalid || email.invalid ||
      password.invalid || confirmPassword.invalid
    ) {
      setInvalidSubmit(true);
      setSubmitMessage("Please fix the invalid field(s)")
      return;
    }

    // TODO: check that username and email are available


    onSubmit(e);
    
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
              onChange={e => updateUsername(e.target.value)}
              invalid = {username.invalid}
              required
            />
            <Label for="new-username">Username</Label>
            <FormFeedback>{username.feedback}</FormFeedback>
          </FormGroup>
          <FormGroup floating>
            <Input
              id="new-email"
              name="new-email"
              placeholder="Email"
              type="email"
              onChange={e => updateEmail(e.target.value)}
              invalid = {email.invalid}
              required
            />
            <Label for="new-email">Email</Label>
            <FormFeedback>{email.feedback}</FormFeedback>
          </FormGroup>
          <FormGroup floating>
            <Input
              id="new-password"
              name="new-password"
              placeholder="Password"
              type="password"
              onChange={e => updatePassword(e.target.value)}
              invalid={password.invalid}
              required
            />
            <Label for="new-password">Password</Label>
            <FormFeedback>{password.feedback}</FormFeedback>
          </FormGroup>
          <FormGroup floating>
            <Input
              id="confirm-password"
              name="confirm-password"
              placeholder="Confirm Password"
              type="password"
              onChange={e => updateConfirmPassword(e.target.value)}
              invalid = {confirmPassword.invalid}
              required
            />
            <Label for="confirm-password">Confirm Password</Label>
            <FormFeedback>{confirmPassword.feedback}</FormFeedback>
          </FormGroup>
          <FormGroup floating>
            <Input
              id="new-display-name"
              name="new-display-name"
              placeholder="Display Name (Optional)"
              type="text"
              onChange={e => updateDisplayName(e.target.value)}
            />
            <Label for="new-display-name">Display Name (Optional)</Label>
            <FormText>
              This is the name other people will see you as:{" "}
              {
                <FormText color="success">
                  {displayName !== "" ? displayName : username.value}
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
              onChange={updateBio}
            />
            <Label for="new-bio">About Me (Optional)</Label>
            <FormText>
              Tell us a little bit about yourself!
            </FormText>
          </FormGroup>
        </Form>
      </ModalBody>
      <ModalFooter>
        <FormText color="danger" hidden={!invalidSubmit}>{submitMessage}</FormText>
        <Button 
          type="submit" 
          onClick={e => handleSubmit(e)}
        >
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