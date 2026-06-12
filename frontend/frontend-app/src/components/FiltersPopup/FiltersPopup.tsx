import "./FiltersPopup.css";
import { IoIosSearch } from "react-icons/io";

const categories = [
  "Rent", "Utilities", "Groceries", "Healthcare",
  "Transportation", "Travel/Experience", "Entertainment",
  "Food", "Subscription", "Gifts", "Shopping",
  "Other expense", "Salary", "Pocket money",
  "Gift", "Other income"
];

type Props = {
  filters: {
    type: string;
    category: string;
  };
  setFilters: React.Dispatch<React.SetStateAction<any>>;
};

export default function FiltersPopup({ filters, setFilters }: Props) {

  const handleChange = (
    e: React.ChangeEvent<HTMLSelectElement>
  ) => {
    const { name, value } = e.target;

    setFilters((prev: any) => ({
      ...prev,
      [name]: value
    }));
  };

  return (
    <div className="popup-container">
      <div className="search-field">
        <IoIosSearch />
        <input type="text" placeholder="Search..">
        
        </input>
      </div>
      
      {/* TYPE */}
      <div className="select">
        <label>Type</label>
        <select
          name="type"
          value={filters.type}
          onChange={handleChange}
        >
          <option value="">All</option>
          <option value="income">Income</option>
          <option value="expense">Expense</option>
        </select>
      </div>

      {/* CATEGORY */}
      <div className="select">
        <label>Category</label>
        <select 
          name="category"
          value={filters.category}
          onChange={handleChange}
        >
          <option value="">All</option>
          {categories.map((cat) => (
            <option key={cat} value={cat}>
              {cat}
            </option>
          ))}
        </select>
      </div>

    </div>
  );
}