import { useEffect, useState } from "react";
import MainLayout from "../layouts/MainLayout";
import api from "../services/api";

function Transactions() {

  const [transactions, setTransactions] = useState([]);

  useEffect(() => {

    loadTransactions();

  }, []);

  async function loadTransactions() {

    try {

      const response = await api.get("/transactions");

      setTransactions(response.data);

    } catch (error) {

      console.log(error);

    }

  }

  return (

    <MainLayout>

      <div className="d-flex justify-content-between mb-4">

        <h2>Transactions</h2>

        <button className="btn btn-primary">

          Add Transaction

        </button>

      </div>

      <table className="table table-bordered table-hover">

        <thead className="table-dark">

          <tr>

            <th>Date</th>

            <th>Description</th>

            <th>Amount</th>

            <th>Type</th>

            <th>Category</th>

            <th>Source</th>

          </tr>

        </thead>

        <tbody>

          {transactions.map((t) => (

            <tr key={t.id}>

              <td>{t.date}</td>

              <td>{t.description}</td>

              <td>₹ {t.amount}</td>

              <td>{t.transaction_type}</td>

              <td>{t.category}</td>

              <td>{t.source}</td>

            </tr>

          ))}

        </tbody>

      </table>

    </MainLayout>

  );
}

export default Transactions;