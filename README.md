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
The [log instances rule](https://semgrep.dev/s/KrishnaTejaJ:log-individual3) is used to extract logs in the following categories
* print
* logging
* traceback
* io
* stderr


```
rules:
- id: print
  pattern: |
    print(...)
  message: |
    Match found print
  fix: |
    
  severity: WARNING

- id: logging
  patterns:
    - pattern-either: 
      - pattern: |
          logging.info(...)
      - pattern: |
          logging.error(...)
      - pattern: |
          logging.warning(...)
      - pattern: |
          logging.debug(...)
      - pattern: |
          logging.critical(...)
  message: |
    Match found logging
  fix: |
    
  severity: WARNING

- id: trace-traceback
  patterns:
    - pattern-either: 
      - pattern: |
          trace.$B(...)
      - pattern: |
          traceback.$C(...)   
  message: |
    Match found trace-traceback
  fix: |

- id: io-file.write
  patterns:
    - pattern-either: 
      - pattern: |
          $D.writelines(...)
      - pattern: |
          $E.write(...)   
  message: |
    Match found io-file.write
  fix: |

- id: stderr
  pattern: |
    sys.stderr.write(...)  
  message: |
    Match found stderr
  fix: |
    
  severity: WARNING
```


`./scripts/logging/log_instances.py` implements the log extraction in the above categories

### Log Level
The [log level rule](https://semgrep.dev/s/KrishnaTejaJ:log_level4) is used to extract logs in the following categories
* class
* method
* info (includes logs of print, logging and io)
* error (includes logs of print and io statements including the word error, stder and logging.error)
* warning (includes logs of print and io statements including the word error, stderr and logging.warning)
* debug (includes logs of logging.debug)
* trace (includes logs of trace and traceback)
* fatal (includes logs of print and io statements including the word fatal)


```
rules:
- id: class_
  pattern: |
    class $A(...):
      ...
  message: |
    Match found for class_
  fix: |

- id: method_
  pattern: |
    def $B(...):
      ... 
  message: |
    Match found for method_
  fix: |

- id: end_line_
  patterns:
    - pattern-regex: '(.*)$'
  message: |
    Match found for end_line_
  fix: |
    
- id: info
  patterns:
    - pattern-either: 
      - pattern: |
          print(...)
      - pattern: |
          logging.info(...)
      - pattern: |
          $C.write(...)
      - pattern: |
          $D.writelines(...) 
  message: |
    Match found for info
  fix: |

- id: error
  patterns:
    - pattern-either: 
      - pattern: |
          print("=~/.*[eE][rR][rR][oO][rR].*/")
      - pattern: |
          $E.writelines("=~/.*[eE][rR][rR][oO][rR].*/")
      - pattern: |
          $F.write("=~/.*[eE][rR][rR][oO][rR].*/")
      - pattern: |
          sys.stderr.write(...)
      - pattern: |
          logging.error(...)  
  message: |
    Match found for error
  fix: |

- id: warning
  patterns:
    - pattern-either: 
      - pattern: |
          print("=~/.*[wW][aA][rR][nN][iI][nN][gG].*/")
      - pattern: |
          logging.warning(...)
      - pattern: |
          $H.writelines("=~/.*[wW][aA][rR][nN][iI][nN][gG].*/")
      - pattern: |
          $I.write("=~/.*[wW][aA][rR][nN][iI][nN][gG].*/")
  message: |
    Match found for warning
  fix: |

- id: debug
  patterns:
    - pattern-either: 
      - pattern: |
          print("=~/.*[dD][eE][bB][uU][gG].*/")
      - pattern: |
          logging.debug(...)
  message: |
    Match found for debug
  fix: |

- id: trace
  patterns:
    - pattern-either: 
      - pattern: |
          trace.$J(...)
      - pattern: |
          traceback.$K(...) 
  message: |
    Match found for trace
  fix: |

- id: fatal
  patterns:
    - pattern-either: 
      - pattern: |
          print("=~/.*[fF][aA][tT][aA][lL].*/")
      - pattern: |
          $L.writelines("=~/.*[fF][aA][tT][aA][lL].*/")
      - pattern: |
          $M.write("=~/.*[fF][aA][tT][aA][lL].*/")
      - pattern: |
          logging.critical(...)
  message: |
    Match found for fatal
  fix: |
```


`./scripts/logging/log_level.py` implements the log extraction in the above categories

### Log Churn
Extracted the code churn of the last 10 commits of data science and non-data science projects to review the improvement in quantity and quality of logs.<br>
`./scripts/logging/logvnlog.py` extracts and categorises Data Science and Non Data Science code churns.

## Output
After applying the Semgrep rules, the following outputs files were generated.

`./scripts/export/final_export.py` outputs `./data/FINAL.csv`<br> 
The output file consists of log instances count, log density, log level count, code churn of all python files in every repository and the log details of a specific python file in a repo.<br>
This file is used to calculate Gini Index of the repositories to analyze logging inequalities of Data Science and Non-Data Science GitHub repos.

`./scripts/export/gini_index.py` outputs `./data/gini_index.csv`<br>
The output file contains the gini index of the repository, file level (includes log level categories), class level (includes log level categories) and method level (includes log level categories).

`./scripts/export/final_export2.py` outputs `./data/LogMetrics-Summarized.csv`<br>
The output file consists summary of log instances count, log level count, churn and log statements of Data Science and Non-Data Science repositories.


___
