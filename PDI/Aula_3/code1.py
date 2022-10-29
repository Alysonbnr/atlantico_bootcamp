from tensorflow import reshape , matmul, reduce_sum

model = [[ 1. , 0., -1.]]

letterK = [[1., 0., 1.],
           [1., 1., 0.],
           [1., 0., 1.]]
letterX = [[1., 0., 1.],
           [0., 1., 0.],
           [1., 0., 1.]]
# Reshape model from a 1x3 to a 3x1 tensor
model =___(model, (__, __))

# Multiply letter K by model
output1 = ___(___ , ____)

# Sum over output and print prediction using the numpy method
prediction1 = ___(___)
print(prediction1.numpy())

# Multiply letter X by model
output2 = ___(___, ___)

# Sum over output and print prediction using the numpy method
prediction2 = ___(___)
print(prediction2.numpy())