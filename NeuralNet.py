from numpy import random, dot, exp, array

# Essentially just a matrix with one column per neuron,
# and one row per input to that neuron
class NeuronLayer():

  # Initially, should have random weights between 0 and 1
  # NOTE: NumPy's random can produce an n x m matrix by using random.random((n, m))
  def __init__(self, numNeurons, numInputs):
    self.weights = 2 * random.random((numInputs, numNeurons)) - 1
  
class NeuralNetwork():

  def __init__(self, _layer1, _layer2):
    self.layer1 = _layer1
    self.layer2 = _layer2
  
  # An S shaped function used for normalization because of its 
  # cool derivative characteristics (allows gradient descent)
  def sigmoid(self, x):
    return 1 / (1 + exp(-x))
  
  def sigmoidDerivative(self, x):
    return x * (1 - x)

  def train(self, trainingInputs, trainingOutputs, trainingIterations):
    for i in range(trainingIterations):
      layer1Output, layer2Output = self.think(trainingInputs)

      # How much we need to change the weight depends on how far off it was 
      # (error) and the derivative
      # NOTE: If, the output is a large number, then the network is very confident
      # in that answer. Also, the derivative will be shallow there. So, only change it 
      # a little bit (weighted by the sigmoid)
      layer2Error = trainingOutputs - layer2Output
      layer2Delta = self.sigmoidDerivative(layer2Output) * layer2Error

      # How far off was the second layer? How much of that was a result of the 
      # first layer?
      layer1Error = layer2Delta.dot(self.layer2.weights.T)
      layer1Delta = self.sigmoidDerivative(layer1Output) * layer1Error

      # By multiplying by training inputs, only inputs of "1" will result in
      # updated weights (a little different for layer 2)
      layer1Adjustments = trainingInputs.T.dot(layer1Delta)
      layer2Adjustments = layer1Output.T.dot(layer2Delta)

      self.layer1.weights += layer1Adjustments
      self.layer2.weights += layer2Adjustments


  def printWeights(self):
    print("Layer 1")
    print(self.layer1.weights)
    print("Layer 2")
    print(self.layer2.weights)
      


  def think(self, inputs):
    # To "think", just take the weighted average of the inputs to a neuron
    # Then, normalize it using the sigmoid function.
    layer1Output = self.sigmoid(inputs.dot(self.layer1.weights))
    layer2Output = self.sigmoid(layer1Output.dot(self.layer2.weights))
    return layer1Output, layer2Output

      

  