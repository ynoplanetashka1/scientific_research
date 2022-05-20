import sys
import json
import numpy as np
import matplotlib.pyplot as plt

input_file_name = sys.argv[1]

with open(input_file_name, 'r') as input_file:
	input_file_text = input_file.read()
	contents = json.loads(input_file_text)
	records_count = len(contents)
	delayed_matches_count = np.array([record['delayed_matches_count'] for record in contents])
	print(delayed_matches_count)
	mean = np.mean(delayed_matches_count)
	mean_line = np.full((records_count), mean)
	_, plt1 = plt.subplots()
	_, plt2 = plt.subplots()
	plt1.plot(delayed_matches_count, 'ro')
	plt1.plot(mean_line)

	plt2.hist(delayed_matches_count, bins = 5)

	plt.show()