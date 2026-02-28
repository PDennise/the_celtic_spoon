// Select the user button and dropdown menu
const userBtn = document.querySelector('.user-btn');
const dropdown = document.querySelector('.dropdown');

// Toggle dropdown visibility when clicking the user button
userBtn.addEventListener('click', (e) => {
  e.preventDefault();
  dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
});

// Close dropdown if clicked outside of user-menu
window.addEventListener('click', (e) => {
  if (!e.target.closest('.user-menu')) {
    dropdown.style.display = 'none';
  }
});