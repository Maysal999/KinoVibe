
// Optional JavaScript for dropdown (for click behavior)
const dropdownBtn = document.querySelector('.dropdown-btn');
const dropdownContent = document.querySelector('.dropdown-content');

dropdownBtn.addEventListener('click', function () {
    dropdownContent.classList.toggle('show');
});

window.onclick = function (event) {
    if (!event.target.matches('.dropdown-btn')) {
        if (dropdownContent.classList.contains('show')) {
            dropdownContent.classList.remove('show');
        }
    }
};