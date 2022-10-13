import React, {useEffect, useState} from "react";
import './signup.css'
const SignUp = () => {
  const [username, pushUsername]=useState(null)
  const [password, pushPassword]=useState(null)
  return (  
    <div className="signUp-container">
        <div className="signUp-Form">
          <div className="signUp-content">
            <h1 className="signUp-title">Sign Up</h1>
            <div className="signUp-username">
              <input type="text" onChange={pushUsername} 
              className="signUp-username-input" placeholder="Enter Username"/>
            </div>
            <div className="signUp-password">
              <input type="text" onChange={pushPassword} 
              className="signUp-password-input" placeholder="Enter Password"/>
            </div>
            <div className="signUp-button">
              <button type="submit" className="signUp-button-button"> 
              Sign Up
              </button>
            </div>
          </div>
        </div>
        
        <h1>
          
        </h1>
      </div>
  );
};
  
export default SignUp;
