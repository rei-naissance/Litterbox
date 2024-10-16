import { hideElement, toggleOverlay} from './function.js'; 


document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('add-profile-photo-id')
        .addEventListener("click", function(event) {
            hideElement('profile-popup-add-id', 'flex')
    })

    document.getElementById('add-profile-button-id')
        .addEventListener("click", function(event) {
            toggleOverlay('profile-add-photo-popup-id','flex')
            toggleOverlay('overlay','flex')
    })

    document.getElementById('profile-popup-open-id')
        .addEventListener("click", function(event) {
            toggleOverlay('edit-profile-section-id','flex')
            toggleOverlay('overlay','flex')
    })

    document.getElementById('add-profile-button-id')
    .addEventListener("click", function(event) {
        toggleOverlay('profile-add-photo-popup-id','flex')
})

    document.getElementById('edit-about-id')
    .addEventListener("click", function(event) {
        toggleOverlay('edit-about-container-id', 'none')
        toggleOverlay('about-form-id', 'flex')
        console.log("ok")
    })
});