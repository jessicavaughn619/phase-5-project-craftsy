'use client'

import axios from 'axios';

export default function GoogleLogin() {
  const handleLogin = async () => {
    try {
      const response = await axios.post('api/login');
      // Handle success response
      console.log(response.data);
    } catch (error) {
      // Handle error response
      console.error(error);
    }
  };
  return (
    <div>
    <h1>Hello!</h1>
    <button onClick={handleLogin}>Login with Google</button>
  </div>
  )
}