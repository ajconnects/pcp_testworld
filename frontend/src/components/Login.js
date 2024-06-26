import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';
import { CForm, CFormInput, CButton, CContainer, CRow, CCol } from '@coreui/react';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/login/', { email, password }, {
        headers: {
          'Content-Type': 'application/json',
        },
      });

      localStorage.setItem('access_token', response.data.jwt);

      const userType = response.data.user_type;
      const userId = response.data.user_id;

      console.log('User ID:', userId); // Debugging

      if (userType === 'programmer') {
        navigate(`/programmer-profile/${userId}`);
      } else if (userType === 'client') {
        navigate(`/client-profile/${userId}`);
      }
    } catch (err) {
      setError('Invalid email or password');
    }
  };

  return (
    <CContainer>
      <CRow className="justify-content-center">
        <CCol md={6}>
          <h1>Login</h1>
          {error && <p style={{ color: 'red' }}>{error}</p>}
          <CForm onSubmit={handleSubmit}>
            <CFormInput
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <CFormInput
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <CButton type="submit" className="custom-button">Login</CButton>
          </CForm>
          <p className="mt-3">
            Don't have an account? <Link to="/select-user-type" className="custom-link">Register here</Link>
          </p>
        </CCol>
      </CRow>
    </CContainer>
  );
};

export default Login;