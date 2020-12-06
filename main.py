from config import Config
from scripts.logging.logging import Logging
from scripts.operations.folderoperations import FolderOperations
from scripts.export import finalexport
from scripts.export import finalexport2
from scripts import gini_index
import os

'''#Easing the process of required folder operations
FolderOperations.createFolder([Config.output, Config.repo_data, Config.log_classes_data, Config.datascience, Config.nondatascience, Config.log_instances, Config.log_instances_input, Config.log_level, Config.logvnlog])'''

#Counting the individual log statements in the repo
#Logging.log_instances_()

#To find number of Log based changes and Non Log based changes made to the repo in last 10 versions
#Logging.logvnonlog_()

#For extracting log level based information
Logging.log_level_()

#For the final excel sheet with all the logging data
finalexport.finalcalc()
finalexport2.finalcalc()

#For extracting all the gini values of the repositories on method, class and file level for various logging types
gini_index.gini_input(Config.final)
