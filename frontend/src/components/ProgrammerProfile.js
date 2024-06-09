import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const ProgrammerProfile = () => {
    const { id } = useParams(); // Retrieve programmer ID from URL params
    const [programmerData, setProgrammerData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [editing, setEditing] = useState(false);
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        phone_number: '',
        address: '',
        experience: '',
        sector: '',
        skills: '',
        bio: ''
    });

    useEffect(() => {
        const fetchProgrammerData = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/programmer/${id}/`);
                setProgrammerData(response.data);
                setFormData(response.data); // Set form data with existing programmer data
                setLoading(false);
            } catch (error) {
                setError(error);
                setLoading(false);
            }
        };

        fetchProgrammerData();
    }, [id]);

    const handleDelete = async () => {
        const confirmDelete = window.confirm('Are you sure you want to delete your profile?');
        if (confirmDelete) {
            try {
                await axios.delete(`http://127.0.0.1:8000/programmer/${id}/`);
                // Redirect or show a success message after deletion
            } catch (error) {
                setError(error);
            }
        }
    };

    const handleEdit = () => {
        setEditing(true);
    };

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.put(`http://127.0.0.1:8000/programmer/${id}/`, formData);
            setEditing(false);
            // Show success message or redirect to profile page
        } catch (error) {
            setError(error);
        }
    };

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading programmer data: {error.message}</p>;

    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <h1>Programmer Profile</h1>
            {editing ? (
                <form onSubmit={handleSubmit}>
                    <label>Full Name:</label>
                    <input type="text" name="name" value={formData.name} onChange={handleChange} /> <br/><br/>
                    <label>Email:</label>
                    <input type='email' name='email' value={formData.email} onChange={handleChange} />  <br/><br/>
                    <label>Password:</label>
                    <input type='password' name='password' value={formData.password} onChange={handleChange} />  <br/><br/>
                    <label>Phone Number:</label>
                    <input type='text' name='phone_number' value={formData.phone_number} onChange={handleChange} />  <br/><br/>
                    <label>Address:</label>
                    <input type='text' name='address' value={formData.address} onChange={handleChange} />  <br/><br/>
                    <label>Experience:</label>
                    <input type='number' name='experience' value={formData.experience} onChange={handleChange} />  <br/><br/>
                    <label>Category:</label>
                    <input type='categories' name='categories' value={formData.categories} onChange={handleChange} />  <br/><br/>
                    <label>Sector:</label>
                    <input type='sector' name='sector' value={formData.sector} onChange={handleChange} />  <br/><br/>
                    <label>Skills:</label>
                    <input type='skills' name='skills' value={formData.skills} onChange={handleChange} />  <br/><br/>
                    <label>Bio:</label>
                    <input type='textarea' name='bio' value={formData.bio} onChange={handleChange} />  <br/><br/>
                    <button type="submit">Update</button>
                </form>
            ) : (
                <div>
                    {programmerData && (
                        <div>
                            {programmerData.profile_picture && (
                                <img
                                    src={programmerData.profile_picture}
                                    alt="Profile"
                                    style={{ width: '150px', height: '150px', borderRadius: '50%' }}
                                />
                            )}
                            <p><strong>Name:</strong> {programmerData.name}</p>
                            <p><strong>Email:</strong> {programmerData.email}</p>
                            <p><strong>Phone Number:</strong> {programmerData.phone_number}</p>
                            <p><strong>Address:</strong> {programmerData.address}</p>
                            <p><strong>Experience:</strong> {programmerData.experience} years</p>
                            <p><strong>Category:</strong> {programmerData.categories ? programmerData.categories.name : 'N/A'}</p>
                            <p><strong>Sector:</strong> {programmerData.sector}</p>
                            <p><strong>Skills:</strong> {programmerData.skills}</p>
                            <p><strong>Bio:</strong> {programmerData.bio}</p>
                            <button onClick={handleEdit}>Edit Profile</button> <br/> <br/>
                            <button onClick={handleDelete}>Delete Profile</button>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default ProgrammerProfile;