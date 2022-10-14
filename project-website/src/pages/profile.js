import React from "react";
import {useEffect, useState} from "react";
import { BrowserRouter as Router, Route, Navigate, useNavigate } from "react-router-dom";
import Select from 'react-select';
import './profile.css';
const Profile = () => {
    var colors = [
        {
            value: 1,
            label: "coral"
        },
        {
            value: 2,
            label: "yellow"
        },
        {
            value: 3,
            label: "teal"
        },
        {
            value: 4,
            label: "pink"
        },
        {
            value: 4,
            label: "purple"
        },
        {
            value: 4,
            label: "green"
        },
    ];
    var [setbgColor, colorValue] = useState(colors.label);
    var colorHandle = e => {
        colorValue(e.label);
    }
    const navigate = useNavigate();
    const [userId, setUserid]=useState(null)
    const [loggedIn, setLoggedIn]=useState("false")
    const [username, setUsername]=useState(null)
    const [password, setPassword]=useState(null)
    const [email, setEmail]=useState(null)
    const [dob, setDob]=useState(null)
    const [genderID, setGenderID]=useState(null)
    const [profileSuccess, setprofileSuccess]=useState(false)
    const [editUsername, setEditUsername]=useState(false)  
    const [editPassword, setEditPassword]=useState(false)
    const [changeUsername, setChangeUsername]=useState(null)
    const [changeUsernameDuplicate, setChangeUsernameDuplicate]=useState(false)
    const [changePassword, setChangePassword]=useState(null)
    function getChangeUsername(val) {
        setChangeUsername(val.target.value)
    }
    function getChangePassword(val) {
        setChangePassword(val.target.value)
    }
    function getSessionStorage() {
        setUserid(sessionStorage.getItem("id"))
        console.log(userId)
        setLoggedIn(sessionStorage.getItem("loggedIn"))
        console.log(loggedIn)
        getUserData(userId)
    }
    function usernameChange(){
        let usernameChangeInfo = {
            "id": sessionStorage.getItem("id"),
            "changeUsername": changeUsername
        };
        fetch('/usernameChange', {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify(usernameChangeInfo)
        }).then(res => res.json()).then(
            data => {
                if (data.returncode === "0") {
                    setUsername(changeUsername)
                    setEditUsername(false)
                    setChangeUsernameDuplicate(false)
                } else {
                    setChangeUsernameDuplicate(true)
                }
            }
        )
    }
    function passwordChange(){
        let passwordChangeInfo = {
            "id": sessionStorage.getItem("id"),
            "changePassword": changePassword
        };
        fetch('/passwordChange', {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify(passwordChangeInfo)
        }).then(res => res.json()).then(
            data => {
                setPassword(changePassword)
                setEditPassword(false)
            }
        )
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
    <div className= 'container'>
      <div className='profile-box'>
          <div className='profile-content'>
      <h1 className= 'username'>
      username: {username}
      </h1>
      <h1 className= 'password'>
      password: {password}
      </h1>
      <h1 className= 'email'>
      email: {email}
      </h1>
      <h1 className= 'dob'>
      DOB: {dob}
      </h1>
      <h1 className= 'gender'>
      gender: {genderID}
      </h1>
      <h1>
      {
        profileSuccess?
        <h2>
        <button className='delete' onClick={()=>deleteProfile()}> 
        delete profile</button>
        <button className = 'editUser' onClick={()=>setEditUsername(true)}> 
        edit username</button>
        <button className = 'editPass' onClick={()=>setEditPassword(true)}> 
        edit password</button>
        </h2>:null
      }
      {
        editUsername?
        <h2>
            New Username:<input type="text" onChange={getChangeUsername} 
             placeholder="Enter New Username"/>
            <button onClick={()=>usernameChange(changeUsername)}> Change Username complete </button>
            {
                changeUsernameDuplicate?
                <h3>
                    duplicate username, change another
                </h3>:null
            }
        </h2>:null
      }
      {
        editPassword?
        <h2>
            New Password:<input type="text" onChange={getChangePassword} 
             placeholder="Enter New Password"/>
            <button onClick={()=>passwordChange(changeUsername)}> Change Password complete</button>
        </h2>:null
      }
      </h1>
        <button onClick={()=>getSessionStorage()}> 
        see profile</button>
        <style>{'body {background-color:'+setbgColor+';}'}</style>
        <Select options={colors} onChange={colorHandle}/>
        </div>
    </div>
    </div>
  );
};
  

//{userId}
//        {
//            loggedIn?            
//            null:<Navigate to="/login" />
//        }
export default Profile;
