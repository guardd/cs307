import React from "react";
import { BrowserRouter as Router, Route, Navigate } from "react-router-dom";
const Profile = () => {
    const [userId, setUserid]=useState(sessionStorage.getItem("id"))
    const [loggedIn, setLoggedIn]=useState(sessionStorage.getItem("loggedIn")) 
  return (
    <div>
    <div>
        {
            loggedIn?            
            null:<Navigate to="/profile" />
        }

        </div>
      <h1>
        Portfolio here
      </h1>
    </div>
  );
};
  
export default Profile;