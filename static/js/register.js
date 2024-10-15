// Get the password input and strength meter elements
const passwordInput = document.getElementById("id_password");
const meterBars = document.querySelectorAll(".flex .rounded-lg");

// Password strength check function
function updateStrengthMeter() {
  const password = passwordInput.value;
  let strength = 0;

  // Check if the password has at least 8 characters
  if (password.length >= 8) {
    strength++;
  }

  // Check if the password contains at least one number
  if (/\d/.test(password) || /[!@#$%^&*(),.?":{}|<>]/.test(password)) {
    strength++;
  }

  // Check if the password contains at least one uppercase letter
  if (/[A-Z]/.test(password)) {
    strength++;
  }

  // Reset all bars and the password input's border to gray first
  meterBars.forEach((bar) => {
    bar.classList.remove("bg-red-400", "bg-yellow-400", "bg-green-400");
    bar.classList.add("bg-gray-400");
  });

  passwordInput.classList.remove(
    "border-red-400",
    "border-yellow-400",
    "border-green-400"
  );
  passwordInput.classList.add("border-gray-400"); // Default border color

  // Apply colors based on the strength level
  if (strength === 1) {
    // When weak is met
    meterBars[0].classList.remove("bg-gray-400");
    meterBars[0].classList.add("bg-red-400");
    passwordInput.classList.remove("border-gray-400");
    passwordInput.classList.add("border-red-400");
  } else if (strength === 2) {
    // When medium is met
    meterBars[0].classList.remove("bg-gray-400");
    meterBars[0].classList.add("bg-yellow-400");
    meterBars[1].classList.remove("bg-gray-400");
    meterBars[1].classList.add("bg-yellow-400");
    passwordInput.classList.remove("border-gray-400", "border-red-400");
    passwordInput.classList.add("border-yellow-400");
  } else if (strength === 3) {
    // When strong is met
    meterBars[0].classList.remove("bg-gray-400");
    meterBars[0].classList.add("bg-green-400");
    meterBars[1].classList.remove("bg-gray-400");
    meterBars[1].classList.add("bg-green-400");
    meterBars[2].classList.remove("bg-gray-400");
    meterBars[2].classList.add("bg-green-400");
    passwordInput.classList.remove(
      "border-gray-400",
      "border-red-400",
      "border-yellow-400"
    );
    passwordInput.classList.add("border-green-400");
  }
}

const confirmPasswordInput = document.getElementById("id_confirm_password");
const continueButton = document.querySelector("button[type='submit']");

// Function to check if passwords match and update button color
function checkPasswordMatch() {
  // Only check if the confirm password field is not empty
  if (confirmPasswordInput.value === "") {
    // Reset button to original color (if no input in confirm password field)
    continueButton.classList.remove("bg-gray-500");
    continueButton.classList.remove("hover:bg-gray-700");
    continueButton.classList.add("bg-green-box");
    continueButton.classList.add("hover:bg-green-700");
  } else if (passwordInput.value !== confirmPasswordInput.value) {
    // If passwords don't match, turn the button red
    continueButton.classList.remove("bg-green-box");
    continueButton.classList.remove("hover:bg-green-700");
    continueButton.classList.add("bg-gray-500");
    continueButton.classList.add("hover:bg-gray-700");
  } else {
    // If passwords match, keep the original green color
    continueButton.classList.remove("bg-gray-500");
    continueButton.classList.remove("hover:bg-gray-700");
    continueButton.classList.add("bg-green-box");
    continueButton.classList.add("hover:bg-green-700");
  }
}

// Add event listeners to both password and confirm password input fields
confirmPasswordInput.addEventListener("input", checkPasswordMatch);
passwordInput.addEventListener("input", checkPasswordMatch);

// Add event listener to the password input field
passwordInput.addEventListener("input", updateStrengthMeter);
