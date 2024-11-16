// /** @type {import('tailwindcss').Config} */
// module.exports = {
//   content: ["./template/**/*.html", "./products/templates/**/*.html"],
//   theme: {
//     extend: {},
//   },
//   plugins: [],
// };

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Correct path to templates
    "./products/templates/**/*.html", // Path for the 'products' app templates
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
