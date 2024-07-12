
const projectRows = document.querySelectorAll('#userTable tbody tr')
const employeeProjectRows = document.querySelectorAll('#employeeProjectTable tbody tr')

projectRows.forEach((row) => {
    row.addEventListener('click',() => {
        var projectId = row.getAttribute('id');
        window.location.href="projects/" + projectId
    })
})

employeeProjectRows.forEach((row) => {
    row.addEventListener('click',() => {
        var employeeprojectId = row.getAttribute('id');
        window.location.href="projects/" + employeeprojectId
    })
})

document.addEventListener("DOMContentLoaded", function() {
    var table = document.getElementById('userTable');
    var rows = table.getElementsByTagName('tr');
    var rowsPerPage = 11;
    var currentPage = 0;
    function showPage(page) {
        var start = page * rowsPerPage;
        var end = start + rowsPerPage;
        for (var i = 0; i < rows.length; i++) {
            if (i >= start && i < end) {
                rows[i].style.display = '';
            } else {
                rows[i].style.display = 'none';
            }
        }
    }
    function createPagination() {
        var pageCount = Math.ceil(rows.length / rowsPerPage);
        var pagination = document.getElementById('pagination');
        pagination.innerHTML = '';
        for (var i = 0; i < pageCount; i++) {
            var button = document.createElement('button');
            button.innerText = i + 1;
            button.addEventListener('click', function() {
                currentPage = parseInt(this.innerText) - 1;
                showPage(currentPage);
            });
            pagination.appendChild(button);
        }
    }
    function updatePagination() {
        var buttons = document.querySelectorAll('.pagination button');
        buttons.forEach(function(btn) {
            btn.classList.remove('active');
        });
        buttons[currentPage].classList.add('active');
    }
    createPagination();
    showPage(currentPage);
    var prevBtn = document.getElementById('prevBtn');
    var nextBtn = document.getElementById('nextBtn');
    prevBtn.addEventListener('click', function() {
        if (currentPage > 0) {
            currentPage--;
            showPage(currentPage);
            updatePagination();
        }
    });
    nextBtn.addEventListener('click', function() {
        if (currentPage < Math.ceil(rows.length / rowsPerPage) - 1) {
            currentPage++;
            showPage(currentPage);
            updatePagination();
        }
    });
});
