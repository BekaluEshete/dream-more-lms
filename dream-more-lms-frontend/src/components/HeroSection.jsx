import React from 'react';
import beke from '../assets/beke.jpg'; 
import habte from '../assets/habte.jpg'; 
import tom from '../assets/tom.jpg'; 



const HeroSection = () => (
  <section className="bg-white py-16 px-6 md:px-20 flex flex-col-reverse md:flex-row items-center justify-between relative overflow-hidden">
    {/* LEFT SIDE */}
    <div className="md:w-1/2 text-center md:text-left">
      <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4 leading-tight">
        Unlock Your Potential <br /> with Dream More
      </h1>
      <p className="text-lg text-gray-600 mb-6 max-w-lg">
        Welcome to Dream More, where learning knows no bounds. We believe that education is the key to personal and professional growth, and we’re here to guide you on your journey to success.
      </p>
      <button className="bg-orange-500 hover:bg-orange-600 transition text-white px-6 py-3 rounded-md shadow-md">
        Start your instructor journey
      </button>
    </div>

    {/* RIGHT IMAGES SECTION */}
    <div className="md:w-1/2 flex justify-center items-center relative h-[300px] w-full mb-10 md:mb-0">
      {/* Main (big) image */}
      <div className="w-48 h-48 md:w-60 md:h-60 rounded-full overflow-hidden border-4 border-white shadow-xl z-10 relative">
        <img src={habte} alt="Habte" className="w-full h-full object-cover" />
      </div>

      {/* Top-right smaller image */}
      <div className="absolute top-0 right-6 md:right-16 w-20 h-20 md:w-24 md:h-24 rounded-full overflow-hidden border-4 border-white shadow-lg bg-white">
        <img src={tom} alt="Tom" className="w-full h-full object-cover" />
      </div>

 
      <div className="absolute bottom-0 right-2 md:right-10 bg-yellow-400 rounded-xl p-3 flex items-center gap-3 shadow-lg w-[230px]">
        <img src={beke}alt="Beke" className="w-12 h-12 rounded-full" />
        <div>
          <p className="text-sm text-black font-medium">Join our community of</p>
          <p className="text-sm text-black font-bold">1500+ Students</p>
        </div>
      </div>
    </div>
  </section>
);

export default HeroSection;
