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

  // on mount, set user to session
  useEffect(_ => {
    const cookies = document.cookie.split(';').map(cookieString => cookieString.split('='));
    if (cookies.filter(c => c[0] === 'session').length === 0) {
      sessionStorage.removeItem('username');
      setUser(null);
    } else {
      setUser(sessionStorage.getItem('username'));
    }
  }, []);

  // add function to listen to resize event
  useEffect(_ => {
    window.addEventListener('resize', handleResize);
    setHeaderOffset(headerRef.current.clientHeight)

    return _ => window.removeEventListener('resize', handleResize);
  }, [user]);

  function logout() {
    const cookies = document.cookie.split(';').map(cookieString => cookieString.split('='));
    const userId = sessionStorage.getItem("user_id");

    fetch(`http://localhost:4500/logout/${userId}`, {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'session-id': cookies[0][1]
      }
    })
    .then(res => res.json())
    .then(resData => {
      document.cookie = 'session=none;max-age=0';
      sessionStorage.setItem('username', null);
      sessionStorage.setItem('user_id', null);
      // navigate('/login');
      window.location.reload();
    })
    .catch(err => console.log(err))
  }

  return (
    <AuthContext.Provider value={user}>
      <Header logout={logout} headerRef={headerRef} expand='lg' color='light' />
      <main style={{ marginTop: headerOffset }}>
        <Outlet context={{ user, setUser }} />
      </main>
    </AuthContext.Provider>
  );
}

export default MainLayout;