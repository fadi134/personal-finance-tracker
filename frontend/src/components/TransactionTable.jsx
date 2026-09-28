function TransactionTable({ transactions }) {
  return (
    <table className="table table-striped table-hover shadow">
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
        {transactions.length === 0 ? (
          <tr>
            <td colSpan="6" className="text-center">
              No Transactions Found
            </td>
          </tr>
        ) : (
          transactions.map((t) => (
            <tr key={t.id}>
              <td>{t.date}</td>
              <td>{t.description}</td>
              <td>₹ {t.amount}</td>
              <td>{t.transaction_type}</td>
              <td>{t.category}</td>
              <td>{t.source}</td>
            </tr>
          ))
        )}
      </tbody>
    </table>
  );
}

export default TransactionTable;