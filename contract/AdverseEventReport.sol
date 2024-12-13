// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AdverseEventReport {
    struct Report {
        uint256 id;
        string drugName;
        string adverseEvent;
        string reporter;
        uint256 timestamp;
    }

    Report[] public reports;
    uint256 public reportCount;

    event NewReport(uint256 id, string drugName, string adverseEvent, string reporter, uint256 timestamp);

    function addReport(string memory drugName, string memory adverseEvent, string memory reporter) public {
        reports.push(Report(reportCount, drugName, adverseEvent, reporter, block.timestamp));
        emit NewReport(reportCount, drugName, adverseEvent, reporter, block.timestamp);
        reportCount++;
    }

    function getReports() public view returns (Report[] memory) {
        return reports;
    }
}
