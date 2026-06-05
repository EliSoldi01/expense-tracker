import { useEffect, useState } from "react";
import { api } from "../api/client.ts";
import type { Transaction } from "../types/transaction";

export default function TransactionsTable() {
  const [data, setData] = useState<Transaction[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    console.log("CALLING API...");

    api.get("/transactions")
      .then((res) => {
        console.log("RESPONSE:", res.data); // 👈 IMPORTANTISSIMO

        setData(res.data);
      })
      .catch((err) => {
        console.log("ERROR:", err);
      })
      .finally(() => {
        setLoading(false);
      });

  }, []);

  if (loading) return <p>Loading...</p>;

  return (
    <div>
      <h2>Transactions</h2>

      <table border={1}>
        <thead>
          <tr>
            <th>Type</th>
            <th>Amount</th>
            <th>Category</th>
            <th>Date</th>
          </tr>
        </thead>

        <tbody>
          {data.map((t) => (
            <tr key={t.id}>
              <td>{t.type}</td>
              <td>{t.amount}</td>
              <td>{t.category}</td>
              <td>{t.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}