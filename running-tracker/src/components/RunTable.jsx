import React, { useEffect, useState } from "react";
import Papa from "papaparse";

const RunTable = () => {
  const [runs, setRuns] = useState([]);

  useEffect(() => {
    Papa.parse("/runs.csv", {
      download: true,
      header: true,
      complete: (result) => {
        setRuns(result.data);
      },
    });
  }, []);

  return (
    <div className="table-container">
      <h2>Run Log</h2>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Miles</th>
            <th>Total Time</th>
            <th>Average Pace</th>
          </tr>
        </thead>
        <tbody>
          {runs.map((run, index) => (
            <tr key={index}>
              <td>{run.Date}</td>
              <td>{run.Distance}</td>
              <td>{run.Time}</td>
              <td>{run.AveragePace}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default RunTable;
