import React, {useEffect, useState} from "react";
import './contact.css'
const Contact = () => {
  const [name, pushName]=useState(null)
  const [contact, pushContact]=useState(null)

  
  return (  
    <div className="contact-container">
        <div className="contact-Form">
          <div className="contact-content">
            <h1 className="contact-title">Contact Us</h1>
            <div className="contact-Name">
              <label>Name</label>
              <input type="text" onChange={pushName} 
              className="contact-name-input" placeholder="Enter Your Name"/>
            </div>
            <div className="contact-contact">
              <label>Email</label>
              <input type="text" onChange={pushContact} 
              className="contact-contact-input" placeholder="Enter Your Email"/>
            </div>
            <div className="contact-problem">
              <label>Problem</label>
              <textarea 
              className="contact-problem-input" placeholder="Enter Problem" rows="4" cols="35"/>
            </div>
            <div className="contact-button">
              <button type="submit" className="contact-button-button"> 
              Submit
              </button>
            </div>
          </div>
        </div>
        
        <h1>
          
        </h1>
      </div>
  );
};
  
export default Contact;
