import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://crispy-cod-pjw56rxv49qr29w4j-8000.app.github.dev/api/activity/')
      .then(response => response.json())
      .then(data => setActivities(data));
  }, []);

  return (
    <div>
      <h1>Activities</h1>
      <ul>
        {activities.map(activity => (
          <li key={activity.id}>{activity.activity_type} - {activity.duration} minutes</li>
        ))}
      </ul>
    </div>
  );
};

export default Activities;
