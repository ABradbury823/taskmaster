import {Modal, ModalBody, Form, FormGroup, Label, Input, Button } from 'reactstrap';
import { useState } from 'react';

class Task {
  constructor(taskboard_id=1, name='', description='', due_date=new Date(), assignee_id=null) {
    this.name = name;
    this.description = description;
    this.due_date = due_date.toISOString();
    this.assignee_id = assignee_id;
    this.taskboard_id = taskboard_id;
  }
}

function capitalize(str) {
  return str[0].toUpperCase() + str.slice(1);
}

function parseSnake(str) {
  return str.split('_').map(s => capitalize(s)).join(' ');
}

export default function TaskModal({ toggle, isOpen, taskInfo, update, refresh }) {
  const [task, setTask] = useState(taskInfo ?? new Task());

  function submitTask(e) {
    e.preventDefault();
    if (task.assignee_id === -1) task.assignee_id = null;
    update(task);
    setTask(new Task());
    refresh();
  }

  return (
    <Modal toggle={toggle} isOpen={isOpen}>
      <ModalBody>
        <Form>
        {Object.keys(task).filter(k => k !== 'id').map((k, i) => {
          if (taskInfo && k==='due_date') console.log(k, task[k].slice(0, -4))
          return (
          <FormGroup key={'labelClub'+i}>
            <Label>{parseSnake(k)}</Label>
            <Input type={k === 'due_date' ? 'datetime-local' : 'text'} name={'task' + parseSnake(k)}
            value={task[k] === null ? '' :  k === 'due_date' ? task[k].slice(0, -4) : task[k] }
            // TODO: need more data validation but forgoing for time
            onChange={e => {
              if (taskInfo) console.log('updated', e.target.value)
              const updatedTask = {...task, [k]: e.target.value}
              setTask(updatedTask);
            }} 
            placeholder={Task['default'+capitalize(k)]} />
          </FormGroup>)
        })}
        <Button type='submit' onClick={submitTask}>Save</Button>
      </Form>
    </ModalBody>
  </Modal>
  )
}