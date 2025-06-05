import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { logout } from '../features/authSlice';
import logo from '../assets/logo.jpg'; 

const Navbar = () => {
  const { user } = useSelector((state) => state.auth);
  const dispatch = useDispatch();

  return (
    <nav className="bg-white shadow-md py-3 px-6">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        {/* Left Section */}
        <div className="flex items-center space-x-4">
          <img src={logo} alt="Dream More Logo" className="h-10 w-10 rounded-full" />
          <a href="#" className="text-gray-800 font-medium hover:underline">Categories</a>
        </div>

        {/* Center Section */}
        <div className="flex-1 mx-6 hidden md:flex">
          <input
            type="text"
            placeholder="Search courses..."
            className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-orange-400"
          />
        </div>

        {/* Right Section */}
        <div className="flex items-center space-x-4">
          <span className="text-gray-700 hidden md:block">Dream More</span>
          {user ? (
            <button
              onClick={() => dispatch(logout())}
              className="bg-orange-500 text-white px-4 py-2 rounded-md hover:bg-orange-600"
            >
              Logout
            </button>
          ) : (
            <>
              <a
                href="/login"
                className="px-4 py-2 border border-gray-300 rounded-md hover:bg-gray-100"
              >
                Log In
              </a>
              <a
                href="/register"
                className="bg-orange-500 text-white px-4 py-2 rounded-md hover:bg-orange-600"
              >
                Sign Up
              </a>
            </>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
