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