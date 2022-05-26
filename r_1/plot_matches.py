import sys
import json
import numpy as np
import matplotlib.pyplot as plt

input_file_name = sys.argv[1]

with open(input_file_name, 'r') as input_file:
	input_file_text = input_file.read()
	data = json.loads(input_file_text)

	immediate_matches = np.array(data['immediate_tests']['matches'])
	immediate_errors = np.array(data['immediate_tests']['errors'])

	mean = np.mean(immediate_matches)
	mean_line = np.full((immediate_matches.size), mean)
	_, plt1 = plt.subplots()
	#_, plt2 = plt.subplots()
	plt1.plot(immediate_matches, 'ro')
	plt1.plot(mean_line)

	#plt2.hist(immediate_matches, bins = 5, alpha = .5)
	#plt2.hist(immediate_errors, bins = 5, alpha = .5)

	plt.show()
