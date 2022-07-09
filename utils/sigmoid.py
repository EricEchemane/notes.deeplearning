def sigmoid(n: int):
    'Sigmoid function is an activation function where it outputs only 2 values. It converts input x to either of the two values'
    return 1 / (1+2.71828**-n)

n = sigmoid(0.042 * 42 - 1.53)

print(n)