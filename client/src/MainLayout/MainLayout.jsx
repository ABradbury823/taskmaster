// TODO: Consider using state and react-router-dom useLocation to show active tab
// import React, { useState } from 'react';
import { useState, useEffect, useRef } from 'react';
import Header from '../Header/Header';
import { Outlet } from 'react-router';

function MainLayout() {
  const [headerOffset, setHeaderOffset] = useState('0px');
  const headerRef = useRef(null);
  useEffect(_ => {
    setHeaderOffset(headerRef.current.clientHeight);
  }, []);

  return (
    <>
      <Header headerRef={headerRef} expand='lg' color='light' />
      <main style={{ marginTop: headerOffset }}>
        <Outlet />
      </main>
    </>
  );
}

export default MainLayout;