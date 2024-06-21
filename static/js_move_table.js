// CONTROLE ORDEM ITENS
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
// FIM CONTROLE ORDEM ITENS

// BARRA DE VIDA
function updateProgressText(progressBar, value) {
    progressBar.parentElement.querySelector('.progress-text').textContent = value;
}

function updateProgressColor(progressBar, value) {
    if (value > 50) {
        progressBar.classList.remove('yellow', 'red');
        progressBar.classList.add('green');
    } else if (value >= 25) {
        progressBar.classList.remove('green', 'red');
        progressBar.classList.add('yellow');
    } else {
        progressBar.classList.remove('green', 'yellow');
        progressBar.classList.add('red');
    }
}

function changeHealth(button, amount) {
    var progressContainer = button.closest('tr').querySelector('.progress-container');
    var progressBar = progressContainer.querySelector('progress');
    var currentValue = parseInt(progressBar.value);
    var newValue = currentValue + amount;
    newValue = Math.max(0, Math.min(newValue, progressBar.max)); // Limita entre 0 e max

    progressBar.value = newValue;
    updateProgressText(progressBar, newValue);
    updateProgressColor(progressBar, newValue);
}

// Inicializa o texto das barras de progresso
document.querySelectorAll('.progress-container').forEach(function(container) {
    var progressBar = container.querySelector('progress');
    updateProgressText(progressBar, progressBar.value);
    updateProgressColor(progressBar, progressBar.value);
});
// FIM BARRA DE VIDA