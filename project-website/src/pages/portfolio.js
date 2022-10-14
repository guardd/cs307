import React from "react";
import './portfolio.css';
import { PieChart, Pie, Legend} from 'recharts';
const data01 = [
  {name: 'AAPL', amount: 400, fill: '#57c0e8'},
  {name: 'GOOG', amount: 700, fill: "#FF6565"},
  {name: 'CAT', amount: 200, fill: "#FFDA83"},
  {name: 'MCD', amount: 1000, fill: "#22e3ac"},
  {name: 'CSCO', amount: 650, fill: "#6745a3"}
];
const data02 = [
  {name: 'Gold', amount: 250, fill: "#ff0095"},
  {name: 'Real Estate', amount: 860, fill: "#d46f59"},
  {name: 'Crypto', amount: 325, fill: "#b2cc1f"}
];
const predictedData01 = [
  {name: 'AAPL', amount: 435, fill: '#57c0e8'},
  {name: 'GOOG', amount: 675, fill: "#FF6565"},
  {name: 'CAT', amount: 400, fill: "#FFDA83"},
  {name: 'MCD', amount: 1045, fill: "#22e3ac"},
  {name: 'CSCO', amount: 800, fill: "#6745a3"}
];
const predictdeData02 = [
  {name: 'Gold', amount: 325, fill: "#ff0095"},
  {name: 'Real Estate', amount: 950, fill: "#d46f59"},
  {name: 'Crypto', amount: 100, fill: "#b2cc1f"}
];
const Portfolio = () => {
  return (
    <div class="main">
      <div class="one">
      <h1 className="current-title">Current Porfolio</h1>
      <PieChart width={400} height={300}>
      <Legend layout="vertical" verticalAlign="middle" align="right" />
      <Pie data={data01} dataKey="amount" nameKey="name" cx="50%" cy="50%" outerRadius={50} fill="#fff">
      </Pie>
      <Pie data={data02} dataKey="amount" nameKey="name" cx="50%" cy="50%" innerRadius={60} outerRadius={80} fill="#fff" label />
      </PieChart>
      <h1 className="projected-title">Projected Portfolio</h1>
      <PieChart width={400} height={300}>
      <Legend layout="vertical" verticalAlign="middle" align="right" />
      <Pie data={predictedData01} dataKey="amount" nameKey="name" cx="50%" cy="50%" outerRadius={50} fill="#fff">
      </Pie>
      <Pie data={predictdeData02} dataKey="amount" nameKey="name" cx="50%" cy="50%" innerRadius={60} outerRadius={80} fill="#fff" label />
      </PieChart>
      </div>


      <div class="two">
      <h1 className="stock-title">Current Stock</h1>
      </div>

      

      <div class="three">
        <div className="prediction-container"></div>
        <div className="prediction-Form">
          <div className="prediction-content">
            <h1 className="prediction-title">Make a Prediction</h1>
            <div className="prediction-historical">
              <input type="text" 
              className="prediction-historical-input" placeholder="# of Historical Days"/>
            </div>
            <div className="prediction-symbol">
              <input type="text"  
              className="prediction-symbol-input" placeholder="Enter Symbol"/>
            </div>
            <div className="prediction-interval">
              <input type="text"  
              className="prediction-interval-input" placeholder="Enter Interval"/>
            </div>
            <div className="prediction-button">
              <button type="submit" className="prediction-button-button"> 
              Submit
              </button>
            </div>
          </div>
        </div>
      </div>

    </div>
  )
};
export default Portfolio;
