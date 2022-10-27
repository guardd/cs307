import React from "react";
//import './portfolioChange.css';
import { PieChart, Pie, Legend, LineChart, CartesianGrid, XAxis, YAxis, Tooltip, Line} from 'recharts';
import {useEffect, useState} from "react";
import { Navigate, useNavigate } from "react-router-dom";
import Select from 'react-select';

const PortfolioChange = () => {

    const [userId, setUserid]=useState(null)
    const [loggedIn, setLoggedIn]=useState("false")
    const navigate = useNavigate();
    const [showNewPort, setShowNewPort] = useState(false)
    const [newPortName, setNewPortName] = useState(null)
    const [newPortFunds, setNewPortFunds] = useState(null)
    var portNames = []
    var portIds = []
    const [howmanyports, sethowmanyports] = useState(0)
    var stockABVS = []
    var stockids = []
    var stockAmount = []
    var stockPrices = []
    var stockWeight = []
    const [portOptions, setPortOptions] = useState([]); 
    const [gotportfolios, setGotportfolios] = useState(false);
    var debugMessage = null;
    var newPortFailed = false
    var chosenportId;

    function getNewPortName(val) {
        setNewPortName(val.target.value)
    }

    function getNewPortFunds(val) {
        setNewPortFunds(val.target.value)
    }
    
    function getShowNewPort() {
        setShowNewPort(true)
    }
 

    //function choosePortId(val) {
    //    chosenportId = val.target.value
    //    console.log(chosenportId)
    //}
    var choosePortId = e => {
      chosenportId = e.value
    }
  
    //purpose of this function - to call it in the beginning of page load so we will know if we're logged in with who
    function getSessionStorage() {
      setUserid(sessionStorage.getItem("id"))
      console.log(userId) //DEBUG
      setLoggedIn(sessionStorage.getItem("loggedIn"))
      if (loggedIn === false) {
        navigate('/home')
      }
      console.log(loggedIn)
    }
    //purpose of this function - getting the portfolio ids and names to show in the dropdown menu
    function getUserPortfolios() {
      var portOption = []; 
      let userInfo = {
        "id": sessionStorage.getItem("id")
      };
      console.log(sessionStorage.getItem("id")) // DEBUG
      fetch('/getUserPortfolios', {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify(userInfo)
    }).then(res=>res.json()).then(
      data => {
        sethowmanyports(data.size)
        console.log(data.size) // DEBUG
        portNames = data.portnames
        console.log(portNames) // DEBUG
        portIds = data.portids
        console.log(portIds) // DEBUG
        for (let i = 0; i < data.size; i++) {
            var port = {
                value: portIds[i],
                label: portNames[i]
            }
            console.log(1)
            portOption.push(
                port
            )
            console.log(port)
            console.log(portOption)
        }
        console.log(portOptions) // DEBUG
        setPortOptions(portOption)
        console.log(portOptions) // DEBUG
        setGotportfolios(true);
      }
    )
  }
  function makeNewPortfolio(name, funds) {
    let portInfo = {
      "name": name,
      "id": sessionStorage.getItem("id"),
      "funds": funds
    };
    fetch('/makeNewPortfolio', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(portInfo)
  }).then(res=>res.json()).then(
      data => {
        console.log("portfolio created")
        setShowNewPort(false);
      }
    )
  }
  function getportfoliodata(portid) {
    let portInfo = {
      "id": portid
    };
    fetch('/getPortfolioData', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(portInfo)
  }).then(res=>res.json()).then(
    data => {
      stockABVS = data.stockABVS
      stockids = data.stockids
      stockAmount = data.stockAmount
      stockPrices = data.stockPrices
      stockWeight = data.stockWeight
    }
  )  
  }
/*
<select onchange={choosePortId}>
                {portOptions.map((option) => {
                    return <option value = {option.value}> {option.names} </option>
                })}
                </select>
*/

  return (
    <div>
        <button onClick={()=>getUserPortfolios()}> Edit portfolio </button>
    
        {
            gotportfolios?
            <Select options={portOptions} onchange={choosePortId}/>
               
            :null

        }
        <button onClick={()=>getShowNewPort()}> Make new Portfolio </button>
        {
            showNewPort?
            <div>
            Portfolio name:<input type="text" onChange={getNewPortName} 
             placeholder="Enter New Portfolio Name"/>
            Portfolio funds:<input type="text" onChange={getNewPortFunds} 
             placeholder="Enter New Portfolio Funds"/>
             <button onClick={()=>makeNewPortfolio(newPortName, newPortFunds)}> Make portfolio</button>
             {
                newPortFailed?
                <div>
                {
                    debugMessage
                }
                </div>:null
             }
            </div>:null
        }
    </div>
    
  )
}

export default PortfolioChange;