import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages';
import Contact from './pages/contact';
import Login from './pages/login';
import Portfolio from './pages/portfolio';
import SignUp from './pages/signup';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route exact path="/" exact element={<Home />} />
        <Route exact path="/contact" exact element={<Contact />} />
        <Route exact path="/login" exact element={<Login />} />
        <Route exact path="/portfolio" exact element={<Portfolio />} />
        <Route exact path="/signup" exact element={<SignUp />} />
      </Routes>
    </Router>
  );
}
export default App;