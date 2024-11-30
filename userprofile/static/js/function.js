// export function hideElement(DIVname, condition) {toggleVisibility
//     const x = document.getElementById(DIVname);
//     if (x) {
//         x.style.display = (condition === "flex") ? "flex" : "none";
//     }
// }

// export function toggleOverlay(DIVname, condition) {
//     hideElement(DIVname, condition);
// }

// export function replaceElement(DIVname1, condition1, DIVname2, condition2) {
//     hideElement(DIVname1, condition1);
//     hideElement(DIVname2, condition2);
// }

// Function to toggle visibility of elements
export function toggleVisibility(element) {
    element.classList.toggle("hidden"); 
}


