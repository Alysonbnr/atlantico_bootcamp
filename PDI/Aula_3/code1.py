from tensorflow import reshape , matmul, reduce_sum

model = [[ 1. , 0., -1.]]

letterK = [[1., 0., 1.],
           [1., 1., 0.],
           [1., 0., 1.]]
letterX = [[1., 0., 1.],
           [0., 1., 0.],
           [1., 0., 1.]]
# Reshape model from a 1x3 to a 3x1 tensor
model = reshape(model, (3, 1))

# Multiply letter K by model
output1 = matmul(letterK , model)

# Sum over output and print prediction using the numpy method
prediction1 = reduce_sum(output1)
print(prediction1.numpy())

# Multiply letter X by model
output2 = matmul(letterX, model)

# Sum over output and print prediction using the numpy method
prediction2 = reduce_sum(output2)
print(prediction2.numpy())