document.addEventListener('DOMContentLoaded', () => {
    let deleteButtons = document.querySelectorAll('.delete-btn');

    deleteButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            let confirmDelete = confirm("Are you sure you want to delete this book?");
            if (!confirmDelete) {
                event.preventDefault();
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', () => {
    let deleteButtons = document.querySelectorAll('.delete-btn');

    deleteButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            let confirmDelete = confirm("Are you sure you want to delete this book?");
            if (!confirmDelete) {
                event.preventDefault();
            }
        });
    });

    let bookForm = document.querySelector("#book-form");
    if (bookForm) {
        bookForm.addEventListener("submit", function(event) {
            let title = document.querySelector("#id_title").value.trim();
            let author = document.querySelector("#id_author").value.trim();
            if (title === "" || author === "") {
                alert("Title and author fields cannot be empty.");
                event.preventDefault();
            }
        });
    }
});