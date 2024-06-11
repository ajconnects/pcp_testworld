import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { CFormInput, CForm, CCol, CButton, CFormCheck, CFormFeedback, CFormSelect, CFormTextarea } from '@coreui/react';

const ProgrammerForm = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: '',
        phone_number: '',
        address: '',
        experience: '',
        category_id: '',
        sector: 'AI/MachineLearning',
        skills: '',
        bio: '',
        profile_picture: null,
    });

    const [categories, setCategories] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchCategories = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/categories/');
                setCategories(response.data);
                setIsLoading(false);
            } catch (error) {
                console.error('Error fetching categories:', error);
                setIsLoading(false);
            }
        };

        fetchCategories();
    }, []);

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
            const response = await axios.post('http://127.0.0.1:8000/programmer/', form, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            console.log(response.data);
            navigate(`/programmer-profile/${response.data.id}`); // Redirect to programmer profile page
        } catch (error) {
            console.error('Error submitting form:', error);
            if (error.response) {
                setError(error.response.data);
            }
        }
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <h1>Programmer Registration Form:</h1>
            <br/>
            {isLoading ? (
                <p>Loading categories...</p>
            ) : (
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
                    <CCol md={6}>
                        <CFormInput
                            type="number"
                            id="inputExperience"
                            label="Experience (years)"
                            name="experience"
                            onChange={handleChange}
                        />
                    </CCol>
                    <CCol md={6}>
                        <CFormSelect
                            id="inputCategories"
                            label="Categories"
                            name="category_id"
                            onChange={handleChange}
                        >
                            <option value="">Select Category</option>
                            {categories.map((category) => (
                                <option key={category.id} value={category.id}>
                                    {category.name}
                                </option>
                            ))}
                        </CFormSelect>
                    </CCol>
                    <CCol md={12}>
                        <CFormSelect
                            id="inputSector"
                            label="Sector"
                            name="sector"
                            onChange={handleChange}
                        >
                            <option value="WebDeveloper">WebDeveloper</option>
                            <option value="BackendDeveloper">BackendDeveloper</option>
                            <option value="Networking">Networking</option>
                            <option value="AI/MachineLearning">AI/Machine Learning</option>
                            <option value="CloudServices">Cloud Services</option>
                            <option value="Admin/CustomerSupport">Administration/Customer Support</option>
                        </CFormSelect>
                    </CCol>
                    <CCol xs={12}>
                        <CFormInput
                            id="inputSkills"
                            label="Skills"
                            name="skills"
                            placeholder="List your skills"
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
            )}
            {error && <p style={{ color: 'red' }}>Error: {JSON.stringify(error)}</p>}
        </div>
    );
};

export default ProgrammerForm;