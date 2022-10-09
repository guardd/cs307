import React, {useEffect, useState} from "react";

const BugReport = () => {
  const [report, pushReport] = useState(null)
  return (
    <div className="bugReport-container">
			<form className="bugReport-form">
				<div className="bugReport-content">
					<h1 className="bugReport-title">Sign Up</h1>
					<div className="bugReport-report">
						<label>report</label>
						<input type="text" onChange={pushReport}
						className="bugReport-report-input" placeholder="Enter Bug Report"/>
					</div>
					<div className="bugReport-button">
						<button type="submit" className="bugReport-button-button">
						BugReport
						</button>
					</div>
				</div>
			</form>
			<h1>
			</h1>
		</div>
	);
};

export default BugReport;
