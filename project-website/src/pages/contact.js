import { stripBasename } from "@remix-run/router";
import React, {useEffect, useState} from "react";
import './contact.css'
const Contact = () => {
  const [name, pushName]=useState(null)
  const [contact, pushContact]=useState(null)
  const [problem, pushProblem]=useState(null)
  const [reportSent, pushReportSent]=useState(false)
  function setName(val) {
    pushName(val.target.value)
  }
  function setContact(val) {
    pushContact(val.target.value)
  }
  function setProblem(val) {
    pushProblem(val.target.value)
  }


  function sendBugReport() {
    let bugInfo = {
      "name": name,
      "email": contact,
      "problem": problem
    };
    fetch('/bugReport', {
      "method": "POST",
      "headers": {"Content-Type": "application/json"},
      "body": JSON.stringify(bugInfo)
    }).then(res => res.json()).then(
      pushReportSent(true)
    )
  }
  
  return (  
    <div className="contact-container">
        <div className="contact-Form">
          <div className="contact-content">
            <h1 className="contact-title">Contact Us</h1>
            <div className="contact-Name">
              <label>Name</label>
              <input type="text" onChange={setName} 
              className="contact-name-input" placeholder="Enter Your Name"/>
            </div>
            <div className="contact-contact">
              <label>Email</label>
              <input type="text" onChange={setContact} 
              className="contact-contact-input" placeholder="Enter Your Email"/>
            </div>
            <div className="contact-problem">
              <label>Problem</label>
              <textarea 
              className="contact-problem-input" placeholder="Enter Problem" rows="4" cols="35" onChange={setProblem}/>
            </div>
            <div className="contact-button">
              <button type="submit" className="contact-button-button" onClick={sendBugReport}> 
              Submit
              </button>
              {
                reportSent?
                <h1>
                bugreport sent!
                </h1>:null
              }
            </div>
          </div>
        </div>
        
        <h1>
          
        </h1>
      </div>
  );
};
  
export default Contact;
