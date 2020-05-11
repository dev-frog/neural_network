import numpy as np

np.random.seed(0);

X = [[1.0, 2.0, 3.0, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8]]


class Layber_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs,n_neurons)
        self.biases = np.zeros((1,n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.biases

layber1 = Layber_Dense(4, 5)
layber2 = Layber_Dense(5, 2)

layber1.forward(X)
# print(layber1.output)
layber2.forward(layber1.output)
print(layber2.output)
