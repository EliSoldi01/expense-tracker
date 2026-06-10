import { useEffect, useState } from "react";
import { api } from "../api/client";
import BalanceCard from "../components/BalanceCard/BalanceCard";
import RecentTransactions from "../components/RecentTransactions/RecentTransactions";

export default function Dashboard() {
  const [balance, setBalance] = useState({
    balance: 0,
    expense: 0,
    income: 0,
  });

  useEffect(() => {
    api.get("/reports/balance").then((res) => {
      setBalance(res.data);
    });
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>

      <BalanceCard
        balance={balance.balance}
        expense={balance.expense}
        income={balance.income}
      />

      {/* RECENT TRANSACTIONS */}
      <RecentTransactions />
    </div>
  );
}