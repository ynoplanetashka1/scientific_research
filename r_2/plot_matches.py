import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import json
import sys
import vectors_to_displacements

input_file_name = sys.argv[1]

output = None
with open(input_file_name, 'r') as file:
    contents = json.loads(file.read())
    distances_count = len(contents)
    hits_count = len(contents[0]['hits'])

    deviation = np.empty(distances_count)
    distances = np.fromiter((record['distance'] for record in contents), float)

    for index, record in enumerate(contents):
        hits = np.array(record['hits'])
        #print(hits)
        scale_factor = record['scaleFactor']
        rescaled_hits = hits * scale_factor
        #print(rescaled_hits)
        displacements = vectors_to_displacements.vectors_to_displacements(rescaled_hits)
        #print(displacements)
        _std = np.std(displacements)
        deviation[index] = _std
#distances = np.array([0, *list(distances)])
distances = np.array([val for ind, val in enumerate(list(distances)) if ind != 5])
#deviation = np.array([0, *list(deviation)])
deviation = np.array([val for ind, val in enumerate(list(deviation)) if ind != 5])
#quit()
tend_line_poly_coef = np.polyfit(distances, deviation, 2)
tend_line_poly = np.poly1d(tend_line_poly_coef)
tend_line = tend_line_poly(distances)
r, p = scipy.stats.pearsonr(tend_line, deviation)
print(r, p)
print(tend_line_poly_coef)

plt.xlabel('расстояние, м')
plt.ylabel('стандартная девиация, мм')

plt.plot(distances, deviation, 'ro', label='экспериментальные данные')
plt.plot(distances, tend_line, label='аппроксимация многочленом 2-ой степени')
plt.legend()
plt.show()
