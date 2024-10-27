import {toggleOverlay} from './function.js'; 


function toggle(elementId, displayStyle) {
    var x = document.getElementById(elementId);
    if (x.style.display === "none" || x.style.display === "") {
        x.style.display = displayStyle;
    } else {
        x.style.display = "none";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('add-profile-photo-id')
        .addEventListener("click", function(event) {
            toggle('profile-popup-add-id', 'flex')
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