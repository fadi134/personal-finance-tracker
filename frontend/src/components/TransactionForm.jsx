import { useState } from "react";

function TransactionForm({ onSave }) {
  const [form, setForm] = useState({
    date: "",
    description: "",
    amount: "",
    transaction_type: "Expense",
    category: "",
    source: "Manual",
  });

  function handleChange(e) {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  }

  function submit(e) {
    e.preventDefault();
    onSave(form);

    setForm({
      date: "",
      description: "",
      amount: "",
      transaction_type: "Expense",
      category: "",
      source: "Manual",
    });
  }

  return (
    <form onSubmit={submit} className="card shadow p-3 mb-4">

      <div className="row">

        <div className="col-md-2">
          <input
            type="date"
            className="form-control"
            name="date"
            value={form.date}
            onChange={handleChange}
            required
          />
        </div>

        <div className="col-md-3">
          <input
            className="form-control"
            placeholder="Description"
            name="description"
            value={form.description}
            onChange={handleChange}
            required
          />
        </div>

        <div className="col-md-2">
          <input
            type="number"
            className="form-control"
            placeholder="Amount"
            name="amount"
            value={form.amount}
            onChange={handleChange}
            required
          />
        </div>

        <div className="col-md-2">
          <select
            className="form-control"
            name="transaction_type"
            value={form.transaction_type}
            onChange={handleChange}
          >
            <option>Expense</option>
            <option>Income</option>
          </select>
        </div>

        <div className="col-md-2">
          <input
            className="form-control"
            placeholder="Category"
            name="category"
            value={form.category}
            onChange={handleChange}
            required
          />
        </div>

        <div className="col-md-1">
          <button className="btn btn-success w-100">
            Add
          </button>
        </div>

      </div>

    </form>
  );
}

export default TransactionForm;