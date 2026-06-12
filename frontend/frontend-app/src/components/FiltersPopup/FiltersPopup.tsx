import Select from "react-select";
import "./FiltersPopup.css";

type Filters = {
  type: string;
  category: string;
};

type Props = {
  filters: Filters
  setFilters: React.Dispatch<React.SetStateAction<Filters>>;
};

const types = [
  { value: "income", label: "Income" },
  { value: "expense", label: "Expense" },
];

const categories = [
  { value: "rent", label: "Rent", type: "expense" },
  { value: "utilities", label: "Utilities", type: "expense" },
  { value: "groceries", label: "Groceries", type: "expense" },
  { value: "healthcare", label: "Healthcare", type: "expense" },
  { value: "transportation", label: "Transportation", type: "expense" },
  { value: "travel", label: "Travel/Experience", type: "expense" },
  { value: "entertainment", label: "Entertainment", type: "expense" },
  { value: "food", label: "Food", type: "expense" },
  { value: "subscription", label: "Subscription", type: "expense" },
  { value: "gifts", label: "Gifts", type: "expense" },
  { value: "shopping_exp", label: "Shopping", type: "expense" },
  { value: "other_expense", label: "Other expense", type: "expense" },

  { value: "salary", label: "Salary", type: "income" },
  { value: "pocket_money", label: "Pocket money", type: "income" },
  { value: "gift_income", label: "Gift", type: "income" },
  { value: "other_income", label: "Other income", type: "income" },
  { value: "shopping_inc", label: "Shopping", type: "income" }
];

export default function FiltersPopup({ filters, setFilters }: Props) {
  const filteredCategories =
    filters.type === ""
      ? categories
      : categories.filter(c => c.type === filters.type);

  return (
    <div className="filters">

      {/* TYPE */}
      <div className="select">
      <Select
        options={types}
        placeholder="Type"
        value={types.find(t => t.value === filters.type) || null}
        onChange={(selected) =>
          setFilters(prev => ({
            ...prev,
            type: selected?.value ?? "",
            category: ""
          }))
        }
      />
      </div>

      {/* CATEGORY */}
      <div className="select">
        <Select
          options={filteredCategories}
          placeholder="Category"
          value={filteredCategories.find(c => c.value === filters.category) || null}
          onChange={(selected) =>
            setFilters(prev => ({
              ...prev,
              category: selected?.value ?? ""
            }))
          }
        />
      </div>

      <button
        className="clear-button"
        onClick={() =>
          setFilters({
            type: "",
            category: ""
          })
        }>
        Clear All
      </button>

      <button
        className="apply-button">
        Apply
      </button>

    </div>
  );
}