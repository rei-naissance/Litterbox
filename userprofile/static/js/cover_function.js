import { toggleOverlay, replaceElement } from './function.js'; 

document.addEventListener("DOMContentLoaded", function() {

    document.getElementById('base-popup-close-id')
        .addEventListener("click", function() {
            toggleOverlay('base-popup-id', 'none'); 
            toggleOverlay('overlay', 'none'); 
        });

    document.getElementById('add-cover-photo-id')
        .addEventListener("click", function() {
            replaceElement('base-popup-id', 'none', 'select-popup-id', 'flex');
        });

    document.getElementById('select-popup-close-id')
        .addEventListener("click", function() {
            toggleOverlay('select-popup-id', 'none');
            toggleOverlay('overlay', 'none');
        });

    document.getElementById('select-profile-popup-close-id')
        .addEventListener("click", function() {
            toggleOverlay('profile-add-photo-popup-id', 'none');
            toggleOverlay('overlay', 'none');
        });

    document.getElementById('popup-edit-cover-id')
        .addEventListener("click", function() {
            toggleOverlay('base-popup-id', 'flex');
            toggleOverlay('overlay', 'flex');
        });


    document.getElementById('profile-edit-popup-close-id')
        .addEventListener("click", function() {
            toggleOverlay('edit-profile-section-id', 'flex');
            toggleOverlay('overlay', 'flex');
        });
});
