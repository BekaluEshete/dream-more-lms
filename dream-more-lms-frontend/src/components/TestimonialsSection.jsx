import React from 'react';

const TestimonialsSection = () => (
  <section className="bg-gray-200 py-12">
    <div className="container mx-auto">
      <h2 className="text-2xl font-bold text-primary-dark-blue mb-6 text-center">What Customers Say</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {['Markos', 'Temee', 'Habte'].map((name) => (
          <div key={name} className="bg-white p-4 rounded-lg shadow-md text-center">
            <p className="text-gray-600 mb-2">"Dream More courses are top-notch. As someone who's always looking to stay ahead in the rapidly evolving tech world, I appreciate the in-depth knowledge."</p>
            <img src="https://via.placeholder.com/50" alt={name} className="rounded-full mx-auto mb-2" />
            <h3 className="text-lg font-semibold">{name}</h3>
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default TestimonialsSection;