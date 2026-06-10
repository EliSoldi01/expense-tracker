import "./BalanceCard.css";

type Props = {
  balance: number;
  expense: number;
  income: number;
};

export default function BalanceCard({ balance, expense, income }: Props) {
  return (
    <div className="balance-container">
      <div className="card main">
        <h3>Balance</h3>
        <p className="amount">{balance.toFixed(2)} €</p>
      </div>
      <div className="expense-card">
        <h3>Expense</h3>
        <p className="expense">-€ {expense.toFixed(2)}</p>
      </div>

      <div className="income-card">
        <h3>Income</h3>
        <p className="income">+€ {income.toFixed(2)}</p>
      </div>
      
    </div>
  );
}