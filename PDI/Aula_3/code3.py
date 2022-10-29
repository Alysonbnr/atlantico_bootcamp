from tensorflow import Variable, keras, ones, matmul
borrower_features = [[ 2. , 2., 43.]]

# Define the first dense layer
dense1 = keras.layers.Dense(__, activation='__')(borrower_features)

# Define a dense layer with 3 output nodes
dense2 = ____

# Define a dense layer with 1 output node
predictions = ____

# Print the shapes of dense1, dense2, and predictions
print('\n shape of dense1: ', dense1.shape)
print('\n shape of dense2: ', ____.shape)
print('\n shape of predictions: ', ____.shape)