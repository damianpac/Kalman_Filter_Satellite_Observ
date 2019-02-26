import random

def mvg_avg(data_set):

    window = 5
    obs = len(data_set)

    if (obs%window != 0):
        x = obs%window
        data_set.pop(random.randint(0, (obs-x)))
    else:
        data_set = data_set

    avg_dataset = []
    window = 5
    j = 1

    while j <= len(data_set):
        cnt = 0
        suma = 0
        for i in data_set[(j - 1):(window + j)]:
            suma = suma + i
            cnt = cnt + 1
            if cnt == window:
                avg_val = suma / window
                avg_dataset.append(avg_val)
        j = j + 1

    return avg_dataset
