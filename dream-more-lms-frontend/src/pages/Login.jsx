import React from 'react';

function Login() {
  return (
    <div className="min-h-screen bg-dark text-white flex items-center justify-center">
      <div className="bg-white p-8 rounded shadow-md w-full max-w-md">
        <h2 className="text-2xl font-bold mb-4 text-dark">Login</h2>
        <form>
          <div className="mb-4">
            <label className="block text-dark mb-2">Email</label>
            <input
              type="email"
              className="w-full p-2 border border-gray-300 rounded"
              placeholder="Enter your email"
            />
          </div>
          <div className="mb-6">
            <label className="block text-dark mb-2">Password</label>
            <input
              type="password"
              className="w-full p-2 border border-gray-300 rounded"
              placeholder="Enter your password"
            />
          </div>
          <button
            type="submit"
            className="w-full bg-primary text-white p-2 rounded hover:bg-orange-600"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
}

export default Login;
