import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css'; // CoreUI depends on Bootstrap
import '@coreui/coreui/dist/css/coreui.min.css'; // CoreUI CSS
import ProgrammerForm from './components/ProgrammerForm';
import ClientForm from './components/ClientForm';
import ClientProfile from './components/ClientProfile';
import ProgrammerProfile from './components/ProgrammerProfile';

function App() {
    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="/register-programmer" element={<ProgrammerForm />} />
                    <Route path="/programmer-profile/:id" element={<ProgrammerProfile />} />
                    <Route path="/register-client" element={<ClientForm />} />
                    <Route path="/client-profile/:id" element={<ClientProfile />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;