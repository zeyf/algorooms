/** @type {import('tailwindcss').Config} */

const withMT = require("@material-tailwind/react/utils/withMT");

module.exports =withMT({
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
      darkAccent: "#051135",
      greenAccent: "#19F8A7",
    },
    extend: {
        keyframes: {
          'fade-in-down': {
              '0%': {
                  opacity: '0',
                  transform: 'translateY(0px)'
              },
              '100%': {
                  opacity: '1',
                  transform: 'translateY()'
              },
          }
      },
      animation: {
          'fade-in-down': 'fade-in-down 1s ease-out'
      },

      '.custom-split .split-drag': {
        cursor: 'col-resize',
      }
    },
    fontFamily: {
      noto: ['Open Sans', 'sans-serif'],
      monte: ['Montserrat', 'sans-serif'],
      inter: ['Inter', 'sans-serif']
    },
  },
  plugins: [
    require('tailwind-scrollbar'),
    require("flowbite/plugin")
  ],
})
