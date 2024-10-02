function hideElement(DIVname, condition) {
    var x = document.getElementById(DIVname);


    // style = condition;
    // if(condition === "flex") {
    //     style = "flex"
    // }

    if (x.style.display !== "flex") {
      x.style.display = condition;
    } else {
      x.style.display = "none";
    }
}

function toggleOverlay(DIVname, condition) {
    hideElement(DIVname, condition)
    hideElement('overlay', 'flex');
}

function replaceElement(DIVname1, condition1 , DIVname2, condition2){
    hideElement(DIVname1, condition1)
    // console.log("ok")
    hideElement(DIVname2, condition2)
    // console.log("ok")
}

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
    .addEventListener("click", function(event) {replaceElement('base-popup-id','flex', 'select-popup-id', 'flex')
})

document.getElementById('select-popup-close-id')
    .addEventListener("click", function(event) {
        toggleOverlay('select-popup-id','flex')
})

document.getElementById('add-profile-photo-id')
    .addEventListener("click", function(event) {
        hideElement('profile-popup-add-id', 'flex')
})

document.getElementById('add-profile-button-id')
    .addEventListener("click", function(event) {
        toggleOverlay('profile-add-photo-popup-id','flex')
})

document.getElementById('select-profile-popup-close-id')
    .addEventListener("click", function(event) {
        toggleOverlay('profile-add-photo-popup-id','flex')
})