import React, {useEffect, useState} from "react";
  
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
      }
    ).catch(error => {
      console.error('login error!', error);
    });
  }
  return (
    <div>
      {
        loggedIn?
        <h1>
          {userId}
        </h1>
        :null
      }
      <h1>
        username:
        <input type="text" onChange={getUsername} />
      </h1>
      <h1>
        password:
        <input type="text" onChange={getPassword} />
      </h1>
      <h1>
        <button onClick={()=>getUserid(username, password)}> Login</button>
      </h1>
    </div>
  );
};
  
export default Login;