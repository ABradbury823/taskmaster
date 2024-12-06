import { useState, useEffect } from 'react';
import { Container, Row } from "reactstrap";
import TaskCard from "../TaskCard/TaskCard";

export default function Taskboard() {

  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const controller = new AbortController();
    fetch('http://localhost:4500/tasks', { signal: controller.signal })
      .then(res => res.json())
      .then(data => setTasks(data))
      .catch(err => console.error(err))
      .finally(() => setLoading(false));

    return () => controller.abort();
  }, []);

  return (
    <Container fluid>
      <Row className="gx-0">
        {loading ? 'loading' : tasks.map(task => <TaskCard key={task.id} task={task} />)}
      </Row>
    </Container>
  );
}