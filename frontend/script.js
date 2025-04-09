const API_URL = window.location.origin + "/api/trades";

async function loadTrades() {
    const res = await fetch(API_URL);
    const data = await res.json();
    const list = document.getElementById("trades-list");
    list.innerHTML = "";
    data.forEach(t => {
        const item = document.createElement("li");
        item.innerText = `${t.symbol}: ${t.profit} USD (${t.note})`;
        list.appendChild(item);
    });
}

async function addTrade() {
    const symbol = document.getElementById("symbol").value;
    const profit = parseFloat(document.getElementById("profit").value);
    const note = document.getElementById("note").value;

    const res = await fetch(API_URL, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({symbol, profit, note})
    });

    const newTrade = await res.json();
    alert(`Added trade: ${newTrade.symbol}`);
    loadTrades();
}

document.addEventListener("DOMContentLoaded", loadTrades);
document.getElementById("add-trade-btn").addEventListener("click", addTrade);
