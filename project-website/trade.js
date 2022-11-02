import React from "react";
import './trade.css';
import { PieChart, Pie, Legend, LineChart, CartesianGrid, XAxis, YAxis, Tooltip, Line } from 'recharts';
import { useEffect, useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";
const Trade = () => {
    const [ExchangeRate, setExchangeRate] = useState(null)
    const [symbol1, setSymbol1] = useState(null)
    const [symbol2, setSymbol2] = useState(null)
    const [base, setBase] = useState(null)
    const [exchangeRateSuccess, setexchangeRateSuccess] = useState(false)
    const [amount,setAmount] = useState(null)
    const navigate = useNavigate();

    

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
                if (data.returncode === "-1") {
                    setexchangeRateSuccess(false)
                    return;
                }
                setExchangeRate(data.exchangeRate);
                setExchangeAmount(data.exchangeAmount)
                console.log(data)
                console.log("Exchange conversion success?" + ExchangeRate + ", " + data.exchangeRate)
                setexchangeRateSuccess(true)
            }
        ).catch(error => {
            console.error('exchange class error', error);
        });
    }
    
    return (
        
        <div class="main">
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
                          onClick={() => getExchangeRate(symbol1,symbol2,base) }                            >
                             Submit
                     </button>
                        </div>
                       
                    <h1>
                            {exchangeRateSuccess?

                                <div className="exchange-rate">
                                    
                                    Exchange Rate: {ExchangeRate}
                                </div>:null} 
                     </h1>
                        </div>
                 </div>
            </div>
            <div class="two">
              <div className="prediction-container"></div>
               <div className="prediction-Form">
                <div className="prediction-content">
                        <h1 className="prediction-title">Top Commodities Rate</h1>

                        <div className="exchange-rate">
                            
                            Commodity1 <br/>
                            Commodity2 <br/>
                            Commodity3 <br/>
                            
                        </div>








                        <div className="prediction-button">
                            <button type="submit" className="prediction-button-button"
                                onClick={() => getExchangeRate(symbol1, symbol2, base)}                            >
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