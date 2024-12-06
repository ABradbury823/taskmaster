import { Card, CardTitle, CardBody, Row, Col, Container } from "reactstrap";

export default function TaskCard ({ task }) {
  const { name, description, due_date, assignee_id } = task;
  return (
    <Col xs={{ size: 10, offset: 1}} sm={{ size: 3, offset: 0}}>
      <Card style={{ maxWidth: '18rem', minWidth: 'fit-content' }} >
        <CardTitle style={{ 
          padding: '0.5rem',
          borderBottom: '0.05rem solid black'
        }} tag='h4'>
          {name}
        </CardTitle>
        <CardBody className="p-4 pt-0">
          <Row>
            <Col xs="6">
              {assignee_id}
            </Col>
            <Col xs="6">
              {due_date}
            </Col>
          </Row>
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