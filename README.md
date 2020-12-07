# Characterizing Logging in Data Science and Non Data Science Github Repositories

With the increased usecases for Data Science in this modern era, it is important to figure out ways so that Data Science projects would adapt smoothly with Non Data Science projects.<br>
For this to happen one of the cruicial steps is to analyse logging in the types of projects and drawing insights from them.
That is the purpose of this repository.

## Data
From the data listed in the [source](https://github.com/a2i2/mining-data-science-repositories/tree/master/data), api link and github link of a repo are the only columns used for the purpose of this repository.<br>
Contains both Data Science and Non Data Science repos.

## Input
The input file is considered in XLSX format with two sheets one for Data Science repos and the other for Non Data Science repos, it resides in `data/input` directory.

## Using Semgrep rules
Logs were extracted from the repos using two semgrep rules.
### Log Instances
The [log instances rule](https://semgrep.dev/s/KrishnaTejaJ:log-individual2) is used to extract logs in the following categories
* print
* logging
* traceback
* io
* stderr

`log_instances.py` in the directory `scripts/logging/` implements the log extraction in the above categories

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

`log_level.py` in the directory `scripts/logging/` implements the log extraction in the above categories

### Log changes
From among the last 10 changes made to the repo, number of changes that belong to Data Science and those that belong to Non Data Science are also extracted.<br>
`logvnlog.py` in the directory `scripts/logging` extracts and categorises Data Science and Non Data Science type changes.

## Output
After applying the log rules the following outputs files are extracted from the JSON files (results of applying log rules).

**FINAL.csv** in the directory `data/`<br>
This output file consists of log instances count, log density, log level count and changes count of each and every python file of all repository.<br>
This file will be used to extract gini index of the repositories which will the key factor in analysing logging of Data Science and Non Data Science github repos.

**gini_index.csv** in the directroy `data/`<br>
This file contains the gini index of the repository, file level (includes log level categories), class level (includes log level categories) and method level (includes log level categories).

**LogMetrics-Summarized.csv** in the directory `data/`<br>
This output file consists of tota log instances count, total log level count, changes made to the repos (last 10) and log statements of a repo.


___
