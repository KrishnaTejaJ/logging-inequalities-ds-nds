from config import Config
from scripts.operations.file_operations import FileOperations
import os
import glob
import pandas as pd


#To find the instances of each log in a repository
class LogInstances:

	#To create a json for easy repo data fetching
	def csv2json(repo_file):
		data = pd.read_csv(repo_file)
		repo2json = {}
		type = "DataScience"
		for link in data['Repo_Link']:
			if link == "NonDataScience":
				type = "NonDataScience"
			else:
				repo_name = link.split('/')[-1]
				repo2json[repo_name] = {}
				repo2json[repo_name]['Type'] = type
				repo2json[repo_name]['Repo Link'] = link
		FileOperations.json.save_json(repo2json, f"{Config.log_instances}/input/csv[2repo.json")	

	#Applying semgrep rule on all the repos for specific log statement count
	def json2semgrep(jsonfile):
		json_data = FileOperations.json.read_json(jsonfile)	
		semgrep_rule = Config.semgrep_logcount
		for repo_name, type_link in json_data.items():
			os.chdir(f"{Config.root}{Config.repo_data}{type_link['Type']}/")
			os.system(f"git clone {type_link['Repo Link']}")
			os.system(f"semgrep -f {semgrep_rule} {repo_name} --json -o {Config.root}{Config.log_instances}{repo_name}.json")
			
	#For creating a file logcount json
	def semgrep2json():
		os.chdir(f'{Config.root}{Config.log_instances}')
		path = '*.json'
		repo_log_count = {}
		for reponame in glob.glob(path, recursive = True):
			repo_log_count[reponame.split('.')[0]] = {'print' : 0, 'logging' : 0, 'trace-traceback' : 0, 'io-file.write' : 0,  'stderr' : 0}	
			file_logcount = FileOperations.json.read_json(reponame)
			for file_in_repo in file_logcount['results']:
				#for stoping the redundancy of sys.stderr in io and stdrr, """ is to avoid conflict when formatting is used
				if file_in_repo['check_id'] == 'stderr':
					repo_log_count[reponame.split('.')[0]]['io-file.write'] -= 1
				repo_log_count[reponame.split('.')[0]][file_in_repo['check_id']] += 1
		FileOperations.json.save_json(repo_log_count, f"{Config.root}{Config.log_instances}log_count.json")
		os.chdir(Config.root)	
