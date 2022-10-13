import React, {useEffect, useState} from "react";
import './signup.css'
const SignUp = () => {
  const [username, pushUsername]=useState(null)
  const [password, pushPassword]=useState(null)
  const [email, pushEmail]=useState(null)
  const [verifyCode, pushVerifyCode]=useState(null)
  const [verified, pushVerified]=useState(false)
  const [verifyFailed, pushVerifyFailed]=useState(false)
  const [verifyFailMessage, pushVerifyFailMessage] = useState("verify")
  const [show, setShow] = useState(false);

  function send_verify_email(username, password, email) {
    let verifyInfo = {
      "username": username,
      "password": password,
      "email": email
    };
    fetch('/userSignup', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(verifyInfo)
    }).then(res => res.json()).then(
      data => {
        var returnCode = data.returncode;
        if (returnCode == -1) {

          pushVerifyFailMessage("duplicate username")
        } else if (returnCode == -2) {

          pushVerifyFailMessage("duplicate email")
        } else {
          pushVerified(true) 

        }
      }

    ).catch(error => {
      console.error('Verify error!', error);
    });
  }
  function verify_email(inputcode) {
    let code = {
      "code": inputcode
    };
    fetch('/emailVerification', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(code)
    }).then(res=>res.json()).then(
      data => {
        var returnCode = data.returncode;
        if (returnCode == -1) {
          pushVerifyCode("wrong code");
          
        } else {
          pushUsername("verification success!")
        }
      }
    )

  }

  return (     
    <div className="signUp-container">
      {
        verified?
        <div className="verify-Button">
        <button type="submit" className="verify-button-button"
        onClick={()=>verify_email(verifyCode)}>
        </button>
        </div>
        :<div>
        verifyFailMessage
        </div>
      }
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
            <div className="signUp-email">
              <input type="text" onChange={pushEmail} 
              className="signUp-email-input" placeholder="Enter email"/>
            <div className="signUp-button">
              <button id="button" type="submit" className="signUp-button-button" onClick={()=>setShow(true)} onClick={()=>send_verify_email(username, password, email)}> 
              Sign Up
              </button>
            </div>
            {
              show && <div id = "verification" className="signUp-verification">
              <div className="signUp-verify">
                <input type="text" onChange={pushVerifyCode} 
                className="signUp-verify-input" placeholder="Enter Verification"/>
              </div>
              <div className="signUp-verify-button">
                <button id='button-verify' type="submit" className="signUp-verify-verify"> 
                Verify
                </button>
              </div>
              </div>
            }

          </div>
        </div>
        
        <h1>
          
        </h1>
      </div>
  );
};
  
export default SignUp;
