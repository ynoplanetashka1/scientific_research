import sys
import json

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

input_file = open(input_file_name, 'r')
input_file_contents = input_file.read()

output_file = open(output_file_name, 'w')

data = json.loads(input_file_contents)
output = []

sequence = set(data['sequence'].split(' '))

for record in data['records']:
	name = record['name']
	immediate_test = set(record['immediate_test'].split(' '))
	if ('' in immediate_test):
		immediate_test.clear()
	delayed_test = set(record['delayed_test'].split(' '))
	if ('' in delayed_test):
		delayed_test.clear()
	immediate_matches_count = len(sequence & immediate_test)
	immediate_error_count = len(immediate_test) - immediate_matches_count
	delayed_matches_count = len(sequence & delayed_test)
	delayed_error_count = len(delayed_test) - delayed_matches_count

	output.append({'name': name, 'immediate_error_count': immediate_error_count, 'immediate_matches_count': immediate_matches_count, 'delayed_error_count': delayed_error_count, 'delayed_matches_count': delayed_matches_count})

output_text = json.dumps(output)
output_file.write(output_text)