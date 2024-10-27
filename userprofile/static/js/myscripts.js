import { hideElement, toggleOverlay, replaceElement} from './function.js'; 




document.getElementById('edit-about-id')
    .addEventListener("click", function(event) {
        hideElement('about-detail-id', 'flex')
        console.log("ok")
    })

document.getElementById('popup-edit-cover-id')
    .addEventListener("click", function(event) {
        toggleOverlay('base-popup-id','flex')
    })

document.getElementById('base-popup-close-id')
    .addEventListener("click", function(event) {
    toggleOverlay('base-popup-id','flex')
    console.log("ok")
})

document.getElementById('add-cover-photo-id')
    .addEventListener("click", function(event) {
        replaceElement('base-popup-id','flex', 'select-popup-id', 'flex')
})

document.getElementById('select-popup-close-id')
    .addEventListener("click", function(event) {
        toggleOverlay('select-popup-id','flex')
})

document.getElementById('add-profile-photo-id')
    .addEventListener("click", function(event) {
        toggleOverlay('profile-popup-add-id', 'flex')
})

document.getElementById('add-profile-button-id')
    .addEventListener("click", function(event) {
        toggleOverlay('profile-add-photo-popup-id','flex')
})

document.getElementById('select-profile-popup-close-id')
    .addEventListener("click", function(event) {
        toggleOverlay('profile-add-photo-popup-id','flex')
})

