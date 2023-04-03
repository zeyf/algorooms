/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
    "./node_modules/flowbite-react/**/*.js",

 
    // Or if using `src` directory:
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    colors: {
      navbar: '#051135',
    },
    extend: {},
    fontFamily: {
      abc: ['Open Sans', 'sans-serif']
    },
  },
  plugins: [
    require("flowbite/plugin")
  ],
}
