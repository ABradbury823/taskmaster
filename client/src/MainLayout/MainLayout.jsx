// TODO: Consider using state and react-router-dom useLocation to show active tab
// import React, { useState } from 'react';
import { useState, useEffect, useRef } from 'react';
import Header from '../Header/Header';
import { Outlet } from 'react-router';
import { AuthContext } from '../Context';

function MainLayout() {
  const [headerOffset, setHeaderOffset] = useState('0px');
  const [user, setUser] = useState(null);
  console.log(user)

  const headerRef = useRef(null);
  useEffect(_ => {
    setHeaderOffset(headerRef.current.clientHeight);
  }, []);

  return (
    <>
      <AuthContext.Provider value={user}>
        <Header headerRef={headerRef} expand='lg' color='light' />
      </AuthContext.Provider>
      <main style={{ marginTop: headerOffset }}>
        <Outlet context={{ user, setUser }} />
      </main>
    </>
  );
}

export default MainLayout;