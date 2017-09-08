#!/usr/bin/env python

import numpy as np
from sklearn.ensemble import RandomForestClassifier

# learninig data
data_training = np.loadtxt('data/train-images.txt', delimiter=' ')
label_training = np.loadtxt('data/train-labels.txt')

# test data
data_test = np.loadtxt('data/test-images.txt', delimiter=' ')
label_test = np.loadtxt('data/test-labels.txt', delimiter=' ')

# learn
#estimator = LinearSVC(C=1.0)
estimator = RandomForestClassifier()
estimator.fit(data_training, label_training)

# test
print(estimator.score(data_test, label_test))
