import { useState, useEffect, useContext } from 'react';
import { Button, Container, Row } from "reactstrap";
import TaskModal from './TaskModal';
import TaskCard from "../TaskCard/TaskCard";
import { AuthContext } from '../Context';
import { useNavigate } from 'react-router';

export default function Taskboard({ taskboard }) {
  // A component that renders information about a provided task board
  // Includes name and tasks associated with board
  // Renders TaskCards and Modals
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(false);
  const [showNewTaskModal, setShowNewTaskModal] = useState(false);
  const [showEditTaskModal, setShowEditTaskModal] = useState(false);
  const [edittedTask, setEdittedTask] = useState(null);
  const user = useContext(AuthContext);
  const navigate = useNavigate();
  // let { taskboardId } = useParams();

  function removeTask(deletedId) {
    // Remove the task from the front end
    setTasks(tasks.filter(task => task.id !== deletedId))
  }

  function postTask(task) {
    // Send the updated task state to the data base
    // Add the newly created task to the front end upon successful response
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
    .catch(err => console.error(err));
  }

  function editHandler(e, task) {
    // Edit initialization with provide task
    // Task supplied in TaskCard component
    e.preventDefault();
    setEdittedTask(task);
    setShowEditTaskModal(true);
  }

  function updateTask(task) {
    // Send the updated task state to the data base
    // Update the task on the front end upon successful response
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
    // Close and remove state from the edit task modal
    setEdittedTask(null);
    setShowEditTaskModal(false);
  }

  useEffect(() => {
    if (user === null) {
      navigate('/login');
      return;
    }

    const controller = new AbortController();
    fetch(`http://localhost:4500/tasks?taskboard_id=${taskboard.id}`, { signal: controller.signal })
      .then(res => res.json())
      .then(data => setTasks(data))
      .catch(err => console.error(err))
      .finally(() => setLoading(false));

    return () => controller.abort();
  }, [user, taskboard, navigate]);

  return (
    <div>
      <h2>
        {taskboard.name}
      </h2>
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
            : tasks.length && tasks.map(task => (
              <TaskCard 
                key={task.id} 
                task={task} 
                removeTask={removeTask} 
                editHandler={e => editHandler(e, task)}
              />
            ))}
        </Row>
      </Container>
    </div>
  );
}