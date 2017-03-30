from numpy import array, random
from NeuralNet import NeuralNetwork, NeuronLayer

random.seed(1)

layer1 = NeuronLayer(3, 2)
layer2 = NeuronLayer(2, 3)

neuralNet = NeuralNetwork(layer1, layer2)

#neuralNet.printWeights()

inputs = array([[0, 0], [0, 1], [1, 1]])
outputs = array([[0,0], [0, 1], [1, 0]])
print(outputs)
neuralNet.train(inputs, outputs, 60000)

#neuralNet.printWeights()

hiddenOutput, output = neuralNet.think(array([1, 0]))
print(output)