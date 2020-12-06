from config import Config
from scripts.operations.file_operations import FileOperations
import os
import glob
import re
			


#For finding out the number of Log related changes and Non Log related changes from the last 10 changes of the repos
class LogVsNlog:

	#Git log helps in extracting the entire changes in one go
	def gitchanges():
		paths = [f"{Config.datascience}*/", f"{Config.nondatascience}*/"]
		for path in paths:
			for folder in glob.glob(path, recursive = True):
				reponame = folder.split('/')[-2]
				os.system(f"git --git-dir={folder}.git log -10 -p '*.py' | grep '^[+-]' | grep -Ev '^(--- a/|\+\+\+ b/)'> {Config.logvnlog}{reponame}.txt")

	#changes json for adding the data to the final format
	def changesjson():
		path = f"{Config.logvnlog}*.txt"
		logvsnlog_changes = {}
		for repo_changes in glob.glob(path, recursive=True):
			log_lines = []
			total_lines, logc = 0, 0
			name = repo_changes.split('/')[-1]
			with open(repo_changes) as rc:
				for line in rc:
					total_lines += 1
					temp_line = line[1:].strip()
					if len(temp_line)!=0:
						regexList = ['^print', 'io\.', '^trace\.', '^traceback\.', 'logging\.', '^sys\.stderr\.write', '.*\.write']
						for regex in regexList:
							s = re.search(regex,temp_line)
							if s:								
								log_lines.append(temp_line)
								logc += 1
								break
			logvsnlog_changes[name.split('.')[0]] = {'logchanges' : logc, 'nonlogchanges' : total_lines-logc, 'log_lines' : log_lines}
		FileOperations.json.save_json(logvsnlog_changes, f"{Config.root}{Config.logvnlog}logvsnlog_changes.json")
