// URL of the backend API
const API_URL = "http://127.0.0.1:5000/api/transactions";

// Function to fetch transaction data from the backend
async function fetchTransactions() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error("Failed to fetch transactions");
        }
        const transactions = await response.json();
        populateTable(transactions);
    } catch (error) {
        console.error("Error fetching transactions:", error);
    }
}

// Function to populate the table with transaction data
function populateTable(transactions) {
    const tableBody = document.getElementById("transaction-table");
    tableBody.innerHTML = ""; // Clear existing rows

    transactions.forEach(transaction => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${transaction.date}</td>
            <td>${transaction.time}</td>
            <td>${transaction.amount}</td>
            <td>${transaction.utr_number}</td>
            <td>${transaction.upi_id}</td>
        `;

        tableBody.appendChild(row);
    });
}

// Fetch transactions when the page loads
document.addEventListener("DOMContentLoaded", fetchTransactions);
