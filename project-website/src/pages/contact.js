import React, {useEffect, useState} from "react";
const Contact = () => {
  const [name, pushName]=useState(null)
  const [contact, pushContact]=useState(null)

  
  return (  
    <div className="contact-container">
        <form className="contact-Form">
          <div className="contact-content">
            <h1 className="contact-title">Sign Up</h1>
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
            <div className="contact-password">
              <label>Problem</label>
              <textarea 
              className="contact-password-input" placeholder="Enter Password" rows="4" cols="50"/>
            </div>
            <div className="contact-button">
              <button type="submit" className="contact-button-button"> 
              Submit
              </button>
            </div>
          </div>
        </form>
        
        <h1>
          
        </h1>
      </div>
  );
};
  
export default Contact;
