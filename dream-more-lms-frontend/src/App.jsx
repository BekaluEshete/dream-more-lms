import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import Navbar from './components/Navbar';
import HeroSection from './components/HeroSection';
import StatsSection from './components/StatsSection';
import CategoriesSection from './components/CategoriesSection';
import TopCoursesSection from './components/TopCoursesSection';
import TopInstructorsSection from './components/TopInstructorsSection';
import TestimonialsSection from './components/TestimonialsSection';
import CallToActionSection from './components/CallToActionSection';
import Footer from './components/Fotter';
import { loginSuccess } from './features/authSlice';

const App = () => {
  const { user, } = useSelector((state) => state.auth);
  const dispatch = useDispatch();

  useEffect(() => {
    if (user) return;
    const token = localStorage.getItem('token');
    if (token) {
      dispatch(loginSuccess(JSON.parse(token)));
    }
  }, [dispatch, user]);

  return (
    <div>
      <Navbar />
      <HeroSection />
      <StatsSection />
      <CategoriesSection />
      <TopCoursesSection />
      <TopInstructorsSection />
      <TestimonialsSection />
      <CallToActionSection />
      <Footer />
    </div>
  );
};

export default App;