import React from 'react';

const CallToActionSection = () => (
  <section className="bg-white py-12 text-center">
    <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
      <div className="text-left">
        <img src="https://via.placeholder.com/200" alt="Instructor" className="rounded-full mx-auto mb-4" />
        <h3 className="text-2xl font-bold text-primary-dark-blue">Become an Instructor</h3>
        <p className="text-gray-600">Join the world’s largest community of students on Dream More. We provide the tools and skills to teach what you love.</p>
        <button className="bg-primary-orange text-white px-6 py-3 rounded-md mt-4 hover:bg-orange-600">Start Your Journey</button>
      </div>
      <div className="text-left">
        <img src="https://via.placeholder.com/200" alt="Student" className="rounded-full mx-auto mb-4" />
        <h3 className="text-2xl font-bold text-primary-dark-blue">Transform Your Life through Education</h3>
        <p className="text-gray-600">Learners from around the world are launching careers, advancing in their fields, and enriching lives.</p>
        <a href="#" className="text-primary-orange mt-4 inline-block">Checkout Courses</a>
      </div>
    </div>
  </section>
);

export default CallToActionSection;