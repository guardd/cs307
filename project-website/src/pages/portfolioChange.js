import React from "react";
//import './portfolioChange.css';
import { PieChart, Pie, Legend, LineChart, CartesianGrid, XAxis, YAxis, Tooltip, Line} from 'recharts';
import {useEffect, useState} from "react";
import { Navigate, useNavigate } from "react-router-dom";
import Select from 'react-select';

const PortfolioChange = () => {
    const upDownMenu = [{value: 1, label: "up"}, {value: 0, label: "down"}]
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
    const [sellInfoString, setSellInfoString] = useState("");
    const [listInfoString, setListInfoString] = useState("");
    const [showBuy, setShowBuy] = useState(false);
    const [showSell, setShowSell] = useState(false);
    const [buyNameABV, setBuyNameABV] = useState(null)
    const [sellNameABV, setSellNameABV] = useState(null)
    const [buyShares, setBuyShares] = useState(null)
    const [sellShares, setSellShares] = useState(null)
    const [chosenportName, setchosenportName] = useState(null)
    const [portfolioChangeMessage, setportfolioChangeMessage] = useState(null)
    var debugMessage = null;
    var newPortFailed = false
    const datals = []
    const [datalss, setdatalss] = useState(null);
    const [chosenportId, setchosenportId] = useState(null);
    const [showPort, setShowPort] = useState(false)
    const [showPercentageChangeList, setShowPercentageChangeList] = useState(false)
    const [percentage, setPercentage] = useState("0")
    const [updown, setUpdown] = useState(1)
    const percentageListResults = []
    const [percentageListResultsUpdate, setPercentageListResultsUpdate] = useState(null)
    const [showPercentageChangeListTable, setShowPercentageChangeListTable] = useState(false)
    const [showTax, setShowTax] = useState(false)
    const [stateABV, setStateABV] = useState(null)
    const [userTotalValue, setUserTotalValue] = useState(null)
    const [userTaxPercent, setUserTaxPercent] = useState(null)
    const [userTaxAmount, setUserTaxAmount] = useState(null)
    const [showTaxFinal, setShowTaxFinal] = useState(false)
    function getShowTaxFinal(val) {
      setShowTaxFinal(val)
    }
    function getUserTaxPercent(val) {
      setUserTaxPercent(val)
    }
    function getUserTaxAmount(val) {
      setUserTaxAmount(val)
    }
    function getUserTotalValue(val) {
      setUserTotalValue(val)
    }
    function getShowTax(val) {
      setShowTax(val)
    }
    function getStateABV(val) {
      setStateABV(val.target.value)
    }
    function getShowPercentageChangeTable(val) {
      setShowPercentageChangeListTable(val)
    }
    function getPercentage(val) {
      setPercentage(val.target.value)
    }
    function getUpdown(val) {
      setUpdown(val)
    }
    function getShowPercentageChangeList(val) {
      setShowPercentageChangeList(val)
    }
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
    function getSellNameABV(val) {
      setSellNameABV(val.target.value)
    }
    function getBuyShares(val) {
      setBuyShares(val.target.value)
    }
    function getSellShares(val) {
      setSellShares(val.target.value)
    }
    function getShowPort() {
      setShowPort(true);
    }
    function getShowBuy(val) {
      setShowBuy(val);
    }
    function getShowSell(val) {
      setShowSell(val);
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

    function chooseUpDown(e) {
      getUpdown(e.value)
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

  function getTax() {

    let userInfo = {
      "amount": userTotalValue,
      "state": stateABV
    };

    fetch('/getTax', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(userInfo)
  }).then(res=>res.json()).then(
    data => {
      console.log(data)
      getUserTaxAmount(data.taxAmount)
      getUserTaxPercent(data.taxPercentage)
      getShowTaxFinal(true)
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
        if (data.returncode === 0) {
          setportfolioChangeMessage("portfolio created")
        } else if (data.returncode === -1){
          setportfolioChangeMessage("duplicate portfolio name")
        }
       
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

      //getStockABVS(data.stockABVs)
      //console.log(stockABVS)
      getStockids(data.stockids)
      getStockAmount(data.stockAmount)
      getStockPrices(data.stockPrices)
      getStockWeight(data.stockWeight)
      setSelectportFunds(data[0].funds)
      setUserTotalValue(data[0].total)
      console.log(data)
      var stocks = [];
      var portStockABVs = []
      for (let i = 1; i < data[0].size; i++) {
        //console.log(stockABVS)
        portStockABVs.push(data[i].stockABVs)
        var stock = {
            abv: data[i].stockABVs,
            id: data[i].stockids,
            amount: data[i].stockAmount,
            price: data[i].stockPrices,
            weight: data[i].stockWeight
        }
        console.log(data)
        let datal = {name: data[i].stockABVs + ": " +data[i].stockAmount + " shares", amount: data[i].stockWeight, fill: data[i].stockColor};
        console.log(1)
        stocks.push(
            stock
        )
        console.log(datal)
        datals.push(datal)
        
    }
    setStockABVS(portStockABVs)
    setSelectport(stocks)
    getShowPort(true)
    setdatalss(datals)
    }
    )  
  }

  function buyStock(portid, nameABV, shares) {
    let buyInfo = {
      "uid": sessionStorage.getItem("id"),
      "id": portid,
      "nameABV": nameABV.toUpperCase(),
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
        getShowBuy(false)
      } else if (data.returncode === "-2") {
        setBuyInfoString("Not valid ABV")
        getShowBuy(false)
      } else if (data.returncode === "-3") {
        setBuyInfoString("Not valid # of shares")
        getShowBuy(false)
      } else if (data.returncode === "-4") {
        setBuyInfoString("Daytrade rejected due to pattern day trader rule")
        getShowBuy(false)
      }
    }
  ).then(
    //getportfoliodata(portid)
  )
  }

  function sellStock(portid, nameABV, shares) {
    let sellInfo = {
      "uid": sessionStorage.getItem("id"),
      "id": portid,
      "nameABV": nameABV.toUpperCase(),
      "shares": shares
    };
    fetch('/sellStock', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(sellInfo)
  }).then(res=>res.json()).then(
    data => {
      console.log(data)
      if (data.returncode === "1") {
        setSellInfoString("Stock Sold")
        getShowSell(false)
      } else if (data.returncode === "-1") {
        setSellInfoString("Insufficient funds")
        getShowSell(false)
      } else if (data.returncode === "-2") {
        setSellInfoString("Not valid #")
        getShowSell(false)
      } else if (data.returncode === "-3") {
        setSellInfoString("Not valid # of shares")
        getShowSell(false)
      } else if (data.returncode === "-4") {
        setSellInfoString("Not valid stockABV")
        getShowSell(false)
      } else if (data.returncode === "-5") {
        setSellInfoString("Daytrade rejected due to pattern day trader rule")
        getShowSell(false)
      }
    }
  ).then(
    //getportfoliodata(portid)
  )
  }
  function getLists() {
    let listInfo = {
      "abvs": stockABVS,
      "percentage": percentage,
      "downup": updown
    };
    console.log(listInfo)
    fetch('/getPercentageList', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(listInfo)
  }).then(res=>res.json()).then(
    data => {
      if (data.size === -1) {
        setListInfoString("Percentage not valid")
      } else if (data.size === -2) {
        setListInfoString("Down / Up not valid")
      } else if (data.size === 0) {
        setListInfoString("No matching stocks")
      } else {
        for (let i = 0; i < data.size; i++) {
          var result = {
            id: i,
            percentage: data.percentages[i],
            abv: data.abvs[i]
          }
          percentageListResults.push(result)
        }
        setPercentageListResultsUpdate(percentageListResults)
        getShowPercentageChangeTable(true)
        getShowPercentageChangeList(false)
        setListInfoString("")
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
          showPort &&          
          <h1>
          <PieChart className= 'pie1'width={400} height={300}>
          <Legend layout="vertical" verticalAlign="middle" align="right" />
          <Pie data={datalss} dataKey="amount" nameKey="name" cx="50%" cy="50%" outerRadius={50} fill="#fff">
          </Pie>
          </PieChart>
          </h1>
         
        }
        
        {
          showPort?
          <button onClick={()=>getShowBuy(true)}> buy stock </button>
          :null
        }
        {
          showPort?
          <button onClick={()=>getShowSell(true)}> sell stock </button>
          :null
        }
        {
          showPort?
          <button onClick={()=>getShowPercentageChangeList(true)}> get percentage change list </button>
          :null
        }
        {
          showPort?
          <button onClick={()=>getShowTax(true)}> get Tax Info </button>
          :null
        }
         <h1>
         {buyInfoString}
         </h1>
         <h1>{sellInfoString}</h1>
         <h1>{listInfoString}</h1>
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
        {
          showSell?
          <div>
          Stock ABV:<input type="text" onChange={getSellNameABV} 
          placeholder="Enter Stock Abreviation"/>
          Shares:<input type="text" onChange={getSellShares} 
          placeholder="Enter # of Shares"/>
          <button onClick={()=>sellStock(chosenportId, sellNameABV, sellShares)}>Sell confirm</button>
          </div>
          :null
        }
        {
          showPercentageChangeList?
          
          <div>
          <div>Get list of stocks that are projected to change more than the percentage</div>
          Percentage:<input type="text" onChange={getPercentage} 
          placeholder="0"/>
          Updown:
          <Select options={upDownMenu} onChange={chooseUpDown} defaultValue={{label: "up", value: 1}}/>

          <button onClick={()=>getLists()}>Get Lists</button>
          </div>
          :null
        }
        {portfolioChangeMessage}
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
        {
          showPercentageChangeListTable?
          <div>
            <table>
            <thead>
              <tr>
                <th>Entry #</th>
                <th>Stock ABV</th>
                <th>Percentage Change</th>
              </tr>
            </thead>
            <tbody>
              {percentageListResultsUpdate && percentageListResultsUpdate.map(result =>
                <tr key={result.id}>
                  <td>{result.id}</td>
                  <td>{result.abv}</td>
                  <td>{result.percentage}</td>
                </tr>
              )}
            </tbody>
            </table>
          </div>
          :null
        }
        {
          showTax?
          <div>
          State ABV:<input type="text" onChange={getStateABV} 
          placeholder="Enter State Abbreviation"/>
          <button onClick={()=>getTax()}>Get Tax</button>
          </div>
          :null
        }
        {
          showTaxFinal?
          <div>
          <h1>Tax Percentage: {userTaxPercent}</h1>
          <h1>Tax Amount: {userTaxAmount}</h1>
          </div>
          :null
        }
    </div>
  )
}

export default PortfolioChange;