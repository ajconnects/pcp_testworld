import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import '@coreui/coreui/dist/css/coreui.min.css';
import { MDBContainer } from 'mdb-react-ui-kit';
import 'mdb-react-ui-kit/dist/css/mdb.min.css';
import './App.css';

import Navbar from './components/Navbar';
import MarketingMessage from './components/MarketingMessage';
import Categories from './components/Categories';
import ProgrammerForm from './components/ProgrammerForm';
import ClientForm from './components/ClientForm';
import ClientProfile from './components/ClientProfile';
import ProgrammerProfile from './components/ProgrammerProfile';
import Login from './components/Login';
import UserTypeSelection from './components/UserTypeSelect';

function App() {
  const [visible, setVisible] = useState(false);

  return (
    <Router>
      <div className="App">
        <Navbar visible={visible} setVisible={setVisible} />
        <div className="main-content">
          <MDBContainer>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/register-programmer" element={<ProgrammerForm />} />
              <Route path="/programmer-profile/:id" element={<ProgrammerProfile />} />
              <Route path="/register-client" element={<ClientForm />} />
              <Route path="/client-profile/:id" element={<ClientProfile />} />
              <Route path="/login" element={<Login />} />
              <Route path="/select-user-type" element={<UserTypeSelection />} />
            </Routes>
          </MDBContainer>
        </div>
      </div>
    </Router>
  );
}

// Example home component to display MarketingMessage and Categories
const Home = () => (
  <>
    <MarketingMessage />
    <Categories />
  </>
);

export default App;