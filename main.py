from numpy import array, random
from NeuralNet import NeuralNetwork, NeuronLayer

random.seed(1)

layer1 = NeuronLayer(4, 3)
layer2 = NeuronLayer(1, 4)

neuralNet = NeuralNetwork(layer1, layer2)

neuralNet.printWeights()

inputs = array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0, 0, 0]])
outputs = array([[0, 1, 1, 1, 1, 0, 0]]).T

neuralNet.train(inputs, outputs, 60000)

neuralNet.printWeights()

hiddenOutput, output = neuralNet.think(array([1, 1, 0]))
print(output)