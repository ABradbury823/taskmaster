import { AuthContext } from "../Context";
import { useState, useEffect, useContext } from "react";
import Taskboard from "../Taskboard/Taskboard";
import { useNavigate } from "react-router";

export default function UserDashboard() {
  const user = useContext(AuthContext);
  const [taskboards, setTaskboards] = useState([]);
  const navigate = useNavigate();

  useEffect(_ => {
    if (user === null) navigate('/login');
    const controller = new AbortController();

    fetch('http://localhost:4500/taskboards')
      .then(res => res.json())
      .then(data => setTaskboards(data))
      .catch(err => console.error(err));

    return _ => controller.abort();
  }, []);

  return (<div>
    User dashboard: {user}
    {taskboards.length && taskboards.map(tb => (
      <Taskboard taskboard={tb} />
    ))}
  </div>)
}