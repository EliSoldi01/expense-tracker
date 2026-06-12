import { useEffect, useState } from "react";
import { api } from "../../api/client.ts";
import type { Transaction } from "../../types/transaction.ts";
import { IoFilterOutline } from "react-icons/io5";
import FiltersPopup from "../FiltersPopup/FiltersPopup.tsx";

export default function TransactionsTable() {
  const [transactions, setTransactions] = useState<Transaction[]>([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showFilters, setShowFilters] = useState(false);
  const [filters, setFilters] = useState({
  type: "",
  category: ""
});

  useEffect(() => {
    setLoading(true);
    setError(null);

    api.get("/transactions")
    .then(res => {setTransactions(res.data)})
    .catch((err) => {
      console.log(err);
      setError("❌ Errore nel caricamento dei dati");
    })
    .finally(() => {
      setLoading(false);
    });

  }, []);

  if (loading) return <p>Loading...</p>;

  if (error) {
    return <p style={{ color: "red" }}>{error}</p>;
  }

  return (
      
      <div className="transactions-page">

      <div className="header">
        <button
          onClick={() => setShowFilters(!showFilters)}
          className={`filters_button ${showFilters ? "active" : ""}`}
        >
          <IoFilterOutline />
          Filters
        </button>

        {showFilters && (
          <FiltersPopup
            filters={filters}
            setFilters={setFilters}
          />
        )}
      </div>
      
      <div className="table-container">

        <table>
          <thead>
            <tr>
              <th>Type</th>
              <th>Amount</th>
              <th>Category</th>
              <th>Date</th>
            </tr>
          </thead>

          <tbody>
            {transactions.map((t) => (
              <tr key={t.id}>
                <td className="text-format">
                  {t.type === "income" ? "🟢 Income" : "🔴 Expense"}
                </td>

                <td className="text-format">
                  {t.type === "income" ? "+€" : "-€"}
                  {Number(t.amount).toFixed(2)}
                </td>

                <td className="text-format">{t.category}</td>

                <td className="text-format">
                  {t.date
                    ? new Date(t.date).toLocaleDateString("it-IT")
                    : "-"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      </div>
  );
}
