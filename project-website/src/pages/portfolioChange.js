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
    const [stockABVS, setStockABVS] = useState([]);
    const [stockids, setStockids] = useState([]);
    const [stockAmount, setStockAmount] = useState([]);
    const [stockPrices, setStockPrices] = useState([]);
    const [stockWeight, setStockWeight] = useState([]);
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
    const datals = []
    const [datalss, setdatalss] = useState(null);
    const [chosenportId, setchosenportId] = useState(null);
    const [showPort, setShowPort] = useState(false)
    function getStockABVS(val) {
      setStockABVS(val)
    }
    function getStockids(val) {
      setStockids(val)
    }
    function getStockAmount(val) {
      setStockAmount(val)
    }
    function getStockPrices(val) {
      setStockPrices(val)
    }
    function getStockWeight(val) {
      setStockWeight(val)
    }
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

      getStockABVS(data.stockABVs)
      getStockids(data.stockids)
      getStockAmount(data.stockAmount)
      getStockPrices(data.stockPrices)
      getStockWeight(data.stockWeight)
      setSelectportFunds(data.funds)
      console.log(data)
      var stocks = [];
      for (let i = 1; i < data[0]; i++) {
        //console.log(stockABVS)
        var stock = {
            abv: data[i].stockABVs,
            id: data[i].stockids,
            amount: data[i].stockAmount,
            price: data[i].stockPrices,
            weight: data[i].stockWeight
        }
        console.log(data)
        let datal = {name: data[i].stockABVs, amount: data[i].stockWeight, fill: '#57c0e8'};
        console.log(1)
        stocks.push(
            stock
        )
        console.log(datal)
        datals.push(datal)
        
    }
    setSelectport(stocks)
    getShowPort(true)
    setdatalss(datals)
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
        getShowBuy(false)
      } else if (data.returncode === "-1") {
        setBuyInfoString("Insufficient funds")
      } else if (data.returncode === "-2") {
        setBuyInfoString("Not valid ABV")
      }
    }
  ).then(
    getportfoliodata(portid)
  )
  }
/*
<select onchange={choosePortId}>
                {portOptions.map((option) => {
                    return <option value = {option.value}> {option.names} </option>
                })}
                </select>
*/
function showportdata() {
  return (

    /*selectport.map((stock) => (
      <p key = {stock.abv}> {stock.abv}{stock.id}{stock.amount}{stock.price}{stock.weight} </p>
  ))*/
  <h1>
          <PieChart className= 'pie1'width={400} height={300}>
          <Legend layout="vertical" verticalAlign="middle" align="right" />
          <Pie data={datalss} dataKey="amount" nameKey="name" cx="50%" cy="50%" outerRadius={50} fill="#fff">
          </Pie>
          </PieChart>
          </h1>
  )
}
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
          showPort &&          
          <h1>
          <PieChart className= 'pie1'width={400} height={300}>
          <Legend layout="vertical" verticalAlign="middle" align="right" />
          <Pie data={datalss} dataKey="amount" nameKey="name" cx="50%" cy="50%" outerRadius={50} fill="#fff">
          </Pie>
          </PieChart>
          </h1>
         
        }
        {<h1>
          <PieChart className= 'pie1'width={400} height={300}>
          <Legend layout="vertical" verticalAlign="middle" align="right" />
          <Pie data={datalss} dataKey="amount" nameKey="name" cx="50%" cy="50%" outerRadius={50} fill="#faf">
          </Pie>
          </PieChart>
          </h1>
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