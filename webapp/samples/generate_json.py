import json

import_files = [
	{
		'file': 'test.txt',
		'author': 'Human',
		'model': 'human'
	},
	{
		'file': 'seq2seq.txt',
		'author': 'Computer',
		'model': 'seq2seq'
	},
	{
		'file': 'vrae.txt',
		'author': 'Computer',
		'model': 'vrae'
	}
]

output_file_name = 'Poem-db-init-V2.json'

def main():
	documents = []
	for file_config in import_files:
		file_name = file_config['file']
		file_author = file_config['author']
		file_model = file_config['model']

		with open(file_name) as file:
			poem_lines = []
			keyword_lines = []
			for line in file:
				poem_line, keyword_line = line.strip().split('\t')
				poem_lines.append(poem_line)
				keyword_lines.append(keyword_line)

				if len(poem_lines) == len(keyword_lines) == 4:
					poem = {
						'content': poem_lines,
						'keyword': keyword_lines,
						'author': file_author,
						'model': file_model
					}

					documents.append(poem)
					poem_lines = []
					keyword_lines = []


	with open(output_file_name, 'w+') as output_file:
		for document in documents:
			json_str = json.dumps(document)
			print json_str
			output_file.write(json_str + '\n')

if __name__ == '__main__':
	main()