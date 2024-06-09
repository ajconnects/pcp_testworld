import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { CFormInput, CForm, CCol, CButton, CFormCheck, CFormFeedback, CFormTextarea } from '@coreui/react';

const ClientForm = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: '',
        phone_number: '',
        address: '',
        bio: '',
        profile_picture: null,
    });

    const navigate = useNavigate();

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleFileChange = (e) => {
        setFormData({
            ...formData,
            profile_picture: e.target.files[0],
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const form = new FormData();
        for (let key in formData) {
            if (formData[key] !== null) {
                form.append(key, formData[key]);
            }
        }

        try {
            const response = await axios.post('http://127.0.0.1:8000/client/', form, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            const clientId = response.data.id; // Assuming the response contains the new client's ID
            navigate(`/client-profile/${clientId}`); // Redirect to the profile page
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <h1>Client Registration Form:</h1>
            <br/>
            <CForm className="row g-3" onSubmit={handleSubmit} style={{ maxWidth: '600px' }}>
                <CCol md={6}>
                    <CFormInput
                        type="text"
                        id="inputName"
                        label="Full Name"
                        name="name"
                        onChange={handleChange}
                    />
                </CCol>
                <CCol md={6}>
                    <CFormInput
                        type="email"
                        id="inputEmail4"
                        label="Email"
                        name="email"
                        onChange={handleChange}
                    />
                </CCol>
                <CCol md={6}>
                    <CFormInput
                        type="password"
                        id="inputPassword4"
                        label="Password"
                        name="password"
                        onChange={handleChange}
                    />
                </CCol>
                <CCol md={6}>
                    <CFormInput
                        type="text"
                        id="inputPhoneNumber"
                        label="Phone Number"
                        name="phone_number"
                        onChange={handleChange}
                    />
                </CCol>
                <CCol xs={12}>
                    <CFormInput
                        id="inputAddress"
                        label="Address"
                        name="address"
                        placeholder="Current Location"
                        onChange={handleChange}
                    />
                </CCol>
                <CCol xs={12}>
                    <CFormTextarea
                        id="inputBio"
                        label="Bio"
                        name="bio"
                        rows={3}
                        placeholder="Tell us about yourself"
                        onChange={handleChange}
                    />
                </CCol>
                <CCol xs={12}>
                    <label>Profile Picture:</label>
                    <input
                        type="file"
                        name="profile_picture"
                        onChange={handleFileChange}
                    />
                </CCol>
                <CCol xs={12}>
                    <CFormCheck
                        type="checkbox"
                        id="invalidCheck"
                        label="Agree to terms and conditions"
                        required
                    />
                    <CFormFeedback invalid>You must agree before submitting.</CFormFeedback>
                </CCol>
                <CCol xs={12}>
                    <CButton color="primary" type="submit">Submit form</CButton>
                </CCol>
            </CForm>
        </div>
    );
};

export default ClientForm;