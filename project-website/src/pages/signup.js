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
  function getUsername(val)
  {
    pushUsername(val.target.value)
  }
  function getPassword(val)
  {
    pushPassword(val.target.value)
  }
  function getEmail(val)
  {
    pushEmail(val.target.value)
  }
  function getVerifyCode(val)
  {
    pushVerifyCode(val.target.value)
  }

  function send_verify_email() {
    let user = username
    let pass = password
    let ee = email
    let verifyInfo = {
      "username": user,
      "password": pass,
      "email": ee
    };
    fetch('/userSignup', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(verifyInfo)
    }).then(res => res.json()).then(
      data => {
        var returnCode = data.returncode;
        if (returnCode === -1) {

          pushVerifyFailMessage("duplicate username")
        } else if (returnCode === -2) {

          pushVerifyFailMessage("duplicate email")
        } else {
          pushVerified(true) 
          setShow(true)
        }
      }

    ).catch(error => {
      console.error('Verify error!', error);
    });
  }
  function verify_email(veCode) {
    let code = {
      "code": veCode
    };
    fetch('/emailVerification', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(code)
    }).then(res=>res.json()).then(
      data => {
        var returnCode = data.returncode;
        if (returnCode === -1) {
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
        <button className="verify-button-button"
        onClick={()=>verify_email(verifyCode)}>
        </button>
        </div>
        :<div>
        verifyFailMessage
        </div>
      }

          <div className="signUp-content">
            <h1 className="signUp-title">Sign Up</h1>
            <div className="signUp-username">
              <input type="text" onChange={getUsername} 
              className="signUp-username-input" placeholder="Enter Username"/>
            </div>
            <div className="signUp-password">
              <input type="text" onChange={getPassword} 
              className="signUp-password-input" placeholder="Enter Password"/>
            </div>
            <div className="signUp-email">
              <input type="text" onChange={getEmail} 
              className="signUp-email-input" placeholder="Enter email"/>
            <div className="signUp-button">
              <button id="button" className="signUp-button-button" onClick={()=>send_verify_email()}> 
              Sign Up
              </button>
            </div>
            {
              show && <div id = "verification" className="signUp-verification">
              <div className="signUp-verify">
                <input type="text" onChange={getVerifyCode} 
                className="signUp-verify-input" placeholder="Enter Verification"/>
              </div>
              <div className="signUp-verify-button">
                <button id='button-verify' type="submit" className="signUp-verify-verify" onClick={()=>verify_email(verifyCode)}> 
                Verify
                </button>
              </div>
              </div>
            }

          </div>

        
        <h1>
          
        </h1>
      </div>
    </div>
  );
};
  
export default SignUp;
