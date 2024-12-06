import {useState} from "react";
import { Button, Modal, ModalBody, ModalFooter, ModalHeader } from "reactstrap";

export default function NewUserForm({open, onSubmit, onToggle}) {
  return (
    <Modal isOpen={open} toggle={onToggle}> 
      <ModalHeader toggle={onToggle}>New User Register</ModalHeader>
      <ModalBody>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Assumenda, id consequatur et ipsum ad corporis unde minus a placeat rem ea nulla. 
        In porro, obcaecati at et eveniet minus doloribus repellat fugiat suscipit quis deserunt 
        aspernatur assumenda, fugit similique. Numquam commodi enim quasi ipsum ullam. Iste, 
        dicta assumenda. Ducimus, incidunt.
      </ModalBody>
      <ModalFooter>
        <Button color="success" onClick={onSubmit}>
          Submit
        </Button>
        {" "}
        <Button color="secondary" onClick={onToggle}>
          Cancel
        </Button>
      </ModalFooter>
    </Modal>
  )
}