import React, { useEffect, useState } from "react";

const RunStats = () => {
  const [stats, setStats] = useState({
    totalMiles: 0,
    totalTime: "0:00",
    avgPace: "0:00",
    last6MonthsMiles: 0,
  });

  useEffect(() => {
    fetch("/runs.json")
      .then((res) => res.json())
      .then((runs) => {
        if (runs.length === 0) return;

        const totalMiles = runs.reduce((sum, r) => sum + parseFloat(r.Distance || 0), 0);

        const totalSeconds = runs.reduce((sum, r) => {
          const parts = r.Time.split(":").map(Number);
          const seconds =
            parts.length === 3 ? parts[0] * 3600 + parts[1] * 60 + parts[2] : parts[0] * 60 + parts[1];
          return sum + seconds;
        }, 0);

        const avgPaceSeconds = totalMiles > 0 ? totalSeconds / totalMiles : 0;
        const avgMin = Math.floor(avgPaceSeconds / 60);
        const avgSec = Math.round(avgPaceSeconds % 60)
          .toString()
          .padStart(2, "0");

        const totalHours = Math.floor(totalSeconds / 3600);
        const totalMins = Math.floor((totalSeconds % 3600) / 60);
        const totalSecs = Math.round(totalSeconds % 60)
          .toString()
          .padStart(2, "0");

        const oneMonthAgo = new Date();
        oneMonthAgo.setMonth(oneMonthAgo.getMonth() - 1);
        const last6MonthsMiles = runs.reduce((sum, r) => {
          const date = new Date(r.Date);
          return date >= oneMonthAgo ? sum + parseFloat(r.Distance || 0) : sum;
        }, 0);

        setStats({
          totalMiles: totalMiles.toFixed(1),
          totalTime: `${totalHours}:${totalMins.toString().padStart(2, "0")}:${totalSecs}`,
          avgPace: `${avgMin}:${avgSec}`,
          last6MonthsMiles: last6MonthsMiles.toFixed(1),
        });
      });
  }, []);

  return (
    <div className="stats-container">
      <h2>Overall Stats</h2>
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Total Mileage</h3>
          <p>{stats.totalMiles} miles</p>
        </div>
        <div className="stat-card">
          <h3>Last Month</h3>
          <p>{stats.last6MonthsMiles} miles</p>
        </div>
        <div className="stat-card">
          <h3>Total Time</h3>
          <p>{stats.totalTime}</p>
        </div>
        <div className="stat-card">
          <h3>Average Pace</h3>
          <p>{stats.avgPace} /mile</p>
        </div>
      </div>
    </div>
  );
};

export default RunStats;
