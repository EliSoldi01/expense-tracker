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
  { value: "Rent", label: "Rent", type: "expense" },
  { value: "Utilities", label: "Utilities", type: "expense" },
  { value: "Groceries", label: "Groceries", type: "expense" },
  { value: "Healthcare", label: "Healthcare", type: "expense" },
  { value: "Transportation", label: "Transportation", type: "expense" },
  { value: "Travel", label: "Travel/Experience", type: "expense" },
  { value: "Entertainment", label: "Entertainment", type: "expense" },
  { value: "Food", label: "Food", type: "expense" },
  { value: "Subscription", label: "Subscription", type: "expense" },
  { value: "Gifts", label: "Gifts", type: "expense" },
  { value: "Shopping_exp", label: "Shopping", type: "expense" },
  { value: "Other_expense", label: "Other expense", type: "expense" },

  { value: "Salary", label: "Salary", type: "income" },
  { value: "Pocket_money", label: "Pocket money", type: "income" },
  { value: "Gift_income", label: "Gift", type: "income" },
  { value: "Other_income", label: "Other income", type: "income" },
  { value: "Shopping_inc", label: "Shopping", type: "income" }
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

    </div>
  );
}