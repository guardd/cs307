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
        setUserid(data.id);
        console.log(data)
        console.log("login success?" + userId + ", " + data.id)
        setLoggedIn(true)
        sessionStorage.setItem("loggedIn", true);
        sessionStorage.setItem("id", data.id)
      }
    ).catch(error => {
      console.error('login error!', error);
    });
  }
  return (
    <div className="logIn-container">
      {
        loggedIn?
        <Navigate to="/profile" />
        :null
      }
      <div className="login-Form">
        <div className="logIn-content">
          <h1 className="logIn-title">Log In</h1>
          <div className="logIn-username">
            <label>Username</label>
            <input type="text" onChange={getUsername} 
            className="logIn-username-input" placeholder="Enter Username"/>
          </div>
          <div className="logIn-password">
            <label>Password</label>
            <input type="text" onChange={getPassword} 
            className="logIn-password-input" placeholder="Enter Password"/>
          </div>
          <div className="logIn-button">
            <button type="submit" className="logIn-button-button"
            onClick={()=>getUserid(username, password)}> 
            Log In
            </button>
          </div>
        </div>
        </div>
      
      <h1>
        
      </h1>
    </div>
);
};

/*
with form : 
<form className="logIn-Form">
        <div className="logIn-content">
          <h1 className="logIn-title">Log In</h1>
          <div className="logIn-username">
            <label>Username</label>
            <input type="text" onChange={getUsername} 
            className="logIn-username-input" placeholder="Enter Username"/>
          </div>
          <div className="logIn-password">
            <label>Password</label>
            <input type="text" onChange={getPassword} 
            className="logIn-password-input" placeholder="Enter Password"/>
          </div>
          <div className="logIn-button">
            <button type="submit" className="logIn-button-button"
            onClick={()=>getUserid(username, password)}> 
            Log In
            </button>
          </div>
        </div>
      </form>
*/
export default Login;