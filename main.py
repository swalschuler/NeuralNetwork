from numpy import array, random, append, empty
from os import chdir, listdir
from NeuralNet import NeuralNetwork, NeuronLayer

def train_file(file, just_think=False):
    outputs = 0
    this_input = empty((0, 0), int)
    with open(file) as inf:
        output = int(inf.readline().strip('\n'))
        content = inf.readlines()

        for line in content:
            for char in line:
                if char != '\n':
                    this_input = append(this_input, array([int(char)]))

    inputs = array([this_input])
    outputs = array([[output]])
    if not just_think:
        NEURAL_NET.train(inputs, outputs, 1)
    else:
        hiddenOutput, answer = NEURAL_NET.think(inputs)
        #print(answer)
        return answer, output # This seems backwards, but "answer" is
                              # the network's response, and output is the correct answer

def test_all_files():
    files = listdir()

    for file in files:
        print(file)
        networkAnswer, correctAnswer = train_file(file, True)
        networkAnswer = networkAnswer[0][0]
        print("Network response: {:6} ({:.2e})"
              .format("CIRCLE" if networkAnswer < .5 else "LINE", networkAnswer))
        print("Correct response: {}".format("CIRCLE" if correctAnswer < .5 else "LINE"))

        if ((networkAnswer < .5 and correctAnswer < .5)
                or (networkAnswer > .5 and correctAnswer > .5)):
            correct = "correct"
        else:
            correct = "incorrect"

        if networkAnswer > .5:
            if networkAnswer > .8:
                level_of_certainty = "high"
            else:
                level_of_certainty = "low"
        else:
            if 1 - networkAnswer > .8:
                level_of_certainty = "high"
            else:
                level_of_certainty = "low"


        print("The network was {} with {} certainty".format(correct, level_of_certainty))


def train_all_files():
    files = listdir()

    for file in files:
        train_file(file)


random.seed(1)

IMAGE_HEIGHT = 15
IMAGE_WIDTH = 15

# (number neurons, number of inputs per neuron)
LAYER1 = NeuronLayer(int(IMAGE_HEIGHT * IMAGE_WIDTH / 2), IMAGE_HEIGHT * IMAGE_WIDTH)
LAYER2 = NeuronLayer(1, int(IMAGE_HEIGHT * IMAGE_WIDTH / 2))

NEURAL_NET = NeuralNetwork(LAYER1, LAYER2)

chdir("./newEncodings")
for i in range(0, 400):
    if i % 100 == 0:
        print(i)
    train_all_files()

chdir("../tests")
test_all_files()
# train_file("l14.txt", True)
# train_file("c14.txt", True)