# NeuralNetwork
NeuralNetwork is a Python3 module to create, train and test neural networks with mutible layers. To use this module you should know how a neural network works.

# Content
- [How to use](#how-to-use)
- [Installation](#installation)

---

# Installation
After downloading the neural_network.py you can use the module for one project or install it permanently for your Python.

## Install for one project
Just drag the neural_network.py into you project folder and import it by using `import neural_network`.

## Install for all projects
Browse for your Python framework folder and move the file to `Python.framework/Version/3.x/lib/python3.x`. Now you can import this module into every Phyton file by using `import neural_network`

# How to use
After you imported `neural_network` you can create a neural network by using the class `NeuralNetwork`. This class has the parameters `neurons, random=True, silent=False`.
* `neurons: list` Contains the neurons of the NeuralNetwork. Each item is a layer with [itemvalue] neurons. The NeuralNetwork needs at least two layers and one neuron per layer.
* `random: bool` If true (default), the weights will be random when creating the NeuralNetwork. Otherwise, every weight will be 0.0.
* `silent: bool` If false (default), the NeuralNetwork prints a message when loading or saving. Otherwise, it will not.

Example:
```
import neural_network

nn = neural_network.NeuralNetwork([50, 30, 10])
```

---

You can train the neural network by using the function `train`. It has the parameters `inputs, targets, learningrate`.
* `inputs: list` Contains one training iteration data. The length of the list has to be the number of neurons in the first layer. The values have to be betweet 0 and 1.
* `targets: list` Contains the correct ansewrs for the inputs. The length of the list has to be the number of neurons in the last layer. The values have to be betweet 0 and 1.
* `learningrate: float` A smaller learningrate results a slower learning but more accurate results. a larger learningrate results faster learning but more inaccurate results. The value of the learningrate has to be between 0 and 1.

Example:
```
nn.train([0.05, 0.99, 0.95, 0.88, 0.98, 0.46, 0.59, 0.89, 0.54, 0.27, 0.93, 0.37, 0.43, 0.87, 0.59, 0.04, 0.63, 0.7, 0.86, 0.44, 0.9, 0.66, 0.56, 0.2, 0.75, 0.1, 0.07, 0.36, 0.78, 0.39, 0.9, 0.53, 0.66, 0.46, 0.18, 0.75, 0.43, 0.11, 0.1, 1.0, 0.52, 0.39, 0.84, 0.21, 0.9, 0.84, 0.13, 0.83, 0.31, 0.43],
         [0.04, 0.52, 0.33, 0.13, 0.8, 0.19, 0.29, 0.27, 0.69, 0.26],
         0.1)
```

---

After training the neural network, you can test it by using the funtion `query`. It has the parameter `inputs` and returns a list.
* `inputs: list` Contains one training iteration data. The length of the list has to be the number of neurons in the first layer. The values have to be betweet 0 and 1.
* `return` The coutput from the NeuralNetwork.

Example:
```
outputs = nn.query([0.98, 0.58, 0.51, 0.48, 0.12, 0.36, 0.14, 0.61, 0.92, 0.69, 0.73, 0.82, 0.12, 0.88, 0.7, 1.0, 0.75, 0.19, 0.43, 0.45, 0.22, 0.55, 0.47, 0.29, 0.27, 0.06, 0.08, 0.36, 0.82, 0.83, 1.0, 0.03, 0.13, 0.89, 0.6, 0.1, 0.35, 0.32, 0.47, 0.12, 0.72, 0.54, 0.08, 0.06, 0.56, 0.07, 0.83, 0.82, 0.87, 0.76])
```

---

You can save a NeuralNetwork by using the function `save`. If this file already exists, it will be overwritten. The function has the parameter `name`.
* `name: str` The filename of the saved NeuralNetwork. The file will be called [name].npy.

Example:
```
nn.save("nn")
```

---

You can load a saved NeuralNetwork by using the function `load`. By loading a NeuralNetwork the current weights will be overwritten by the loaded ones. The function has the parameter `name`.
* `name: str` The filename of the saved NeuralNetwork. It tries to load the file called [name].npy.

Example:
```
nn.load("nn")
```