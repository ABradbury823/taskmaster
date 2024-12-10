// TODO: Consider using state and react-router-dom useLocation to show active tab
import { useState, useEffect, useRef } from 'react';
import Header from '../Header/Header';
import { Outlet } from 'react-router';
import { AuthContext } from '../Context';

function MainLayout() {
  // use MainLayout to keep track of signed in user,
  // will provide context to rest of applicatoin
  const [user, setUser] = useState(null);
  
  // Enable dynamic resize of main based on fixed position nav
  const headerRef = useRef(null);
  const [headerOffset, setHeaderOffset] = useState('0px');
  function handleResize() {
    setHeaderOffset(headerRef.current.clientHeight);
  }

  // add function to listen to resize event
  useEffect(_ => {
    window.addEventListener('resize', handleResize);
    setHeaderOffset(headerRef.current.clientHeight)

    return _ => window.removeEventListener('resize', handleResize);
  }, [user]);

  return (
    <AuthContext.Provider value={user}>
      <Header headerRef={headerRef} expand='lg' color='light' />
      <main style={{ marginTop: headerOffset }}>
        <Outlet context={{ user, setUser }} />
      </main>
    </AuthContext.Provider>
  );
}

export default MainLayout;