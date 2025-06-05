import React from 'react';

const TopCoursesSection = () => (
  <section className="bg-gray-200 py-12">
    <div className="container mx-auto">
      <h2 className="text-2xl font-bold text-primary-dark-blue mb-6 text-center">Top Courses</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {['Beginner Guide to Graphic Design', 'Introduction to Web Development', 'Introduction to Digital Marketing'].map((course) => (
          <div key={course} className="bg-white p-4 rounded-lg shadow-md">
            <img src="https://via.placeholder.com/150" alt={course} className="w-full h-32 object-cover rounded-md mb-4" />
            <h3 className="text-lg font-semibold">{course}</h3>
            <p className="text-sm text-gray-600">42 Hours | 10 Lessons</p>
            <p className="text-green-600 font-bold">$14.99</p>
          </div>
        ))}
      </div>
      <a href="#" className="text-primary-orange mt-4 inline-block">See All</a>
    </div>
  </section>
);

export default TopCoursesSection;