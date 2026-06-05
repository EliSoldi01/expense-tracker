export type TransactionType = "income" | "expense";

export interface Transaction {
  id: number;
  type: "income" | "expense";
  amount: number;
  date: string;
  category: string;
  description?: string;
}