import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch('https://crispy-cod-pjw56rxv49qr29w4j-8000.app.github.dev/api/leaderboard/')
      .then(response => response.json())
      .then(data => setLeaderboard(data));
  }, []);

  return (
    <div>
      <h1>Leaderboard</h1>
      <ul>
        {leaderboard.map(entry => (
          <li key={entry.id}>{entry.team} - {entry.points} points</li>
        ))}
      </ul>
    </div>
  );
};

export default Leaderboard;
