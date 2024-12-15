import { Link } from 'react-router';
import { NavItem, NavLink } from 'reactstrap';

export default function HeaderItem({to, label}) {
  return (
    <NavItem>
      <Link style={{padding: '0.2rem', textDecoration: 'none'}} to={to}>
        <NavLink tag='span'>{label}</NavLink>
      </Link>
    </NavItem>
  );
}