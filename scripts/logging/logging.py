from config import Config
from scripts.logging.log_instances import LogInstances
from scripts.logging.logvnlog import LogVsNlog
from scripts.logging.log_level import LogLevel


#All the logging methods
class Logging:
	
	def log_instances_():
		#LogInstances.excel2json(Config.repo_file)
		#LogInstances.json2semgrep(Config.excel2repo)
		LogInstances.semgrep2json()

	def logvnonlog_():
		LogVsNlog.gitchanges()
		total_lines = LogVsNlog.changesjson()

	def log_level_():
		LogLevel.semgrep2json()
		LogLevel.finallogeveljson()
		
	
	
