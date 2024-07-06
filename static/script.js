document.getElementById('extract-tables').addEventListener('click', () => {
    const sql = document.getElementById('sql-input').value;
    fetch('/extract', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ sql })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('tables').innerText = data.tables.join(', ');
        document.getElementById('columns').innerText = data.columns.join(', ');
    });
});

document.getElementById('extract-columns').addEventListener('click', () => {
    const sql = document.getElementById('sql-input').value;
    fetch('/extract', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ sql })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('tables').innerText = data.tables.join(', ');
        document.getElementById('columns').innerText = data.columns.join(', ');
    });
});