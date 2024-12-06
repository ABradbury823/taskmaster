import { useState, useEffect } from "react";
import { Card, CardTitle, CardBody, Row, Col } from "reactstrap";

export default function TaskCard ({ task }) {
  const { name, description, due_date, assignee_id } = task;
  const [user, setUser] = useState(null);

  useEffect(() => {
    // A really inefficient but effective way to get around joins
    if (assignee_id === null) return;
    const controller = new AbortController();
    fetch(`http://localhost:4500/users/${assignee_id}`, { signal: controller.signal })
      .then(res => res.json())
      .then(data => setUser(data))
      .catch(err => console.error(err));

    return () => controller.abort();
  }, [assignee_id]); 

  return (
    <Col xs={{ size: 10, offset: 1}} sm={{ size: 3, offset: 0}}>
      <Card className="m-2">
        <CardTitle style={{ 
          padding: '0.5rem',
          borderBottom: '0.05rem solid black'
        }} tag='h4'>
          {name}
        </CardTitle>
        <CardBody className="p-4 pt-0">
          <div className="d-flex flex-column flex-sm-row justify-content-between">
            <div style={{ width: 'fit-content', textAlign: "left" }}>{user?.display_name ?? 'Unassigned'}</div>
            <div style={{ width: 'fit-content', textAlign: "right" }}>Due: {due_date ? new Date(due_date).toDateString() : '-'}</div>
          </div>
          <Row style={{ textAlign: "left"}}>
            <Col xs="12">
              {description}
            </Col>
          </Row>
        </CardBody>
      </Card>
    </Col>
  );
}