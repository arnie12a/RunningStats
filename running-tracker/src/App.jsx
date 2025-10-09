import React from "react";
import "./App.css";
import RunChart from "./components/RunChart";
import RunTable from "./components/RunTable";
import RunStats from "./components/RunStats";

function App() {
  return (
    <div className="app">
      <header>
        <h1>My Run Tracker</h1>
      </header>
      <main>
        <RunStats />
        <RunChart />
        <RunTable />
      </main>
    </div>
  );
}

export default App;
