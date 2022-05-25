import sys
import json

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

input_file = open(input_file_name, 'r')
input_file_contents = input_file.read()

output_file = open(output_file_name, 'w')

data = json.loads(input_file_contents)
output = {'immediate_tests': {'matches': [], 'errors': []}, 'delayed_tests': {'matches': [], 'errors': []}}

def record_match(sequence, record):
	matches_count = len(sequence & record)
	errors_count = len(record) - matches_count
	return matches_count, errors_count

for sample in data:
	sequence = set(sample['sequence'].split(' '))

	for immediate_test in sample['immediate_tests']:
		immediate_test = set(immediate_test.split(' '))
		matches, errors = record_match(sequence, immediate_test)
		output['immediate_tests']['matches'].append(matches)
		output['immediate_tests']['errors'].append(errors)

	for delayed_test in sample['delayed_tests']:
		delayed_test = set(delayed_test.split(' '))
		matches, errors = record_match(sequence, delayed_test)
		output['delayed_tests']['matches'].append(matches)
		output['delayed_tests']['errors'].append(errors)

output_text = json.dumps(output)
output_file.write(output_text)