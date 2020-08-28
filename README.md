# BACKLOG BUILDER

Backlog Builder is a simple solution for producing a backlog report for organizations of all sizes. The solution is designed to be an addition to an organization's project management toolbox that can produce a backlog report which is:

- _Easy to understand and navigate_. The report should be free of overwhelming and distracting elements in the interface as well as the content, and the organization and presentation of the information should not leave users lost or confused.
- _Comprehensive and transparent_. The data presented should provide the essential elements of a backlog: project time frames, estimated and actual working time (total and remaining), and projected time cost by week, month, or quarter; the analysis pipeline, from raw data to modeled and usable informaiton, should be completely transparent, promoting data integrity and trust in the backlog reporting process.
- _Limitlessly extendable and customizable_. In addition to clear and trustworthy presentation of the core data that makes up the backlog, the reporting tool should be fully customizable, able to be built upon with additional information as needed or desired by those who rely on the backlog report to drive their team's and their organization's success.

Backlog Builder evolved out of a standalone project the author built as an automation script to reduce the time spent calculating a company's[^1] backlog report. This program can be run as a standalone application or configured as an extension for an existing project management solution.

## Required Source Data

Project data can be entered directly into the application if you want to check a project's backlog data in real time. 

For report generation, you can import data from a variety of sources: CSV files, XLSX files, SQL databases, and JSON files are all suitable for getting your project data into the program. Regardless of the data source, the imported data will be converted and stored in JSON format. This makes the data easily accessible to the calculator program (written and Python) and the report display app (written in JavaScript) in a universal format.

## Integration with Existing Tools

An API will be developed for future versions to make integration with existing project management tools as quick and painless as possible. There has not been any work on this, however, and there is no defined timeline on when it will be implemented.


____
[1] The author built this application while working for TractManager, Inc. All proprietary company data has been stripped from this package and the original version of this program, forked to a private repository, remains with TractManager as a private implementation of this tool.