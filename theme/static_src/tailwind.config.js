/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
  content: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
    "../templates/**/*.html",

    /*
     * Main templates directory of the project (BASE_DIR/templates).
     * Adjust the following line to match your project structure.
     */
    "../../templates/**/*.html",

    /*
     * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
     * Adjust the following line to match your project structure.
     */
    "../../**/templates/**/*.html",

    /**
     * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
     * patterns match your project structure.
     */
    /* JS 1: Ignore any JavaScript in node_modules folder. */
    // '!../../**/node_modules',
    /* JS 2: Process all JavaScript files in the project. */
    // '../../**/*.js',

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    // '../../**/*.py'
  ],
  theme: {
    extend: {
      boxShadow: {
        'gray-shadow': '0px 0px 18px 0px rgba(0, 0, 0, 0.3)',
      },
      fontSize: {
        10: "10px",
        11: "11px",
        12: "12px",
        13: "13px",
        14: "14px",
        16: "16px",
        20: "20px",
      },
      colors: {
        "gray-box": "#F7F7F7",
        "gray-box1": "#FAFAFA",
        "gray-font": "#A1A1A1",
        "gray-font1": "#6D6D6D",
        "blue-box": "#e5f1ff",
        "blue-font": "#3985de",
        "gray-btn": "#EDEDED",
        "input-border": "#A9A9A9",
        "green-box": "#087443",
        "bg-gray": "#FAFAFA",
        "border-gray": "#c1c1c1",
      },
      fontFamily: {
        sans: ["SFProDisplay", "sans-serif"],
      },
      letterSpacing: {
        tightest: "0.4px", // Custom letter spacing
      },
    },
  },
  plugins: [
    function ({ addUtilities }) {
      const newUtilities = {
        /* Correcting the syntax for webkit-scrollbar */
        ".no-scrollbar::-webkit-scrollbar": {
          display: "none",
        },
        ".no-scrollbar": {
          "-ms-overflow-style": "none", /* IE and Edge */
          "scrollbar-width": "none", /* Firefox */
        },
      };
      addUtilities(newUtilities);
    },  
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/aspect-ratio"),
  ],
};
