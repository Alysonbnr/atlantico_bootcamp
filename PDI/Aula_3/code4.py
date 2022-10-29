from tensorflow import keras

# Define a Keras sequential model
model = keras.Sequential()

# Define the first dense layer
model.add(keras.layers.____(____, activation='____', input_shape=(784,)))

# Define the second dense layer
____

# Define the output layer
model.add(keras.layers.Dense(____))

# Print the model architecture
print(model.summary())