from config import Config
from scripts.logging.logging import Logging
from scripts.operations.folderoperations import FolderOperations
from scripts.export import finalexport
from scripts.export import finalexport2
from scripts import gini_index
import os
import csv

#Easing the process of required folder operations
FolderOperations.createFolder([Config.output, Config.repo_data, Config.log_classes_data, Config.datascience, Config.nondatascience, Config.log_instances, Config.log_instances_input, Config.log_level, Config.logvnlog])

os.chdir(Config.data)

#For creating all the output files
with open('FINAL.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(['DataScience/NonDataScience', 'Repo Name', 'Repo Link', 'Instances of Log - Logger', 'Instances of Log - Trace/Traceback', 'Instances of Log -StdErr', 'Instances of Log - Print', 'Instances of Log - IO/File.write', 'FileName', 'Log Density - Lines', 'Log Density - File', 'Log Density - Class', 'Log Density - Method', 'Log Level File - Info', 'Log Level File - Error', 'Log Level File - Warning', 'Log Level File - Debug', 'Log Level File - Trace', 'Log Level File - Fatal', 'Log Level Class - Info', 'Log Level Class - Error', 'Log Level Class - Warning', 'Log Level Class - Debug', 'Log Level Class - Trace', 'Log Level Class - Fatal', 'Log Level Method - Info', 'Log Level Method - Error', 'Log Level Method - Warning', 'Log Level Method - Debug', 'Log Level Method - Trace', 'Log Level Method - Fatal', 'DataScience Related Changes', 'Non DataScience Related Changes', 'Line and Log'])

with open('LogMetrics-Summarized.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(['Repo Type', 'Repo Name', 'Repo Link', 'Number of Lines', 'Logging', 'Trace-Traceback', 'Stderr', 'Print', 'io-file.write', "DataScience Changes/Total Changes", "Actual Changed Log lines", "Files Count", 'Total Classes', 'Total Method', 'Total Debug type', 'Total Info Type', 'Total Warning Type', 'Total Error Type', 'Total Fatal type', 'Total Trace type', "Actual Log Lines"])

with open('gini_index.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(['Type of Repo', 'Repo Name', 'Repo GiniIndex', 'File GiniIndex', 'Class GiniIndex', 'Method GiniIndex', 'File GiniIndex Info', 'File GiniIndex Error', 'File GiniIndex Warning', 'File GiniIndex Debug', 'File GiniIndex Trace', 'File GiniIndex Fatal', 'Class GiniIndex Info', 'Class GiniIndex Error', 'Class GiniIndex Warning', 'Class GiniIndex Debug', 'Class GiniIndex Trace', 'Class GiniIndex Fatal', 'Method GiniIndex Info', 'Method GiniIndex Error', 'Method GiniIndex Warning', 'Method GiniIndex Debug', 'Method GiniIndex Trace', 'Method GiniIndex Fatal'])

os.chdir(Config.root)

#Counting the individual log statements in the repo
Logging.log_instances_()

#To find number of Log based changes and Non Log based changes made to the repo in last 10 versions
Logging.logvnonlog_()

#For extracting log level based information
Logging.log_level_()

#For the final excel sheet with all the logging data
finalexport.finalcalc()
finalexport2.finalcalc()

#For extracting all the gini values of the repositories on method, class and file level for various logging types
gini_index.gini_input(Config.final)
