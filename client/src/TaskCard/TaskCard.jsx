import { useState, useEffect } from "react";
import { Card, CardTitle, CardBody, Col, CardFooter, Button } from "reactstrap";

function deleteTask(id, stateUpdater) {
  const controller = new AbortController();
  
  fetch(`http://localhost:4500/tasks/${id}`, {
    signal: controller.signal,
    method: 'DELETE',
  })
  .then(res => {
    if (res.ok) return res.json();
    throw new Error('Server failure');
  })
  .then(data => {
    // TODO: Should anything be done with deleted item, cache for undo?
    // if nothing, move function contents to res.ok conditional
    stateUpdater(id);
  })
  .catch(err => {
    alert('Something went wrong');
    console.error(err);
  })

  return () => controller.abort();
}

export default function TaskCard ({ task, removeTask, editHandler }) {
  const { id, name, description, due_date, assignee_id } = task;
  const [user, setUser] = useState(null);
  const [fetchingUser, setFetchingUser] = useState(false);

  useEffect(() => {
    // A really inefficient but effective way to get around joins
    if (assignee_id === null) return;
    setFetchingUser(true);
    const controller = new AbortController();
    fetch(`http://localhost:4500/users/${assignee_id}`, { signal: controller.signal })
      .then(res => res.json())
      .then(data => setUser(data))
      .catch(err => {
        console.error(err);
        setUser({ display_name: 'Unknown user' })
      })
      .finally(() => setFetchingUser(false));

    return () => controller.abort();
  }, [assignee_id]); 

  return (
    <Col xs={{ size: 10, offset: 1}} sm={{ size: 3, offset: 0}}>
      <Card className="m-2" style={{ minWidth: 'fit-content', maxWidth: '2rem', aspectRatio: '4 / 3', backgroundColor: '#AFFFED60', backdropFilter: 'blur(10px)' }}>
        <CardTitle style={{ 
          padding: '0.5rem',
          borderBottom: '0.05rem solid black'
        }} tag='h4'>
          {name}
        </CardTitle>
        <CardBody className="p-4 pt-0">
          <div className="d-flex flex-column flex-sm-row justify-content-between">
            {/* TODO: Since fetching user information, tooltip with user on hover could be nice */}
            <div style={{ width: 'fit-content', textAlign: "left" }}>{fetchingUser ? '...' : user?.display_name ?? 'Unassigned'}</div>
            <div style={{ width: 'fit-content', textAlign: "right" }}>Due: {due_date ? new Date(due_date).toDateString() : '-'}</div>
          </div>
          <div style={{ textAlign: 'left'}}>
            {description}
          </div>
        </CardBody>
        <CardFooter>
          <Button onClick={editHandler}>Edit</Button>
          <Button onClick={_ => deleteTask(id, removeTask)}>Delete</Button>
        </CardFooter>
      </Card>
    </Col>
  );
}