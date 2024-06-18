import React, { useState } from 'react';
import {
  CNavbar,
  CContainer,
  CNavbarBrand,
  CNavbarToggler,
  CCollapse,
  CNavbarNav,
  CDropdown,
  CDropdownToggle,
  CDropdownMenu,
  CDropdownItem,
  CButton,
  CForm,
  CFormInput
} from '@coreui/react';
import { Link, useNavigate } from 'react-router-dom';
import MultilevelDropdown from 'react-multilevel-dropdown';

function Navbar({ visible, setVisible }) {
  const items = [
    {
      title: 'Our Team',
      submenu: [
        { title: 'Sami' },
        { title: 'Aj' },
        { title: 'Paula' }
      ]
    },
    {
      title: 'Our Product',
      submenu: [
        { title: 'Find Work' },
        { title: 'Why P.C.P' },
        { title: 'News' }
      ]
    }
  ];

  const [signupDropdownOpen, setSignupDropdownOpen] = useState(false);
  const navigate = useNavigate();

  const toggleSignupDropdown = () => {
    setSignupDropdownOpen(!signupDropdownOpen);
  };

  return (
    <CNavbar expand="lg" className="bg-body-tertiary">
      <CContainer fluid>
        <CNavbarBrand href="#">
          <img src="/static/d.png" alt="" style={{ maxHeight: '80px' }} />
        </CNavbarBrand>
        <CNavbarToggler onClick={() => setVisible(!visible)} />
        <CCollapse className="navbar-collapse" visible={visible}>
          <CNavbarNav>
            {items.map((item, index) => (
              <MultilevelDropdown
                key={index}
                title={item.title}
                items={item.submenu}
              />
            ))}
          </CNavbarNav>
          <CNavbarNav className="ms-auto">
            <CForm className="d-flex me-3">
              <CFormInput type="search" placeholder="Search" />
              <CButton type="submit" color="success" variant="outline" className="ms-2">
                Search
              </CButton>
            </CForm>
            <CDropdown isOpen={signupDropdownOpen} toggle={toggleSignupDropdown}>
              <CDropdownToggle color="secondary">Sign up</CDropdownToggle>
              <CDropdownMenu>
                <CDropdownItem>
                  <Link to="/register-programmer">Programmers</Link>
                </CDropdownItem>
                <CDropdownItem>
                  <Link to="/register-client">Clients</Link>
                </CDropdownItem>
              </CDropdownMenu>
            </CDropdown>
            <CButton color="primary" className="me-2" onClick={() => navigate('/login')}>
              Login
            </CButton>
          </CNavbarNav>
        </CCollapse>
      </CContainer>
    </CNavbar>
  );
}

export default Navbar;