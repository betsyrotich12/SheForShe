import React, { useEffect, useState } from 'react';
import apiClient from '../api/axios'; // Ensure this points to your Axios setup

function Mentorship() {
    const [mentors, setMentors] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Fetch mentors when the component loads
    useEffect(() => {
        apiClient.get('/api/mentorship/') // Use the correct Django API endpoint
            .then(response => {
                setMentors(response.data); // Assuming Django returns mentor data as JSON
                setLoading(false);
            })
            .catch(err => {
                setError('Failed to fetch mentor data. Please try again later.');
                console.error('Error fetching mentors:', err);
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <p>Loading mentors...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    return (
        <div>
            <h1>Mentorship Program</h1>
            <ul>
                {mentors.map(mentor => (
                    <li key={mentor.id}>
                        <h3>{mentor.user.username}</h3>
                        <p>Expertise: {mentor.expertise}</p>
                        <p>Location: {mentor.location}</p>
                        <p>Bio: {mentor.bio}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Mentorship;
