import { Link } from "react-router-dom";
import {
  FaHome,
  FaWallet,
  FaFileUpload,
  FaRobot,
  FaChartPie,
  FaCog,
} from "react-icons/fa";

function Sidebar() {
  return (
    <div
      className="bg-dark text-white p-3"
      style={{ width: "240px", minHeight: "100vh" }}
    >
      <h3 className="text-center mb-4">
        💰 Finance
      </h3>

      <Link className="nav-link text-white mb-3" to="/dashboard">
        <FaHome className="me-2" />
        Dashboard
      </Link>

      <Link className="nav-link text-white mb-3" to="/transactions">
        <FaWallet className="me-2" />
        Transactions
      </Link>

      <Link className="nav-link text-white mb-3" to="#">
        <FaFileUpload className="me-2" />
        Import Statement
      </Link>

      <Link className="nav-link text-white mb-3" to="#">
        <FaRobot className="me-2" />
        Smart Categorization
      </Link>

      <Link className="nav-link text-white mb-3" to="#">
        <FaChartPie className="me-2" />
        Analytics
      </Link>

      <Link className="nav-link text-white" to="#">
        <FaCog className="me-2" />
        Settings
      </Link>
    </div>
  );
}

export default Sidebar;