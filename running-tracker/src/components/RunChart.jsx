import React, { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement, Title, Tooltip, Legend);

const RunChart = () => {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    fetch("/runs.json")
      .then((res) => res.json())
      .then((data) => {
        const labels = data.map((row) => row.Date);
        const miles = data.map((row) => parseFloat(row.Distance));
        setChartData({
          labels,
          datasets: [
            {
              label: "Miles Run",
              data: miles,
              borderColor: "#3e95cd",
              fill: false,
              tension: 0.3,
            },
          ],
        });
      });
  }, []);

  if (!chartData) return <p>Loading chart...</p>;

  return (
    <div className="chart-container">
      <h2>Run Distance Over Time</h2>
      <Line data={chartData} />
    </div>
  );
};

export default RunChart;
