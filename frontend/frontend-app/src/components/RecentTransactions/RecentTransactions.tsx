import { useEffect, useState } from "react";
import { api } from "../../api/client.ts";
import type { Transaction } from "../../types/transaction.ts";
import "./RecentTransactions.css"
import { Link } from "react-router-dom";

export default function RecentTransactions() {
  const [transactions, setTransactions] = useState<Transaction[]>([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    setError(null);

      api.get("/transactions/last/5")
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

    <div className="transactions-list">
        <div className="rt-header">
            <h3>Recent Transactions</h3>
            <Link to="/transactions" className="view-all">
            View all
            </Link>
            
        </div>
        {transactions.map((t) => (
            <div className="transaction-card" key={t.id}>
            
            {/* LEFT SIDE */}
            <div className="transaction-left">
                <span className="icon">
                {t.type === "income" ? "🟢" : "🔴"}
                </span>

                <div className="info">
                <div className="category">{t.category}</div>
                <div className="type">
                    {t.type === "income" ? "Income" : "Expense"}
                </div>
                </div>
            </div>

            {/* RIGHT SIDE */}
            <div className="transaction-right">
                <div className={t.type === "income" ? "amount income" : "amount expense"}>
                {t.type === "income" ? "+€" : "-€"}
                {Number(t.amount).toFixed(2)}
                </div>

                <div className="date">
                {t.date ? new Date(t.date).toLocaleDateString("it-IT") : "-"}
                </div>
            </div>

        </div>
    ))}
    </div>
)}