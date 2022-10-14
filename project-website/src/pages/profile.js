import React from "react";
import {useEffect, useState} from "react";
import { BrowserRouter as Router, Route, Navigate, useNavigate } from "react-router-dom";
const Profile = () => {
    const navigate = useNavigate();
    const [userId, setUserid]=useState(null)
    const [loggedIn, setLoggedIn]=useState("false")
    const [username, setUsername]=useState(null)
    const [password, setPassword]=useState(null)
    const [email, setEmail]=useState(null)
    const [dob, setDob]=useState(null)
    const [genderID, setGenderID]=useState(null)
    const [profileSuccess, setprofileSuccess]=useState(false) 
    function getSessionStorage() {
        setUserid(sessionStorage.getItem("id"))
        console.log(userId)
        setLoggedIn(sessionStorage.getItem("loggedIn"))
        console.log(loggedIn)
        getUserData(userId)
    }
    function getUserData(gotUserId) {
        let idInfo = {
            "id": sessionStorage.getItem("id")
        };
        fetch('/userDataRequest', {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify(idInfo)
        }).then(res => res.json()).then(
            data => {
                if (data.returncode === -1) {
                    navigate('/login')
                } else {
                    setUsername(data.username)
                    setPassword(data.password)
                    setEmail(data.email)
                    setDob(data.dateofbirth)
                    setGenderID(data.genderID)
                    setprofileSuccess(true)
                }
            }
        ).catch(error => {
            console.error('profile error!', error);
          });
    }
    function deleteProfile() {
        let idInfo = {
            "id": userId
        };
        fetch('/deleteProfile', {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify(idInfo)
        }).then(res => res.json()).then(
            data => {
                sessionStorage.removeItem("userId")
                sessionStorage.removeItem("loggedIn")
                navigate('/home')
            }

        )
    }
  return (
    <div>
      
      <h1>
      username: {username}
      </h1>
      <h1>
      password: {password}
      </h1>
      <h1>
      email: {email}
      </h1>
      <h1>
      DOB: {dob}
      </h1>
      <h1>
      gender: {genderID}
      </h1>
      <h1>
      {
        profileSuccess?
        <h2>
        <button onClick={()=>deleteProfile()}> 
        delete profile</button>
        </h2>:null
      }
      </h1>
        <button onClick={()=>getSessionStorage()}> 
        see profile</button>
      
      
    </div>
  );
};
  

//{userId}
//        {
//            loggedIn?            
//            null:<Navigate to="/login" />
//        }
export default Profile;