# Notes for Deep Learning

A big thanks to [codebasics](https://www.youtube.com/c/codebasics) for his [deep learning](https://www.youtube.com/watch?v=Mubj_fqiAv8&list=PLeo1K3hjS3uu7CxAacxVndI4bE_o3BDtO
) playlist on youtube.

I curated my own notes for absolute learning. Here I created my own implementations of deep learning key functions and document them for understanding it deeply.

[But what is neural network?](https://www.youtube.com/watch?v=aircAruvnKk&t=990s)

## Key Videos
1. [What is a neuron?](https://www.youtube.com/watch?v=Mubj_fqiAv8&list=PLeo1K3hjS3uu7CxAacxVndI4bE_o3BDtO
)
A neuron is compose of a linear part and an activation part. The linear function receives an input x then passing it to the activation function. The activation function uses the input x and outputs only 2 values. For instance, x to either 0 or 1, *e.g sigmoid function*. Or, x to max(0,x) *e.g. ReLU function*.

2. [Neural Network For Handwritten Digits Classification](https://www.youtube.com/watch?v=iqQgED9vV7k&list=PLeo1K3hjS3uu7CxAacxVndI4bE_o3BDtO&index=7)
Here, he teaches how to use python and keras from tensorflow for building this neural network. It includes, data preparation, flattening, adding layers, what is dense layer, how to compile and how to evaluate the model

## Activation functions
- sigmoid = x => (0 to 1)
- step = x => (0 or 1)
- tanh = x => (-1 to 1)
- relu = x => max(0,x)
- leaky_relu = x => max(0.1x,x)