import json
import numpy as np

files_to_merge = ['5_meters_painted.json', '7.5_meters_painted.json', '10_meters_painted.json', '12.5_meters_painted.json', '15_meters_painted.json', '17.5_meters_painted.json', '20_meters_painted.json', '22.5_meters_painted.json', '25_meters_painted.json']
files_count = len(files_to_merge)

output_file_name = 'hits.json'

step = 2.5
distances = np.linspace(5, 5 + step * (files_count - 1), files_count)
output = []
for index, file_name in enumerate(files_to_merge):
    with open(file_name, 'r') as file:
        content = json.loads(file.read())
        distance = distances[index]
        output.append({'scaleFactor': 1, 'distance': distance, 'hits': content})

output_file = open(output_file_name, 'w')
output_content = json.dumps(output)
output_file.write(output_content)

