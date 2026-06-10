import { Link } from "react-router-dom";
import { FaHome, FaListUl, FaPlusCircle } from "react-icons/fa";
import "./Sidebar.css";

export default function Sidebar() {
  return (
    <div className="sidebar">
      <h2>Expense Tracker</h2>

      <nav>
        <Link to="/">
          <FaHome className="sidebar-icon" /> Dashboard
        </Link>
        <Link to="/transactions">
          <FaListUl className="sidebar-icon" /> Transactions
        </Link>
        <Link to="/transactions/new">
          <FaPlusCircle className="sidebar-icon" /> Add Transaction
        </Link>
      </nav>
    </div>
  );
}