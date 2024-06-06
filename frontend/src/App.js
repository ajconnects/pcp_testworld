import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css'; // CoreUI depends on Bootstrap
import '@coreui/coreui/dist/css/coreui.min.css'; // CoreUI CSS
import ProgrammerForm from './components/ProgrammerForm';
import ClientForm from './components/ClientForm';

function App() {
    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="/register-programmer" element={<ProgrammerForm />} />
                    <Route path="/register-client" element={<ClientForm />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;