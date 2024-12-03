import { toggleVisibility } from './function.js';

document.addEventListener("DOMContentLoaded", function() {
    const profileCoverPopup = document.getElementById('base-popup-id');
    const overlay = document.getElementById('overlay');
    const formAddCoverPhoto = document.getElementById('select-popup-id');

    // Function to handle clicking outside to close popups
    function closePopup(event, popup) {
        if (!popup.classList.contains('hidden') && 
            !event.target.closest('#base-popup-id') && 
            !event.target.closest('#popup-edit-cover-id') &&
            !event.target.closest('#select-popup-id')) {
            toggleVisibility(popup);
            toggleVisibility(overlay);
        }
    }

    // Open add cover img popup    
    var popEditBtn = document.getElementById('popup-edit-cover-id')
    if (popEditBtn) {
        popEditBtn.addEventListener("click", function() {
            toggleVisibility(profileCoverPopup);
            toggleVisibility(overlay);
        });
    }

    // Close add cover img popup when X is clicked
    document.getElementById('base-popup-close-id').addEventListener("click", function() {
        toggleVisibility(profileCoverPopup);
        toggleVisibility(overlay);
    });

    // Close when user clicks outside of the profile cover popup
    window.addEventListener("click", function(event) {
        closePopup(event, profileCoverPopup);
        closePopup(event, formAddCoverPhoto);
    });

    // Directs to the add cover photo form
    document.getElementById('add-cover-photo-id').addEventListener("click", function(event) {
        toggleVisibility(profileCoverPopup);
        toggleVisibility(formAddCoverPhoto);
    });

    // Close cover form when X is clicked
    document.getElementById('select-popup-close-id').addEventListener("click", function(event) {
        toggleVisibility(formAddCoverPhoto);
        toggleVisibility(overlay);
    });
});


// document.addEventListener("DOMContentLoaded", function() {
//     // Function to close specific popups and overlays
//     function closePopup(popupId) {
//         console.log(`Closing popup: ${popupId}`);
//         toggleOverlay(popupId, 'none');
//         toggleOverlay('overlay', 'none'); // Close the overlay as well
//     }

//     // Open the edit cover popup and overlay
//     document.getElementById('popup-edit-cover-id').addEventListener("click", function() {
//         console.log("Opening base popup");
//         toggleOverlay('base-popup-id', 'flex');
//         toggleOverlay('overlay', 'flex');
//     });

//     // Close the base popup when the close button is clicked
//     document.getElementById('base-popup-close-id').addEventListener("click", function() {
//         closePopup('base-popup-id');
//     });

//     // Close the select popup when the close button is clicked
//     document.getElementById('select-popup-close-id').addEventListener("click", function() {
//         closePopup('select-popup-id');
//     });

//     // Close the profile popup when the close button is clicked
//     document.getElementById('select-profile-popup-close-id').addEventListener("click", function() {
//         closePopup('profile-add-photo-popup-id');
//     });

//     // Close the profile edit popup when the close button is clicked
//     document.getElementById('profile-edit-popup-close-id').addEventListener("click", function() {
//         closePopup('edit-profile-section-id');
//         console.log("popup")
//     });

//     // Close popups and overlays if the user clicks outside of them
//     window.addEventListener("click", function(event) {
//         const popups = [
//             'base-popup-id',
//             'select-popup-id',
//             'profile-add-photo-popup-id',
//             'edit-profile-section-id'
//         ];

//         console.log("User clicked:", event.target);

//         popups.forEach(function(popupId) {
//             const popup = document.getElementById(popupId);
//             // Check if the clicked element is not inside the popup and if the popup is displayed
//             if (!popup.contains(event.target) && popup.style.display === 'flex') {
//                 closePopup(popupId);
//             }
//         });
//     });
// });
