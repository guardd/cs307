import React from "react";
import {render} from "react-dom";
import './portfolio.css';
import { PieChart, Pie, Legend, LineChart, CartesianGrid, XAxis, YAxis, Tooltip, Line} from 'recharts';
import {useEffect, useState} from "react";
import { Navigate, renderMatches, useNavigate } from "react-router-dom";
import { CSVLink } from "react-csv";
import Alert from '@mui/material/Alert';
import Stack from '@mui/material/Stack';
const headers = [
  { label: "Date", key: "date" },
  { label: "Close", key: "close" }
];

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
  const result2 = []
  const [projectData, setprojectData] = useState(null)
  const [projectABV, setprojectABV] = useState(null)
  const [projected, setprojected] = useState(false)
  const [projectDataFinal, setprojectDataFinal] = useState(null)
  const [newsFeed, setnewsFeed] = useState([])
  const [userHasStocks, setuserHasStocks] = useState(false)
  const [day, setDate] = useState(null)
  const [rec, setRec] = useState(null)
  const [score, setScore] = useState(null)
  const csvreport = {
    data: projectData,
    headers: headers,
    filename: 'stock.csv'
  };
  function getprojectABV(val) {
    setprojectABV(val.target.value)
  }
  function getDate(val) {
    setDate(val.target.value)
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
      "projectABV": projectABV,
      "days": day
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
      //console.log(stockData)
      setprojectData(result)
      setprojected(true)
    }
    
    
  )
  getPredictionsFinal()
  
  }
  
  function getPredictionsFinal() {
    console.log("functionCalled")
    console.log(projectABV)

    let predictionInfo = {
      "projectABV": projectABV
    };
    fetch('/getPredictionsFinal', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(predictionInfo)
  }).then(res=>res.json()).then(
    data => {
      //console.log(data);
      for (let i = 0; i < 139; i++) {
        let d = {date: data[i].date,
                close: data[i].close};
        //console.log(d)
        result2.push(d)
      }
      console.log(result2)
      //console.log(stockData)
      setprojectDataFinal(result2)
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
function getNews() {
        let userInfo = {
            //"uid": sessionStorage.getItem("id")
            "uid": "e37697b8-7f74-4ab9-b762-1665ea269931"
        };
        fetch('/getNews', {
            "method": "POST",
            "headers": { "Content-Type": "application/json" },
            "body": JSON.stringify(userInfo)
        }).then(res => res.json()).then(
            data => {
                if (data.returncode == "-1" || data.number<3) {
                    setuserHasStocks(false)
                }
                else {
                    var newslist = []
                    setuserHasStocks(true)
                    for (let i = 0; i < data.number; i++) {
                        newslist.push(data.stocks[i])
                        newslist.push(data.newstitles[i])
                        newslist.push(data.newspublishers[i])
                        newslist.push(data.newsurls[i])
                    }
                     
                    setnewsFeed(newslist)
                    console.log(data)
                }
            },
        )
}

  return (
    <div class="main">
    
    <div>
                {loggedIn? 
                    
                    <div class="four">
                        <div className="prediction-container"></div>
                        <div className="prediction-Form">
                            <div className="prediction-content">
                                <h1 className="prediction-title">News Feed</h1>
                                <div className="prediction-symbol" >
                                    
                                    
                                    {userHasStocks ?
                                        <div className= "five">
                                            {newsFeed[0]}<br />
                                                         <br />
                                            {newsFeed[1]}<br />
                                            {newsFeed[2]}<br />
                                            {newsFeed[3]}<br />
                                                         <br />
                                            {newsFeed[4]}<br />
                                                         <br />
                                            {newsFeed[5]}<br />
                                            {newsFeed[6]}<br />
                                            {newsFeed[7]}<br />
                                                         <br />
                                            {newsFeed[8]}<br />
                                                         <br />
                                            {newsFeed[9]}<br />
                                            {newsFeed[10]}<br />
                                            {newsFeed[11]}<br />
                                            

                                        </div>:null}
                                </div>
                                <button type="submit" className="prediction-button-button"
                                    onClick={() => getNews()}                            >
                                    Refresh
                                </button>
                            </div>
                        </div>
                    </div>:null}
        </div>
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
      <LineChart className= 'graph' width={400} height={250} data={projectDataFinal}
        margin={{ top: 70, right: 10, left: 0, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="close" stroke="#8884d8" />
      </LineChart>
      <CSVLink {...csvreport}>Export to CSV</CSVLink>
      <Stack sx={{ width: '100%' }} spacing={2}>
      <Alert severity="info">Reccomendation:{rec} </Alert>
      <Alert severity="info">Risk Score:{score} </Alert>
      </Stack>
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
              <input type="text"  
              className="prediction-date-input" placeholder="Enter Number of Historical Days" onChange={getDate}/>
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
