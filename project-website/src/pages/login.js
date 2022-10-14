import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Route, Navigate } from "react-router-dom";
import {useEffect, useState} from "react";
import './login.css'
const Login = () => {
  const [username, setUsername]=useState(null)
  const [password, setPassword]=useState(null)
  const [userId, setUserid]=useState(null)
  const [loggedIn, setLoggedIn]=useState(false)
  const [email, setEmail]=useState(null)
  const [emailMessage, setEmailMessage]=useState(null)
  function getUsername(val)
  {
    setUsername(val.target.value)
    console.warn(val.target.value)
  }
  function getPassword(val)
  {
    setPassword(val.target.value)
    console.warn(val.target.value)
  }
  function getEmail(val)
  {
    setEmail(val.target.value)
  }
  function sendRecoveryEmail()
  {
    let emailInfo = {
      "email": email
    };
    fetch('/passwordRecovery', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(emailInfo)
    })
    setEmailMessage("Email sent")
  }
  const [show, setShow] = useState(false);
  function getUserid(username, password) {
    let loginInfo = {
      "username": username,
      "password": password
    };
    fetch('/loginMethod', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(loginInfo)
    }).then(res => res.json()).then(
      data => {
        if(data.returncode === "-1") {
          return;
        }
        setUserid(data.id);
        console.log(data)
        console.log("login success?" + userId + ", " + data.id)
        sessionStorage.setItem("loggedIn", "true")
        sessionStorage.setItem("id", data.id)
        console.log(sessionStorage.getItem("loggedIn"))
        setLoggedIn(true)
      }
    ).catch(error => {
      console.error('login error!', error);
    });
  }
  return (
    <div className="logIn-container">
      <div className="logIn-Form">
        <div className="logIn-content">
          <h1 className="logIn-title">Log In</h1>
          <div className="logIn-username">
            <input type="text" onChange={getUsername} 
            className="logIn-username-input" placeholder="Enter Username"/>
          </div>
          <div className="logIn-password">
            <input type="text" onChange={getPassword} 
            className="logIn-password-input" placeholder="Enter Password"/>
          </div>
          <div className="logIn-button">
            <button type="submit" className="logIn-button-button"
            onClick={()=>getUserid(username, password)}> 
            Log In
            </button>
          </div>
          <p className="forgot-password">
            Forgot <a href="#" onClick={()=>setShow(true)}>password?</a>
          </p>
          {
        loggedIn?
        <Navigate to="/profile" />
        :
        <div>
          {
            show && <h1 className="login-forgot">
            <input type="text" onChange={getEmail} 
            className="logIn-email-input" placeholder="Enter Email"/>
            <button className="recovery-button" onClick={()=>sendRecoveryEmail(email)}> Send Recovery Email </button>
            {emailMessage}
          </h1>
          }
        </div>
      }
        </div>
        </div>
      
      <h1>
        
      </h1>
    </div>
);
};
export default Login;
