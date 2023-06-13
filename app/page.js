'use client'

import Home from "./home"
import SignUpForm from "./components/signupform"
import LoginForm from "./components/loginform"

import React, { useEffect, useState } from 'react';

export default function RootPage() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const check_session_response = await fetch("/api/check_session");
        if (check_session_response.ok) {
          const user = await check_session_response.json();
          setUser(user);
        }
      } catch (error) {
        console.log(error)
      }
    }
    fetchData()
  }, []);

  return (
    <div>
      {user ? 
      <div>
        <Home onSetUser={setUser} user={user}/>
      </div> : 
      <div>
        <SignUpForm onLogin={setUser}/>
        <LoginForm onLogin={setUser}/>
      </div>}
    </div>
  )
}
