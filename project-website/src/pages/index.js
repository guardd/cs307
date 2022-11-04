import React from "react";
import './index.css';
import home from "./pexels-markus-spiske-330771.jpg";

const Home = () => {
  return (
    <div>
      <img
        src={home}
        alt="car"
      />
      <div className= 'about'>
        <h1 className='about-title'>Who We Are</h1>
        <p className='about-words'>This is who we are</p>
      </div>
      <div className= 'mission'>
        <h1 className='mission-title'>Our Mission</h1>
        <p className='about-words'>This is our Mission</p>
        
      </div>
    </div>
  );

};
  
export default Home;
