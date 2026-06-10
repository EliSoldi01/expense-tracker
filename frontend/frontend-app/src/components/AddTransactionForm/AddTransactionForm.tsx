import "./AddTransactionForm.css";
import { useState } from "react";

const expense_categories = [
  "Rent",
  "Utilities",
  "Groceries",
  "Healthcare",
  "Transportation",
  "Travel/Experience",
  "Entertainment",
  "Food",
  "Subscription",
  "Gifts",
  "Shopping",
  "Other expense"
];

const income_categories = [
  "Salary",
  "Pocket money",
  "Gift",
  "Other income"
];

export default function AddTransactionForm() {
  const [form, setForm] = useState({
    type: "",
    amount: "",
    category: "",
    date: "",
    description: "",
  });
  const [showSubmitButton, setShowSubmitButton] = useState(false)

  const categories =
    form.type === "income"
      ? income_categories
      : expense_categories;

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;

    setForm((prev) => {
      const updated = {
        ...prev,
        [name]: value,
      };

      if (name === "type") {
        updated.category = "";
      }

      return updated;
    });
  };

  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();

    setForm({
      type: "",
      amount: "",
      category: "",
      date: "",
      description: "",
    });
    setShowSubmitButton(true)

    setTimeout(() => {setShowSubmitButton(false)}, 5000)
  }

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-group">

        <label>Type</label>
        <select
          name="type"
          value={form.type}
          onChange={handleChange}
          required
        >
          <option value="">Select type</option>
          <option value="income">Income</option>
          <option value="expense">Expense</option>
        </select>

        <label>Date</label>
        <input
          name="date"
          type="date"
          value={form.date}
          onChange={handleChange}
          required
        />

        <label>Amount</label>
        <input
          type="number"
          name="amount"
          step="0.01"
          min="0"
          placeholder="€ 0.00"
          value={form.amount}
          onChange={handleChange}
          required
        />

        <label>Category</label>
        <select
          name="category"
          value={form.category}
          onChange={handleChange}
          required
        >
          <option value="">Select category</option>

          {categories.map((cat) => (
            <option key={cat} value={cat}>
              {cat}
            </option>
          ))}
        </select>

        <label>Description</label>
        <input
          name="description"
          value={form.description}
          onChange={handleChange}
        />

        {!showSubmitButton && (
          <button type="submit" disabled={!form.type || !form.amount || !form.category || !form.date}>
                Add transaction 
          </button>
        )}

        {showSubmitButton && <p className="submitted-text">Transaction added</p>}

      </div>
    </form>
  );
}