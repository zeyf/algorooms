/** @type {import('tailwindcss').Config} */

const withMT = require('@material-tailwind/react/utils/withMT');
const plugin = require('tailwindcss/plugin');

module.exports = withMT({
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './node_modules/flowbite-react/**/*.js',

    // Or if using `src` directory:
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    colors: {
      darkAccent: '#051135',
      greenAccent: '#19F8A7',
      lightAccent: '#222C4A',
      gradientEnd: '#24366c',
    },
    extend: {
      keyframes: {
        'fade-in-down': {
          '0%': {
            opacity: '0',
            transform: 'translateY(0px)',
          },
          '100%': {
            opacity: '1',
            transform: 'translateY()',
          },
        },
      },
      animation: {
        'fade-in-down': 'fade-in-down 1s ease-out',
      },
    },
    fontFamily: {
      noto: ['Open Sans', 'sans-serif'],
      monte: ['Montserrat', 'sans-serif'],
      inter: ['Inter', 'sans-serif'],
      mono: ["ui-monospace", "SFMono-Regular", "Menlo", "Monaco", "Consolas", "Liberation Mono", "Courier New", "monospace"]
    },
  },
  plugins: [
    require('tailwind-scrollbar'),
    require('flowbite/plugin'),
    plugin(function ({ addUtilities }) {
      addUtilities({
        '.hide-scrollbar::-webkit-scrollbar': {
          display: 'none',
        },
        '.hide-scrollbar': {
          '-ms-overflow-style': 'none',
          'scrollbar-width': 'none',
        },
      });
    }),
  ],
});
