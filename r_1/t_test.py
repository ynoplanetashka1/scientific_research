import sys
import json
import numpy as np
import scipy.stats as stats


input1_file_name = sys.argv[1]
input2_file_name = sys.argv[2]

input1_file = open(input1_file_name, 'r')
input2_file = open(input2_file_name, 'r')

input1_file_text = input1_file.read()
data1 = json.loads(input1_file_text)
input2_file_text = input2_file.read()
data2 = json.loads(input2_file_text)

immediate_matches_1 = np.array(data1['immediate_tests']['matches'])
immediate_matches_2 = np.array(data2['immediate_tests']['matches'])

print(stats.ttest_ind(immediate_matches_1, immediate_matches_2))