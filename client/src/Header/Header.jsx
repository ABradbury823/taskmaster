import { useState, useContext } from 'react';
import { AuthContext } from '../Context';
import { Link } from 'react-router';
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  NavbarText,
} from 'reactstrap';

function Header({headerRef, ...args}) {
  const [isOpen, setIsOpen] = useState(false);
  const user = useContext(AuthContext);

  const toggle = () => setIsOpen(!isOpen);

  return (
    <header style={{position: 'fixed', width: '100%', top: '0', zIndex: '1'}} ref={headerRef}>
      <Navbar {...args}>
        <NavbarBrand href="/">TaskMaster</NavbarBrand>
        <NavbarToggler onClick={toggle} />
        <Collapse isOpen={isOpen} navbar>
          <Nav className="me-auto" navbar>
            <NavItem>
              {!user && <Link style={{padding: '0.2rem', textDecoration: 'none'}} to="/login">
                <NavLink tag='span'>Login</NavLink>
              </Link>}
            </NavItem>
            {user &&
            <NavItem>
              <Link style={{padding: '0.2rem', textDecoration: 'none'}} to="/taskboard">
                  <NavLink tag='span'>
                    Taskboard
                  </NavLink>
              </Link>
            </NavItem>
            }
          </Nav>
          <NavbarText>{user ? `Welcome, ${user}` : 'Login'}</NavbarText>
        </Collapse>
      </Navbar>
    </header>
  );
}

export default Header;