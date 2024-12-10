import { useState, useContext } from 'react';
import { AuthContext } from '../Context';
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavbarText,
} from 'reactstrap';
import HeaderItem from './HeaderItem';

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
            {user === null 
              ? <HeaderItem to="/login" label="Login" />
              : <HeaderItem to="/taskboard" label="Taskboard" />}
          </Nav>
          {user && <NavbarText>Welcome, {user}</NavbarText>}
        </Collapse>
      </Navbar>
    </header>
  );
}

export default Header;