import React from "react";
import './trade.css';
import { PieChart, Pie, Legend, LineChart, CartesianGrid, XAxis, YAxis, Tooltip, Line } from 'recharts';
import { useEffect, useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";
import Select from 'react-select';
const Trade = () => {
    const [ExchangeRate, setExchangeRate] = useState(null)
    const [symbol1, setSymbol1] = useState(null)
    const [symbol2, setSymbol2] = useState(null)
    const [base, setBase] = useState(null)
    const [exchangeRateSuccess, setexchangeRateSuccess] = useState(false)
    const [validSymbols, setValidSymbols] = useState(false)
    const [validAmount, setValidAmount] = useState(false)
    const [amount, setAmount] = useState(null)
    const [exchangeAmount, setexchangeAmount] = useState(null)
    const [topTenRefresh, settopTenRefresh] = useState(false)
    const [topTenRefreshFail, settopTenRefreshFail] = useState(false)
    const [topTenRates, settopTenRates] = useState([]) 
    const [chosenSortType, setchosenSortType] = useState(false)
    const [chosenSortType2, setchosenSortType2] = useState(false)
    const navigate = useNavigate();
    const [chosenPortID, setchosenPortID] = useState(null)
    const [isIndustry, setisIndustry] = useState(false)
    const [isNotIndustry, setisNotIndustry] = useState(false)
    const [stockABV, setstockABV] = useState([])
    const [stockName, setstockName] = useState([])
    const [stockSortedBy, setstockSortedBy] = useState([])
    const [industryTable, setindustryTable] = useState(null)
    const [chosenOrder, setchosenOrder] = useState(null)
    
    const portOptions = [
        { label: 'Trade Volume', value: '1' },
        { label: 'Market Cap', value: '2' },
        { label: 'Last Sale', value: '3' },
        { label: 'Net Change', value: '4' },
        { label: 'Industry', value: '5'}
    ]
    const portOptions2 = [
        { label: 'asc', value: '1' },
        { label: 'desc', value: '2' }
    ]
    function choosePortId(e) {
        setchosenPortID(e.label)
        setchosenSortType(true)
        
    }
    function chooseOrderID(e) {
        setchosenOrder(e.label)
        setchosenSortType2(true)

    }

    function getSymbol1(val) {
        setSymbol1(val.target.value)
        console.warn(val.target.value)
    }
    function getSymbol2(val) {
        setSymbol2(val.target.value)
        console.warn(val.target.value)
    }
    function getBase(val) {
        setBase(val.target.value)
        console.warn(val.target.value)
    }
    function getAmount(val) {
        setAmount(val.target.value)
        console.warn(val.target.value)
    }
   
    function getExchangeRate(symbol1, symbol2, base, amount) {
        let exchangeInfo = {
            "symbol1": symbol1,
            "symbol2": symbol2,
            "base": base,
            "amount": amount
        };
        fetch('/exchangeRate', {
            "method": "POST",
            "headers": { "Content-Type": "application/json" },
            "body": JSON.stringify(exchangeInfo)
        }).then(res => res.json()).then(
            data => {
                if (data.returncode == "-1") {
                    setexchangeRateSuccess(false)
                    setValidAmount(false)
                    return;
                }
                else if (data.returncode == "0") {
                    setexchangeRateSuccess(false)
                    setValidSymbols(true)
                    setValidAmount(false)
                    return;
                }
                else if (data.returncode == "2") {
                    setexchangeRateSuccess(false)
                    setValidSymbols(false)
                    setValidAmount(true)
                    return;
                }
                else {
                    setValidSymbols(false)
                    setValidAmount(false)
                    setExchangeRate(data.exchangeRate);
                    setexchangeAmount(data.exchangeAmount)
                    console.log(data)
                    console.log("Exchange conversion success?" + ExchangeRate + ", " + data.exchangeRate)
                    setexchangeRateSuccess(true)
                }
            }
        ).catch(error => {
            console.error('exchange class error', error);
        });
    }
    function getTopTen() {
        let exchangeInfo = {
            "symbol1": "WTIOIL",
            "symbol2": "COFFEE",
            "symbol3": "NG",
            "symbol4": "XAU",
            "symbol5": "WHEAT",
            "symbol6": "COTTON",
            "symbol7": "CORN",
            "symbol8": "SUGAR",
            "symbol9": "XAG",
            "symbol10": "XCU"

            
        };
        fetch('/topTenRefresh', {
            "method": "POST",
            "headers": { "Content-Type": "application/json" },
            "body": JSON.stringify(exchangeInfo)
        }).then(res => res.json()).then(
            data => {
                if (data.returncode == "-1") {
                    settopTenRefresh(false)
                    settopTenRefreshFail(true)
                    return;
                }
              
                else {
                    settopTenRefresh(true)
                    settopTenRefreshFail(false)
                    const array = []
                    for (const [key, value] of Object.entries(data.rates)) {

                        array.push(key, value)

                    }
              
                    settopTenRates(array)
                    console.log(data.rates)
                    
                }
            }
        ).catch(error => {
            console.error('Top Ten Refresh error', error);
        });

    }
    function getSortedStocks(chosenPortID,chosenOrder) {
        let sortType = {
            "sortType": chosenPortID,
            "ascdesc": chosenOrder
        };
        fetch('/getSortStock', {
            "method": "POST",
            "headers": { "Content-Type": "application/json" },
            "body": JSON.stringify(sortType)
        }).then(res => res.json()).then(
            data => {
                if (data.returncode == "-1") {
                    setisIndustry(false)
                    setisNotIndustry(false)
                    return;
                }
                else if (data.returncode == "1") {
                    setisIndustry(true)
                    setisNotIndustry(false)
                    setindustryTable(data.topIndustryTable)
                }
                else if (data.returncode == "2") {
                    setisIndustry(false)
                    setisNotIndustry(true)
                    const array = []
                    for (const [key, value] of Object.entries(data.stockABV)) {

                        array.push(key, value)

                    }
                    setstockABV(array)
                    const array1 = []
                    for (const [key, value] of Object.entries(data.stockName)) {

                        array1.push(key, value)

                    }
                    setstockName(array1)
                    const array2 = []
                    for (const [key, value] of Object.entries(data.stockSortedBy)) {

                        array2.push(key, value)

                    }
                    setstockSortedBy(array2)
                    
                    return;
                    
                    

                }
                else {
                    setisIndustry(false)
                    setisNotIndustry(false)
                    return;
                }
            }
        ).catch(error => {
            console.error('Top Ten Refresh error', error);
        });

    }
    return (
        
        <div class="main">
            <div class="one">
            <div className="prediction-container"></div>
            <div className="prediction-Form">
                <div className="prediction-content">
                    <h1 className="prediction-title">Filter Stocks</h1>
                    <div className="prediction-historical">
            <Select options={portOptions} onChange={choosePortId} />
            
            {
                isIndustry?
                    <div className="industry-table">
                        StockABV    Stock Name    Market Cap    Industry <br />
                        <br />
                        {industryTable}
                        
                    </div>:null
            }
            {
                isNotIndustry?
                    <div className="industry-table">
                                        {stockABV[3]}   {stockName[3]}  {stockSortedBy[3]} <br />
                                        {stockABV[5]}   {stockName[5]}  {stockSortedBy[5]} <br />
                                        {stockABV[7]}   {stockName[7]}  {stockSortedBy[7]} <br />
                                        {stockABV[9]}   {stockName[9]}  {stockSortedBy[9]} <br />
                                        {stockABV[11]}   {stockName[11]}  {stockSortedBy[11]} <br />
                                        {stockABV[13]}   {stockName[13]}  {stockSortedBy[13]} <br />
                                        {stockABV[15]}   {stockName[15]}  {stockSortedBy[15]} <br />
                                        {stockABV[17]}   {stockName[17]}  {stockSortedBy[17]} <br />
                                        {stockABV[19]}   {stockName[19]}  {stockSortedBy[19]} <br />
                                        {stockABV[21]}   {stockName[21]}  {stockSortedBy[21]} <br />
                        
                    </div>:null
                            }
            {
                chosenSortType?
                    <h1>
                    <Select options={portOptions2} onChange={chooseOrderID} />        
                                        <div className="prediction-button">
                                            <button className="prediction-button-button" onClick={() => getSortedStocks(chosenPortID, chosenOrder)}> Display Stocks </button> 
                    </div>
                    </h1>: null
            }
                    </div>
                </div>

                </div>
            </div>

           <div class="one">
           <div className="prediction-container"></div>
           <div className="prediction-Form">
              <div className="prediction-content">
                <h1 className="prediction-title">Commodity Exchange Rate</h1>
                <div className="prediction-historical">
                  <input type="text" onChange={getSymbol1}
                  className="prediction-historical-input" placeholder="Commodity Symbol One" />
                  </div>
                  <div className="prediction-symbol">
                    <input type="text"  onChange={getSymbol2}
                       className="prediction-symbol-input" placeholder="Commodity Symbol Two" />
                     </div>
                     <div className="prediction-interval">
                         <input type="text" onChange={getBase}
                             className="prediction-interval-input" placeholder="Conversion Base" />
                     </div>
                     <div className="amount">
                         <input type="text" onChange={getAmount}
                             className="prediction-interval-input" placeholder="Amount" />
                     </div>
                     
                  <div className="prediction-button">
                     <button type="submit" className="prediction-button-button"
                          onClick={() => getExchangeRate(symbol1,symbol2,base,amount) }                            >
                             Submit
                     </button>
                        </div>
                       
                    <h1>
                            {exchangeRateSuccess?

                                <div className="exchange-rate">
                                    
                                    Exchange Rate: {ExchangeRate} <br />
                                    Cost: {exchangeAmount}
                                </div>:null} 
                    </h1>
                    <h1>
                            {validSymbols?

                                <div className="exchange-rate">
                                 Please enter valid symbols   
                                   
                                </div> : null}
                    </h1>
                    <h1>
                            {validAmount?

                                <div className="exchange-rate">
                                 Please enter amount between 1 and 1,000,000,000
                                </div> : null}
                    </h1>
                        </div>
                 </div>
            </div>
            
            <div class="two">
            
              <div className="prediction-container"></div>
               <div className="prediction-Form">
                <div className="prediction-content">
                        <h1 className="prediction-title">Top Commodities </h1>

                            {topTenRefresh?
                            <div className="exchange-rate">
                                WTIOIL: {topTenRates[topTenRates.indexOf("WTIOIL") + 1]}<br />
                                COFFEE: {topTenRates[topTenRates.indexOf("COFFEE") + 1]}<br />
                                NG      {topTenRates[topTenRates.indexOf("NG") + 1]}<br />
                                XAU:    {topTenRates[topTenRates.indexOf("XAU") + 1]}<br />
                                WHEAT:  {topTenRates[topTenRates.indexOf("WHEAT") + 1]}<br />
                                COTTON: {topTenRates[topTenRates.indexOf("COTTON") + 1]}<br />
                                CORN:   {topTenRates[topTenRates.indexOf("CORN") + 1]}<br />
                                SUGAR:  {topTenRates[topTenRates.indexOf("SUGAR") + 1]}<br />
                                XAG:    {topTenRates[topTenRates.indexOf("XAG") + 1]}<br />
                                XCU:    {topTenRates[topTenRates.indexOf("XCU") + 1]}
                                
                                    

                            </div>: null}
                            {topTenRefreshFail?
                            <div className="exchange-rate">


                                Refresh Failed



                            </div> : null}







                        <div className="prediction-button">
                            <button type="submit" className="prediction-button-button"
                                onClick={() => getTopTen()}                            >
                                Refresh
                            </button>
                        </div>
                </div>
                </div>
                
            </div>
                
             </div>
         
              
    );
};
export default Trade;