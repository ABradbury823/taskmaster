import { Container, Row } from "reactstrap";
import TaskCard from "../TaskCard/TaskCard";

const dummy = {name: 'Task name', description: 'Task description', due_date: '10/12/12', assignee_id: 'me'}
const dummyArr = []
for (let i = 0; i < 10; i++) {
  dummyArr.push(dummy)
}

export default function Taskboard() {
  return (
    <Container fluid>
      <Row className="gx-0">
        {dummyArr.map((task, i) => <TaskCard key={i} task={task} />)}
      </Row>
    </Container>
  );
}