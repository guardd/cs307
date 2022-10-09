import React, {useEffect, useState} from "react";
  
const SignUp = () => {
  const [username, pushUsername]=useState(null)
  const [password, pushPassword]=useState(null)
  return (  
    <div className="signUp-container">
       
        <form className="signUp-Form">
          <div className="signUp-content">
            <h1 className="signUp-title">Sign Up</h1>
            <div className="signUp-username">
              <label>Username</label>
              <input type="text" onChange={pushUsername} 
              className="signUp-username-input" placeholder="Enter Username"/>
            </div>
            <div className="signUp-password">
              <label>Password</label>
              <input type="text" onChange={pushPassword} 
              className="signUp-password-input" placeholder="Enter Password"/>
            </div>
            <div className="signUp-button">
              <button type="submit" className="signUp-button-button"> 
              SignUp
              </button>
            </div>
          </div>
        </form>
        
        <h1>
          
        </h1>
      </div>
  );
};
  
export default SignUp;
