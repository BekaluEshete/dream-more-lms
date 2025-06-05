import React from 'react';

const TopInstructorsSection = () => (
  <section className="bg-white py-12">
    <div className="container mx-auto">
      <h2 className="text-2xl font-bold text-primary-dark-blue mb-6 text-center">Top Instructors</h2>
      <div className="grid grid-cols-1 md:grid-cols-5 gap-6">
        {['Ronald Richards', 'Ronald Richards', 'Ronald Richards', 'Ronald Richards', 'Ronald Richards'].map((instructor) => (
          <div key={instructor} className="text-center">
            <img src="https://via.placeholder.com/100" alt={instructor} className="rounded-full mx-auto mb-2" />
            <h3 className="text-lg font-semibold">{instructor}</h3>
            <p className="text-sm text-gray-600">4.8 | 300 Students</p>
          </div>
        ))}
      </div>
      <a href="#" className="text-primary-orange mt-4 inline-block">See All</a>
    </div>
  </section>
);

export default TopInstructorsSection;