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

      localStorage.setItem('access_token', response.data.token);

      if (response.data.user_type === 'programmer') {
        navigate(`/programmer-profile/${response.data.user_id}`);
      } else if (response.data.user_type === 'client') {
        navigate(`/client-profile/${response.data.user_id}`);
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
            <CButton type="submit" color="primary">Login</CButton>
          </CForm>
          <p className="mt-3">
            Don't have an account? <Link to="/select-user-type">Register here</Link>
          </p>
        </CCol>
      </CRow>
    </CContainer>
  );
};

export default Login;