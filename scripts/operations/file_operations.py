import json

#For simplifing the file operations
class  FileOperations:

	class json:

		def save_json(dictionary, fname = 'output.json'):
			with open(fname, "w") as output:  
    				json.dump(dictionary, output)

		def read_json(fname):
			with open(fname) as f:
				data = json.load(f)
			return data
		
	class csv:
		
		def create_csv(fname, header_row):
			with open(fname, 'w', new_line = '') as file:
				writer = csv.writer(file)
				writer.writerow(header_row)
