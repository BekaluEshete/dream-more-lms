import React from 'react';

const CategoriesSection = () => (
  <section className="bg-white py-12">
    <div className="container mx-auto">
      <h2 className="text-2xl font-bold text-primary-dark-blue mb-6 text-center">Categories</h2>
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        {['App Development', 'Web Development', 'Marketing', 'Physics'].map((cat) => (
          <div key={cat} className="bg-gray-100 p-4 rounded-lg text-center">
            <div className="text-gray-500 mb-2">{cat}</div>
            <div className="text-sm text-gray-600">12 Courses</div>
          </div>
        ))}
      </div>
      <a href="#" className="text-primary-orange mt-4 inline-block">See All</a>
    </div>
  </section>
);

export default CategoriesSection;