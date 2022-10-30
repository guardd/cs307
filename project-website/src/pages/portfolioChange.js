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
    const [choseportfolio, setChoseportfolio] = useState(false);
    const [selectport, setSelectport] = useState([]);
    const [selectportFunds, setSelectportFunds] = useState(0);
    const [buyInfoString, setBuyInfoString] = useState("");
    const [showBuy, setShowBuy] = useState(false);
    const [buyNameABV, setBuyNameABV] = useState(null)
    const [buyShares, setBuyShares] = useState(null)
    const [chosenportName, setchosenportName] = useState(null)
    var debugMessage = null;
    var newPortFailed = false
    const [chosenportId, setchosenportId] = useState(null);
    const [showPort, setShowPort] = useState(false)

    function getBuyNameABV(val) {
      setBuyNameABV(val.target.value)
    }
    function getBuyShares(val) {
      setBuyShares(val.target.value)
    }
    function getShowPort() {
      setShowPort(true);
    }
    function getShowBuy(val) {
      setShowBuy(val);
    }
    function getNewPortName(val) {
        setNewPortName(val.target.value)
    }

    function getNewPortFunds(val) {
        setNewPortFunds(val.target.value)
    }
    
    function getShowNewPort() {
        setShowNewPort(true)
    }
    function getchosenportId(a) {
      setchosenportId(a)
    }
    function getchosenportName(a) {
      setchosenportName(a)
    }
    function getchoseportfolio(a) {
      setChoseportfolio(a)
    }
    function getPortOptions(val) {
      setPortOptions(val)
    }
 

    //function choosePortId(val) {
    //    chosenportId = val.target.value
    //    console.log(chosenportId)
    //}
     function choosePortId(e) {
      getchosenportId(e.value)
      getchosenportName(e.label)
      getchoseportfolio(true)
      console.log(getchosenportId)
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
        getPortOptions(portOption);
        console.log(portOptions);
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
      setSelectportFunds(data.funds)
      console.log(data)
      var stocks = [];
      for (let i = 0; i < data.size; i++) {
        var stock = {
            ABV: stockABVS[i],
            id: stockids[i],
            amount: stockAmount[i],
            price: stockPrices[i],
            weight: stockWeight[i]
        }
        console.log(1)
        stocks.push(
            stock
        )
        
    }
    setSelectport(stocks)
    getShowPort(true)
    }
    )  
  }

  function buyStock(portid, nameABV, shares) {
    let buyInfo = {
      "uid": userId,
      "id": portid,
      "nameABV": nameABV,
      "shares": shares
    };
    fetch('/buyStock', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(buyInfo)
  }).then(res=>res.json()).then(
    data => {
      if (data.returncode === "1") {
        setBuyInfoString("Stock Bought")
        getShowBuy("false")
      } else if (data.returncode === "-1") {
        setBuyInfoString("Insufficient funds")
      } else if (data.returncode === "-2") {
        setBuyInfoString("Not valid ABV")
      }
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
            <Select options={portOptions} onChange={choosePortId}/>
            :null

        }
        {
          choseportfolio?
          <button onClick={()=>getportfoliodata(chosenportId)}> See portfolio </button>
          :null
        }
        {
          showPort?
          <h1>funds: {selectportFunds}</h1>
          :null
        }
        {
          showPort?          
          selectport.map(({ABV, id, amount, price, weight}) => (
            
            <p key = {ABV}>{ABV}{id}{amount}{price}{weight}</p>
          ))

          :null
        }
        {
          showPort?
          <button onClick={()=>getShowBuy(true)}> buy stock </button>
          :null
        }
         <h1>
         {buyInfoString}
         </h1>
        {
          showBuy?
          <div>
          Stock ABV:<input type="text" onChange={getBuyNameABV} 
          placeholder="Enter Stock Abreviation"/>
          Shares:<input type="text" onChange={getBuyShares} 
          placeholder="Enter # of Shares"/>
          <button onClick={()=>buyStock(chosenportId, buyNameABV, buyShares)}>Buy confirm</button>
          </div>
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