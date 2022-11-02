import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages';
import Contact from './pages/contact';
import Login from './pages/login';
import Portfolio from './pages/portfolio';
import SignUp from './pages/signup';
import Profile from './pages/profile'
import Trade from './pages/trade'
import PortfolioChange from './pages/portfolioChange';
function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route exact path="/" exact element={<Home />} />
        <Route exact path="/contact" exact element={<Contact />} />
        <Route exact path="/login" exact element={<Login />} />
        <Route exact path="/portfolio" exact element={<Portfolio />} />
        <Route exact path="/portfolioChange" exact element={<PortfolioChange />} />
        <Route exact path="/signup" exact element={<SignUp />} />
        <Route exact path="/profile" exact element={<Profile />} />
        <Route exact path="/trade" exact element={<Trade />} />
      </Routes>
    </Router>
  );
}
export default App;