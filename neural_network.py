# Neural Network
# by Noxmain
# -*- coding: utf-8 -*-
import numpy as np

def sigmoid(x):
    for y in range(len(x)):
        try:
            x[y, 0] = 1 / (1 + pow(3, -x[y, 0]))
        except OverflowError:
            x[y, 0] = round(x[y, 0], 10)
            x[y, 0] = 1 / (1 + pow(3, -x[y, 0]))
    return x

class NeuralNetwork:
    def __init__(self, neurons, random=True, silent=False):
        """
        NeuralNetwork(self, neurons, random=True, silent=False)
        Creates a NeuralNetwork.

        Parameters
        ----------
        neurons: list
            Length of the list: number of layers.
            Values of list items: int > 1.
            Contains the neurons of the NeuralNetwork. Each item is a layer with
            [itemvalue] neurons.
        random: bool, optional
            If true (default), the weights will be random when creating the
            NeuralNetwork. Otherwise, every weight will be 0.0.
        silent: bool, optional
            If false (default), the NeuralNetwork will print a message when loading
            or saving.  Otherwise, it will not.
        """

        self.neurons = neurons
        self.silent = silent

        # Set weights
        lastneuron = 0
        self.weights = []

        for neuron in self.neurons:
            if lastneuron != 0:
                x = np.random.rand(neuron, lastneuron) * 2.0 - 1.0
                if not random:
                    for y in range(len(x)):
                        for z in range(len(x[y])):
                            x[y][z] = 0.0
                self.weights.append(x)
            lastneuron = neuron

    def train(self, inputs, targets, learningrate):
        """
        train(self, inputs, targets, learningrate)
        Trains the NeuralNetwork.

        Parameters
        ----------
        inputs: list
            Length of list: number of neurons in the first layer (neurons[0]).
            Values of list items: float between 0.01 and 1.0.
        targets: list
            Length of list: number of neurons in the last layer (neurons[len(neurons) - 1]).
            Values of list items: float between 0.01 and 1.0.
        learningrate: float
            Value: between 0.01 and 1.0.
            Small learningrate: slower learning but more accurate results
            Big learningrate: faster learning but more inaccurate results
        """

        i = np.array(np.asfarray(inputs), ndmin=2).T
        t = np.array(np.asfarray(targets), ndmin=2).T

        o = [i]
        for weight in self.weights:
            i = sigmoid(np.dot(weight, i))
            o.append(i)

        # Calculate errors
        e = [t - i]
        laste = t - i
        for index in range(len(self.weights) - 1):
            e.append(np.dot(self.weights[(len(self.weights) - 1) - index].T, laste))
            laste = np.dot(self.weights[(len(self.weights) - 1) - index].T, laste)

        # Adjust weights
        for index in range(len(self.weights)):
            self.weights[index] += learningrate * np.dot((e[len(e) - (index + 1)] * o[index + 1] * (1.0 - o[index + 1])), o[index].T)

    def query(self, inputs):
        """
        query(self, inputs)
        Query the NeuralNetwork.

        Parameters
        ----------
        inputs: list
            Length of list: number of neurons in the first layer (neurons[0]).
            Values of list items: float between 0.01 and 1.0.

        Returns
        -------
        o: list
            Length of list: number of neurons in the last layer (neurons[len(neurons) - 1]).
            Values of list items: float between 0.01 and 1.0.
            NeuralNetwork outputs.
        """

        i = np.array(np.asfarray(inputs), ndmin=2).T

        for weight in self.weights:
            i = sigmoid(np.dot(weight, i))

        o = []
        for items in i:
            for item in items:
                o.append(item)

        return o

    def save(self, name):
        """
        save(self, name)
        Saves the NeuralNetwork as a .npy file in the same folder as
        this neural_network.py file.

        Parameters
        ----------
        name: string
            Filename: [name].npy
        """

        save = [self.neurons, self.weights]
        np.save(str(name + ".npy"), save)

        if not self.silent:
            print("[NeuralNetwork]: Network \"" + str(name) + "\" with neurons " + str(self.neurons) + " saved!")

    def load(self, name):
        """
        load(self, name)
        Loads the NeuralNetwork from a .npy file in the same folder as
        this neural_network.py file.

        Parameters
        ----------
        name: string
            Filename: [name].npy
        """

        load = np.load(name + ".npy", encoding="latin1", allow_pickle=True)
        self.neurons = load[0]
        self.weights = load[1]

        if not self.silent:
            print("[NeuralNetwork]: Network \"" + str(name) + "\" with neurons " + str(self.neurons) + " loaded!")
