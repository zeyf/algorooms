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
      }
    },
    fontFamily: {
      noto: ['Open Sans', 'sans-serif'],
      monte: ['Montserrat', 'sans-serif'],
      inter: ['Inter', 'sans-serif']
    },
  },
  plugins: [
    require("flowbite/plugin")
  ],
}
