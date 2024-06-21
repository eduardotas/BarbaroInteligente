document.addEventListener('DOMContentLoaded', function () {
    const tableBody = document.getElementById('table-body');

    tableBody.addEventListener('click', function (e) {
        if (e.target.classList.contains('btn-up')) {
            const row = e.target.closest('tr');
            const previousRow = row.previousElementSibling;
            if (previousRow) {
                tableBody.insertBefore(row, previousRow);
            }
        }

        if (e.target.classList.contains('btn-down')) {
            const row = e.target.closest('tr');
            const nextRow = row.nextElementSibling;
            if (nextRow) {
                tableBody.insertBefore(nextRow, row);
            }
        }
    });
});