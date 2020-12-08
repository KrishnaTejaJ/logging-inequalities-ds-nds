# Characterizing Logging in Data Science and Non Data Science Github Repositories

The software engineering applications are known to follow the product quality rigour. Application logging is one of the standard practice to bring software engineering rigour. The logs are used for debugging, testing, execution path analysis and many more use cases.

In the recent times, the data science projects are being integrated into mainstream software engineering applications.  

In this work, we quantitively and qualitatively analyze Logging practices of Data Science and Non-Data Science (Software Engineering) applications.

As Python is considered as the most widely used application in Data Science projects.  We limit the study of Data Science and Non-Data Science to Python based GitHub repos.


## Data
From the data listed in the [source](https://github.com/a2i2/mining-data-science-repositories/tree/master/data), api link and github link of a repo are the only columns used for the purpose of this repository.<br>
Contains both Data Science and Non Data Science repos.

## Input
The input file contains the list of repos of data science and non-data science in csv format, it resides in `data/input` directory.

## Using Semgrep rules
Logs were extracted from the repos using two semgrep rules.
### Log Instances
The [log instances rule](https://semgrep.dev/s/KrishnaTejaJ:log-individual2) is used to extract logs in the following categories
* print
* logging
* traceback
* io
* stderr

`./scripts/logging/log_instances.py` implements the log extraction in the above categories

### Log Level
The [log level rule](https://semgrep.dev/s/KrishnaTejaJ:log-level3) is used to extract logs in the following categories
* class
* method
* info (includes logs of print, logging and io)
* error (includes logs of print and io statements including the word error, stder and logging.error)
* warning (includes logs of print and io statements including the word error, stderr and logging.warning)
* debug (includes logs of logging.debug)
* trace (includes logs of trace and traceback)
* fatal (includes logs of print and io statements including the word fatal)

`./scripts/logging/log_level.py` implements the log extraction in the above categories

### Log Churn
Extracted the code churn of the last 10 commits of data science and non-data science projects to review the improvement in quantity and quality of logs.<br>
`./scripts/logging/logvnlog.py` extracts and categorises Data Science and Non Data Science code churns.

## Output
After applying the Semgrep rules, the following outputs files were generated.

`./scripts/export/final_export.py` outputs `./data/FINAL.csv`<br> 
The output file consists of log instances count, log density, log level count and code churn of all python files in every repository.<br>
This file is used to calculate Gini Index of the repositories to analyze logging inequalities of Data Science and Non-Data Science GitHub repos.

`./scripts/export/gini_index.py` outputs `./data/gini_index.csv`<br>
The output file contains the gini index of the repository, file level (includes log level categories), class level (includes log level categories) and method level (includes log level categories).

`./scripts/export/final_export2.py` outputs `./data/LogMetrics-Summarized.csv`<br>
The output file consists summary of log instances count, log level count, churn and log statements of Data Science and Non-Data Science repositories.


___
