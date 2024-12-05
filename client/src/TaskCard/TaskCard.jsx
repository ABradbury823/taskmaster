import { Card, CardTitle, CardBody } from "reactstrap";

export default function TaskCard ({ task }) {
  const { name, description } = task;
  return (
    <Card>
      <CardTitle tag='h4'>
        {name}
      </CardTitle>
      <CardBody>
        {description}
      </CardBody>
    </Card>
  );
}