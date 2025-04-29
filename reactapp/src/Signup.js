import React, { useState } from 'react';
import axios from 'axios';

function Signup({ switchToLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSignup = async (e) => {
    e.preventDefault();

    // Input validation (example: checking if username and password are provided)
    if (!username || !password) {
      setMessage('Please enter both username and password.');
      return;
    }

    try {
      const response = await axios.post('http://localhost:5000/signup', { username, password });
      setMessage(response.data.message);  // Success message from backend
      console.log(response.data.message);
    } catch (error) {
      setMessage(error.response ? error.response.data.message : 'Signup failed. Please try again.');
    }
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '100px' }}>
      <h2>Sign Up</h2>
      <form onSubmit={handleSignup}>
        <input 
          type="text" 
          placeholder="Username" 
          value={username} 
          onChange={(e) => setUsername(e.target.value)} 
        /><br/><br/>
        <input 
          type="password" 
          placeholder="Password" 
          value={password} 
          onChange={(e) => setPassword(e.target.value)} 
        /><br/><br/>
        <button type="submit">Sign Up</button>
      </form>
      <p>{message}</p>
      <p>Already have an account? <button onClick={switchToLogin}>Login</button></p>
    </div>
  );
}

export default Signup;
