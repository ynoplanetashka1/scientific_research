import numpy as np
from scipy.spatial import distance


def vectors_to_displacements(vectors):
	x_array, y_array = vectors[:, 0], vectors[:, 1]
	x_mean, y_mean = np.mean(x_array), np.mean(y_mean)
	center = np.array([x_mean, y_mean]);
	distances = np.empty(vectors.size)
	for index, vector in enumerate(vectors):
		distances[index] = distance.euclidean(vector, center)

	return distances