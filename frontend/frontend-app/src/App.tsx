import { Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Transactions from "./pages/Transactions";
import AddTransaction from "./pages/AddTransaction";
import Sidebar from "./components/Sidebar/Sidebar";
import "./App.css"

export default function App() {
  return (
    <div style={{ marginLeft: "50px" }}>
      <div className="app-layout">
      <Sidebar />

      <main className="main-content">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/transactions" element={<Transactions />} />
          <Route path="/transactions/new" element={<AddTransaction />} />
        </Routes>
      </main>
    </div>
  </div>
  );
}