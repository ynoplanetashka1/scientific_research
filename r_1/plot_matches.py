import sys
import json
import numpy as np
import matplotlib.pyplot as plt

input_file_name = sys.argv[1]

def bootstrap(data, sample_size, samples_count):
    data_size = data.size
    result_size = data_size + samples_count
    result = np.empty(result_size)
    result[0:data_size] = data

    for index in range(data_size, result_size):
        sample = np.random.choice(data, sample_size)
        sample_mean = np.mean(sample)
        result[index] = sample_mean

    return result
    
with open(input_file_name, 'r') as input_file:
    input_file_text = input_file.read()
    data = json.loads(input_file_text)

    immediate_matches = np.array(data['immediate_tests']['matches'])
    delayed_matches = np.array(data['delayed_tests']['matches'])

    immediate_mean = np.mean(immediate_matches)
    delayed_mean = np.mean(delayed_matches)

    immediate_std = np.std(immediate_matches)
    delayed_std = np.std(delayed_matches)

    #mean_line = np.full((immediate_matches.size), mean)
    print('immediate_mean=%.2f, delayed_mean=%.2f' % (immediate_mean, delayed_mean))
    print('immediate_std=%.2f, delayed_std=%.2f' % (immediate_std, delayed_std))

    _, plt1 = plt.subplots()
    _, plt2 = plt.subplots()

    plt1.set_xlabel('количество правильных ответов')
    plt1.set_ylabel('участников')
    plt1.set_title('тестирование проведенное сразу')

    plt2.set_xlabel('количество правильных ответов')
    plt2.set_ylabel('участников')
    plt2.set_title('тестирование проведенное через 10 минут')

    immediate_bootstrapped = bootstrap(immediate_matches, 10, int(1e4))
    delayed_bootstrapped = bootstrap(delayed_matches, 10, int(1e4))
    plt1.hist(immediate_bootstrapped, bins = 10)
    plt2.hist(delayed_bootstrapped, bins=10)
    #_, plt2 = plt.subplots()
    #plt1.plot(immediate_matches, 'ro')
    #plt1.plot(mean_line)

    #plt2.hist(immediate_matches, bins = 5, alpha = .5)
    #plt2.hist(immediate_errors, bins = 5, alpha = .5)

    plt.show()
