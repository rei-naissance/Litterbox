import {toggleVisibility} from './function.js'; 

document.addEventListener("DOMContentLoaded", function() {
    var profilePopup = document.getElementById("edit-profile-section-id");
    var overlay = document.getElementById("overlay");

    var settingAdditionalSettings = document.getElementById("myDropdown")
    document.getElementById('profile-settings-id').addEventListener("click", function() {
        toggleVisibility(settingAdditionalSettings);
    });
    // Close the dropdown if the user clicks outside of it
    window.addEventListener("click", function(event) {
        if (!settingAdditionalSettings.classList.contains('hidden')) {
            if (!event.target.closest('#profile-settings-id')){
                toggleVisibility(settingAdditionalSettings);
            }
        }
    });


    // Open profile popup and overlay
    document.getElementById('profile-popup-open-id').addEventListener("click", function() {
        toggleVisibility(profilePopup);
        toggleVisibility(overlay);
    });
    // Close profile popup and overlay if clicking outside of them
    window.addEventListener("click", function(event) {
        if (!profilePopup.classList.contains('hidden')) {
            if (!event.target.closest('#edit-profile-section-id') &&
                !event.target.closest('#profile-popup-open-id')) {
                toggleVisibility(profilePopup);
                toggleVisibility(overlay);
            }
        }
    });

    // Close profile popup and overlay with close button
    document.getElementById('profile-edit-popup-close-id').addEventListener("click", function() {
        toggleVisibility(profilePopup);
        toggleVisibility(overlay);
    });


    var addProfilePhotoPopup = document.getElementById('profile-popup-add-id')
    document.getElementById('add-profile-photo-id').addEventListener("click", function() {
        toggleVisibility(addProfilePhotoPopup);
    });
    // Close add profile photo button popup if clicking outside of them
    window.addEventListener("click", function(event) {
        if (!addProfilePhotoPopup.classList.contains('hidden')) {
            if (!event.target.closest('#add-profile-photo-id')){
                toggleVisibility(addProfilePhotoPopup);
            }
        }
    });

    var profilePhotoPopup = document.getElementById('profile-add-photo-popup-id')
    document.getElementById('add-profile-button-id').addEventListener("click", function() {
        toggleVisibility(profilePhotoPopup);
        toggleVisibility(overlay); 
        console.log("clicked")
    });

    window.addEventListener("click", function(event) {
        if (!profilePhotoPopup.classList.contains('hidden')) {
            if (!event.target.closest('#profile-add-photo-popup-id') && !event.target.closest('#add-profile-button-id')){
                toggleVisibility(profilePhotoPopup);
                toggleVisibility(overlay);
            }
        }
    });

    document.getElementById('select-profile-popup-close-id').addEventListener("click", function() {
        toggleVisibility(profilePhotoPopup);
        toggleVisibility(overlay);
    });



    var origAboutContainer = document.getElementById('edit-about-container-id')
    var formAboutContainer = document.getElementById('about-form-id')
    document.getElementById('edit-about-id').addEventListener("click", function() {
        toggleVisibility(origAboutContainer);
        toggleVisibility(formAboutContainer);
    });

    var origLinksContainer = document.getElementById('edit-links-container-id')
    var formLinksContainer = document.getElementById('edit-forms-container-v2')
    var editLinksBtn = document.getElementById('edit-link-btn-id')
    editLinksBtn.addEventListener("click", function() {
        toggleVisibility(origLinksContainer);
        toggleVisibility(formLinksContainer);
        toggleVisibility(editLinksBtn);
    });



    function getLogoUrl(url) {
        if (!/^https?:\/\//i.test(url)) {
            url = 'https://' + url;
        }

        try {
            const domain = new URL(url).hostname;
            return `https://www.google.com/s2/favicons?sz=64&domain=${domain}`;
        } catch (error) {
            console.error("Invalid URL:", url);
            return null;
        }
    }


    document.querySelectorAll('.social-link').forEach(link => {
        const url = link.getAttribute('data-url');
        const logoUrl = getLogoUrl(url);
        
        const img = document.createElement('img');
        img.src = logoUrl;
        img.width = 16;
        img.height = 16;
        img.alt = "Logo";
        img.style.verticalAlign = "middle";
        img.style.marginRight = "5px"; 

        link.appendChild(img);
        link.appendChild(document.createTextNode(url));
    });

});