import { hideElement, toggleOverlay, replaceElement} from './function.js'; 




// document.getElementById('edit-about-id')
//     .addEventListener("click", function(event) {
//         hideElement('about-detail-id', 'flex')
//         console.log("ok")
//     })

// document.getElementById('popup-edit-cover-id')
//     .addEventListener("click", function(event) {
//         toggleOverlay('base-popup-id','flex')
//     })

// document.getElementById('base-popup-close-id')
//     .addEventListener("click", function(event) {
//     toggleOverlay('base-popup-id','flex')
//     console.log("ok")
// })

// document.getElementById('add-cover-photo-id')
//     .addEventListener("click", function(event) {
//         replaceElement('base-popup-id','flex', 'select-popup-id', 'flex')
// })

// document.getElementById('select-popup-close-id')
//     .addEventListener("click", function(event) {
//         toggleOverlay('select-popup-id','flex')
// })

// document.getElementById('add-profile-photo-id')
//     .addEventListener("click", function(event) {
//         toggleOverlay('profile-popup-add-id', 'flex')
// })

// document.getElementById('add-profile-button-id')
//     .addEventListener("click", function(event) {
//         toggleOverlay('profile-add-photo-popup-id','flex')
// })

// document.getElementById('select-profile-popup-close-id')
//     .addEventListener("click", function(event) {
//         toggleOverlay('profile-add-photo-popup-id','flex')
// })


// function closeOverlays(event, overlayId) {
//     const overlay = document.getElementById(overlayId);
//     if (overlay && !event.target.closest(`#${overlayId}`) && !event.target.closest('#profile-settings-id')) {
//         overlay.classList.add('hidden'); // Or set display: 'none';
//     }
// }

// // Event listeners for button actions
// document.getElementById('edit-about-id').addEventListener("click", function(event) {
//     hideElement('about-detail-id', 'flex');
//     console.log("About section toggled");
// });

// document.getElementById('popup-edit-cover-id').addEventListener("click", function(event) {
//     toggleOverlay('base-popup-id', 'flex');
// });

// document.getElementById('base-popup-close-id').addEventListener("click", function(event) {
//     toggleOverlay('base-popup-id', 'flex');
//     console.log("Base popup closed");
// });

// document.getElementById('add-cover-photo-id').addEventListener("click", function(event) {
//     replaceElement('base-popup-id', 'flex', 'select-popup-id', 'flex');
// });

// document.getElementById('select-popup-close-id').addEventListener("click", function(event) {
//     toggleOverlay('select-popup-id', 'flex');
// });

// document.getElementById('add-profile-photo-id').addEventListener("click", function(event) {
//     toggleOverlay('profile-popup-add-id', 'flex');
// });

// document.getElementById('add-profile-button-id').addEventListener("click", function(event) {
//     toggleOverlay('profile-add-photo-popup-id', 'flex');
// });

// document.getElementById('select-profile-popup-close-id').addEventListener("click", function(event) {
//     toggleOverlay('profile-add-photo-popup-id', 'flex');
// });

// // Attach event listener to window for clicking outside overlays
// window.addEventListener("click", function(event) {
//     closeOverlays(event, 'base-popup-id');
//     closeOverlays(event, 'select-popup-id');
//     closeOverlays(event, 'profile-popup-add-id');
//     closeOverlays(event, 'profile-add-photo-popup-id');
// });

// // Close the dropdown when an item is clicked
// const dropdownItems = document.querySelectorAll('#myDropdown a');
// dropdownItems.forEach(item => {
//     item.addEventListener("click", function() {
//         const dropdown = document.getElementById("myDropdown");
//         dropdown.classList.add('hidden');
//         console.log("Dropdown item clicked: ", this.innerText);
//     });
// });
