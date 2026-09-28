import MainLayout from "../layouts/MainLayout";

function Dashboard() {
  return (
    <MainLayout>

      <h2 className="mb-4">Dashboard</h2>

      <div className="row">

        <div className="col-md-3">
          <div className="card shadow p-3">
            <h5>Total Income</h5>
            <h2>₹0</h2>
          </div>
        </div>

        <div className="col-md-3">
          <div className="card shadow p-3">
            <h5>Total Expense</h5>
            <h2>₹0</h2>
          </div>
        </div>

        <div className="col-md-3">
          <div className="card shadow p-3">
            <h5>Balance</h5>
            <h2>₹0</h2>
          </div>
        </div>

        <div className="col-md-3">
          <div className="card shadow p-3">
            <h5>Transactions</h5>
            <h2>0</h2>
          </div>
        </div>

      </div>

    </MainLayout>
  );
}

export default Dashboard;