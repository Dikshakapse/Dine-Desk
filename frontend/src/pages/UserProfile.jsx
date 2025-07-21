import React, { useEffect, useState } from 'react';
import axios from 'axios';

function UserProfile() {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    axios.get('/api/user-profile')
      .then(response => setProfile(response.data))
      .catch(error => console.error('Error fetching user profile:', error));
  }, []);

  if (!profile) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <h1>User Profile</h1>
      <p><strong>Address:</strong> {profile.address}</p>
      <p><strong>Phone Number:</strong> {profile.phone_number}</p>
      <h2>Purchase History</h2>
      <ul>
        {profile.purchase_history.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default UserProfile;
