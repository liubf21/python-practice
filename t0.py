import tensorflow as tf

# Check TensorFlow version
print("TensorFlow version:", tf.__version__)

# Create a simple TensorFlow computation graph
a = tf.constant(5)
b = tf.constant(10)
c = tf.multiply(a, b)

# Run the computation graph
result = c.numpy()
print("Result:", result)