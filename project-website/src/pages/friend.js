import React from "react";
import {useEffect, useState} from "react";
import { BrowserRouter as Router, Route, Navigate, useNavigate } from "react-router-dom";
import Select from 'react-select';

const Friend = () => {
    const [texts, setTexts] = useState(null)
    const navigate = useNavigate();
    const [userId, setUserid]=useState(null)
    const [loggedIn, setLoggedIn]=useState("false")
    const [gotFriend, setgotFriend]=useState("false")
    const [friendRequests, setFriendRequests] = useState(null)
    const [friendRequestsNames, setFriendRequestsNames] = useState(null)
    const [friendNames, setFriendNames] = useState(null)
    const [friendIds, setFriendIds] = useState(null)
    const [friendRequestSize, setfriendRequestSize] = useState(null)
    const [friendSize, setfriendSize] = useState(null)
    const [otherUsername, setOtherUsername] = useState(null)
    const [addFriendFailInfo, setaddFriendFailInfo] = useState(null)
    const [friendChatname, setFriendChatname] = useState(null)
    const [friendChatid, setFriendChatid] = useState(null)
    const [choseFriend, setChoseFriend] = useState(false)
    const [portfolioName, setportfolioName] = useState(null)
    const [shareFailString, setshareFailString] = useState(null)
    const [chatFailString, setChatFailString] = useState(null)
    const [chatToSend, setChatToSend] = useState(null)
    const friendOptions = []
    const [friendOptionss, setFriendOptionss] = useState(null)
    const [chatting, setChatting] = useState(false)
    function getPortfolioName(val) {
        setportfolioName(val.target.value)
    }
    function getChatToSend(val) {
        setChatToSend(val.target.value)
    }
    function getOtherUsername(val)
    {
        setOtherUsername(val.target.value)
    }

    function getFriendOptionss(val)
    {
        setFriendOptionss(val)
    }

    function chooseFriendId(e) {
        setFriendChatname(e.label)        
        setFriendChatid(e.value)
        setChoseFriend(true)
    }
    function getSessionStorage() {
        setUserid(sessionStorage.getItem("id"))
        console.log(userId)
        setLoggedIn(sessionStorage.getItem("loggedIn"))
        console.log(loggedIn)
        getUserData(userId)
    }
    function sharePortfolio() {
        let Info = {
            "portfolioName": portfolioName,
            "friendId": friendChatid,
            "uid": userId
        };
        fetch('/sharePortfolio', {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify(Info)
        }).then(res => res.json()).then(
            data => {
                if (data.returncode != 0) {
                    setshareFailString("Portfolio not found")
                } else {
                    setshareFailString("Portfolio shared")
                }
            }
        )
    }

    function deleteFriend() {
        let Info = {
            "friendId": friendChatid,
            "uid": userId
        };
        fetch('/deleteFriend', {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify(Info)
        }).then(res => res.json()).then(
            data => {
                if (data.returncode != 1) {
                    console.log("uhh")
                }
            }
        )
    }

    function getUserData(gotUserId) {
        let idInfo = {
            "id": sessionStorage.getItem("id")
        };
        fetch('/getFriends', {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify(idInfo)
        }).then(res => res.json()).then(
            data => {
                if (data.returncode === -1) {
                    navigate('/login')
                } else {
 
                    setgotFriend(true)
                    var id = data.friendIds
                    var name = data.friendNames
                    var friendsii = data.friendSize
                    var options = []
                    for (let i = 0; i < friendsii; i++) {
                        var option = {
                            value: id[i],
                            label: name[i]
                        }
                        friendOptions.push(option)
                        options.push(option)
                        console.log(option)
                    }
                    console.log(friendOptions)
                    getFriendOptionss(options)
                    setgotFriend(true)
                }
            }
        ).catch(error => {
            console.error('profile error!', error);
          });
    }
    function addFriend() {
        console.log(otherUsername)
        let idInfo = {
            "userId": sessionStorage.getItem("id"),
            "otherUsername": otherUsername
        };
        fetch('/addFriend', {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify(idInfo)
        }).then(res => res.json()).then(
            data => {
                if (data.returncode === -1) {
                    setaddFriendFailInfo("username not found")
                } else if (data.returncode === -2) {
                    setaddFriendFailInfo("already sent request")
                } else if (data.returncode === 1) {
                    setaddFriendFailInfo("Request sent")
                } else if (data.returncode === 2) {
                    setaddFriendFailInfo("Friend added")
                }
            }
        )
    }
    function getMsgs() {
        let idInfo = {
            "id": sessionStorage.getItem("id")
        };
        fetch('/textGet', {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify(idInfo)
        }).then(res => res.json()).then(
            data => {setTexts(data.msgs)
            console.log(data.msgs)
            console.log(texts)
            }
            
        )
        
    }
    function sendMsgs() {
        let idInfo = {
            "id": sessionStorage.getItem("id"),
            "friendId": friendChatid,
            "msg": chatToSend
        };
        fetch('/textFriend', {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify(idInfo)
        }).then(res => res.json()).then(
            data => {
                if (data.returncode != 1) {
                    setChatFailString("chat failed")
                } else {
                    setChatFailString("chat sent")
                    setChatting(false)
                }
            }
        )
    }
    return (
        
        <div>
        <button onClick={()=>getSessionStorage()}> 
        see Friends</button>
        
        {
            gotFriend && <div>
            {friendRequestsNames}
            {friendNames}
            <Select options={friendOptionss} onChange={chooseFriendId}/>
            <button onClick={()=>getMsgs()}> get Texts</button>
            {texts}
            </div>
            
        }
        {
            setChoseFriend && <div>
            {friendChatname}
            <input type="text" onChange={(e)=>getPortfolioName(e)} placeholder="Enter Portfolio name to share"/>
        {shareFailString}
        <button onClick={()=>sharePortfolio()}> Share portfolio</button>
        <button onClick={()=>deleteFriend()}> Delete Friend</button>
        <button onClick={()=>setChatting(true)}> Open chat</button>    
        
            </div>

            
        
        }
        {
        chatting && <div><input type="text" onChange={(e)=>getChatToSend(e)} placeholder="Enter chat to send"/>
        {chatFailString}
        <button onClick={()=>sendMsgs()}> Send chat</button>
        </div>
        }

        <div>
        <input type="text" onChange={(e)=>getOtherUsername(e)} 
        placeholder="Enter Username to Add"/>
        </div>
        
        <button onClick={()=>addFriend()}> 
        Add Friend</button>
        {addFriendFailInfo}
        
        </div>
    )
};
  

//{userId}
//        {
//            loggedIn?            
//            null:<Navigate to="/login" />
//        }
export default Friend;
