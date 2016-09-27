"""
Perceptron written by Python

This is a slightly different version of this https://blog.dbrgn.ch/2013/3/26/perceptrons-in-python/
"""

from random import choice
import numpy as np

unit_step = lambda x: 0 if x < 0 else 1

training_data = [
    (np.array([0,0,1]), 0),
    (np.array([0,1,1]), 1),
    (np.array([1,0,1]), 1),
    (np.array([1,1,1]), 1),
]

w = np.random.rand(3)
print w

errors = []
eta = 0.2
n = 100

for i in xrange(n):
    x, expected = choice(training_data)
    result = np.dot(w, x)
    error = expected - unit_step(result)
    errors.append(error)
    w += eta * error * x

for x, _ in training_data:
    result = np.dot(x, w)
    print("{}: {} -> {}".format(x[:2], result, unit_step(result)))
