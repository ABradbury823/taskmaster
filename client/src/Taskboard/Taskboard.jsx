import { useState, useEffect, useContext } from 'react';
import { Button, Container, Row } from "reactstrap";
import TaskModal from './TaskModal';
import TaskCard from "../TaskCard/TaskCard";
import { AuthContext } from '../Context';
import { useNavigate } from 'react-router';

export default function Taskboard() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(false);
  const [showNewTaskModal, setShowNewTaskModal] = useState(false);
  const [showEditTaskModal, setShowEditTaskModal] = useState(false);
  const [edittedTask, setEdittedTask] = useState(null);
  const user = useContext(AuthContext);
  const navigate = useNavigate();

  function removeTask(deletedId) {
    setTasks(tasks.filter(task => task.id !== deletedId))
  }

  function postTask(task) {
    if (task.due_date === ':00.000Z') task.due_date = null;
    fetch('http://localhost:4500/tasks', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(task)
    })
    .then(res => {
      if (res.ok) return res.json();
      throw new Error('Failed to create task');
    })
    .then(newTask => setTasks(tasks.concat(newTask)))
    .catch(err => console.error(err))
  }

  function editHandler(e, task) {
    e.preventDefault();
    setEdittedTask(task);
    setShowEditTaskModal(true);
  }

  function updateTask(task) {
    if (task.due_date === ':00.000Z') task.due_date = null;
    fetch(`http://localhost:4500/tasks/${task.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(task)
    })
    .then(res => {
      if (res.ok) return res.json();
      throw new Error('Failed to update task');
    })
    .then(updatedTask => {
      setTasks(tasks.map(t => t.id === updatedTask.id
          ? updatedTask
          : t));
    })
    .catch(err => console.error(err))
  }

  function refresh() {
    setEdittedTask(null);
    setShowEditTaskModal(false);
  }

  useEffect(() => {
    if (user === null) {
      navigate('/login');
      return;
    }

    const controller = new AbortController();
    fetch('http://localhost:4500/tasks', { signal: controller.signal })
      .then(res => res.json())
      .then(data => setTasks(data))
      .catch(err => console.error(err))
      .finally(() => setLoading(false));

    return () => controller.abort();
  }, [user, navigate]);

  return (
    <>
      <Button tag={'button'} onClick={_ => setShowNewTaskModal(true)}>Add New Task</Button>
      {edittedTask !== null && <TaskModal
          toggle={refresh}
          isOpen={showEditTaskModal}
          taskInfo={edittedTask}
          update={updateTask}
          refresh={refresh}
        />
        }
        <TaskModal
          toggle={_ => setShowNewTaskModal(false)}
          isOpen={showNewTaskModal}
          update={postTask}
          refresh={_ => setShowNewTaskModal(false)}
        />
      <Container fluid>
        <Row className="gx-0">
          {loading 
            ? 'loading' 
            : tasks.map(task => (
              <TaskCard 
                key={task.id} 
                task={task} 
                removeTask={removeTask} 
                editHandler={e => editHandler(e, task)}
              />
            ))}
        </Row>
      </Container>
    </>
  );
}