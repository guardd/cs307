import React from "react";
import {render} from "react-dom";
import './portfolio.css';
import { PieChart, Pie, Legend, LineChart, CartesianGrid, XAxis, YAxis, Tooltip, Line} from 'recharts';
import {useEffect, useState} from "react";
import { Navigate, renderMatches, useNavigate } from "react-router-dom";

const stockData = [
  {
    "date": "2022-06-10",
    "close": 235.1566619873047
  },
  {
    "date": "2022-06-13",
    "close": 223.1666717529297
  },
  {
    "date": "2022-06-14",
    "close": 218.2866668701172
  },
  {
    "date": "2022-06-15",
    "close": 220.9166717529297
  },
  {
    "date": "2022-06-16",
    "close": 222.73666381835938
  },
  {
    "date": "2022-06-17",
    "close": 213.43333435058594
  },
  {
    "date": "2022-06-21",
    "close": 224.60333251953125
  }
]
const projectedData = [
  {
    "date": "2022-06-10",
    "close": 245.1566619873047
  },
  {
    "date": "2022-06-13",
    "close": 215.1666717529297 - 15
  },
  {
    "date": "2022-06-14",
    "close": 210.2866668701172
  },
  {
    "date": "2022-06-15",
    "close": 226.9166717529297
  },
  {
    "date": "2022-06-16",
    "close": 242.73666381835938
  },
  {
    "date": "2022-06-17",
    "close": 223.43333435058594
  },
  {
    "date": "2022-06-21",
    "close": 234.60333251953125
  }
]
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
  const [userId, setUserid]=useState(null)
  const [loggedIn, setLoggedIn]=useState("false")
  const navigate = useNavigate();
  var portNames = []
  var portIds = []
  const [howmanyports, sethowmanyports] = useState(0)
  var stockABVS = []
  var stockids = []
  var stockAmount = []
  var stockPrices = []
  var stockWeight = []
  const result = []
  const [projectData, setprojectData] = useState(null)
  const [projectABV, setprojectABV] = useState(null)
  const [projected, setprojected] = useState(false)

  function getprojectABV(val) {
    setprojectABV(val.target.value)
  }
  //purpose of this function - to call it in the beginning of page load so we will know if we're logged in with who
  function getSessionStorage() {
    setUserid(sessionStorage.getItem("id"))
    console.log(userId)
    setLoggedIn(sessionStorage.getItem("loggedIn"))
    if (loggedIn === false) {
      navigate('/home')
    }
    console.log(loggedIn)
  }
  function getPredictions() {
    console.log("functionCalled")
    console.log(projectABV)

    let predictionInfo = {
      "projectABV": projectABV
    };
    fetch('/getPredictions', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(predictionInfo)
  }).then(res=>res.json()).then(
    data => {
      //console.log(data);
      for (let i = 0; i < 692; i++) {
        let d = {date: data[i].date,
                close: data[i].close};
        //console.log(d)
        result.push(d)
      }
      console.log(result)
      console.log(stockData)
      setprojectData(result)
      setprojected(true)
    }
    
  )
  }
  
  //purpose of this function - getting the portfolio ids and names to show in the dropdown menu
  function getUserPortfolios() {
    let userInfo = {
      "id": sessionStorage.getItem("id")
    };
    fetch('/getUserPortfolios', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(userInfo)
  }).then(res=>res.json()).then(
    data => {
      sethowmanyports(data.size)
      portNames = data.portNames
      portIds = data.portids
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

  return (
    <div class="main">
      <div class="one">
      <h1 className="current-title">Current Porfolio</h1>
      <PieChart className= 'pie1'width={400} height={300}>
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

      {
        
      projected && <div class="two">
      <h1 className="stock-title">Current Stock</h1>
      <LineChart width={400} height={250} data={projectData}
        margin={{ top: 70, right: 10, left: 0, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="close" stroke="#8884d8" />
      </LineChart>
      <h1 className="project-title">Projected Stock</h1>
      <LineChart className= 'graph' width={400} height={250} data={projectedData}
        margin={{ top: 70, right: 10, left: 0, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="close" stroke="#8884d8" />
      </LineChart>
      </div>
      }

      <div class="three">
        <div className="prediction-container"></div>
        <div className="prediction-Form">
          <div className="prediction-content">
            <h1 className="prediction-title">Make a Prediction</h1>
            <div className="prediction-symbol">
              <input type="text"  
              className="prediction-symbol-input" placeholder="Enter Symbol" onChange={getprojectABV}/>
            </div>
            <div className="prediction-button">
              <button onClick= {()=>getPredictions()}> 
              Submit
              </button>
            </div>
          </div>
        </div>
      </div>
      <div>
      <button onClick={()=>navigate('/portfoliochange')}> Edit portfolio </button>
      </div>






    </div>

    

  )
};
//render(<Portfolio />, document.getElementById("root"));
export default Portfolio;
