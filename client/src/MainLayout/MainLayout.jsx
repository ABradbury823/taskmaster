import React, { useState } from 'react';
import Header from '../Header/Header';
import { Outlet } from 'react-router';

function MainLayout() {
  return (
    <>
      <Header />
      <main>
        <Outlet />
      </main>
    </>
  );
}

export default MainLayout;