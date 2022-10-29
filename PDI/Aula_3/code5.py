from tensorflow import keras

model = keras.Sequential()

# Define the first dense layer
model.add(keras.layers.Dense(____, ____, ____))

# Apply dropout to the first layer's output
model.add(keras.layers.____(0.25))

# Define the output layer
____

# Compile the model
model.compile('____', loss='____')

# Print a model summary
print(model.summary())