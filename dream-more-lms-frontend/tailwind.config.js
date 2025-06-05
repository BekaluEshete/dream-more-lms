/** @type {import('tailwindcss').Config} */
export const content = [
    './index.html',
    './src/**/*.{js,jsx,ts,tsx}',
];
export const theme = {
    extend: {
        colors: {
            'primary-orange': '#f47822',
            'primary-dark-blue': '#15142a',
        },
    },
};
export const plugins = [];
