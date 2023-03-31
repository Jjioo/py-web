const stockForm = document.getElementById('stock-form');
const stockTable = document.getElementById('stock-table').getElementsByTagName('tbody')[0];

const iexCloudApiKey = 'pk_05bfc04bdd7f4bcabb59c4cd87777aaa'; // Replace with your own API key

stockForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const stockSymbol = document.getElementsByName('stock_name')[0].value.toUpperCase();
    const url = `https://cloud.iexapis.com/stable/stock/${stockSymbol}/chart/1m?token=${iexCloudApiKey}`;
    fetch(url)
    .then(response => response.json())
    .then(data => {
        stockTable.innerHTML = '';
        const closingPrices = data?.map(price => [price.date, price.close]) || [];
        if (closingPrices.length === 0) {
            const row = stockTable.insertRow();
            const cell = row.insertCell();
            cell.innerHTML = 'No data available';
        } else {
            closingPrices.forEach((price) => {
                const row = stockTable.insertRow();
                const dateCell = row.insertCell(0);
                const priceCell = row.insertCell(1);
                dateCell.innerHTML = price[0];
                priceCell.innerHTML = price[1];
            });
        }
    })
    .catch(error => console.error(error));
});

