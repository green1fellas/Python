import tensorflow as tf

# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

string = tf.Variable("this is a string", tf.string)
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.567, tf.float64)

# Rank 1
rank1_tensor = tf.Variable(["Test", "Ok", "tim"], tf.string)
# Rank 2 (Matrix)
rank2_tensor = tf.Variable([["test", "ok"], ["test", "yes"]], tf.string)

# Printing Ranks
print(tf.rank(string))
print(tf.rank(rank1_tensor))
print(tf.rank(rank2_tensor))

# Printing Shapes
print(string.shape)
print(rank1_tensor.shape)
print(rank2_tensor.shape)

# Reshape

# .ones populates entire tensor w/ 1's
tensor1 = tf.ones([1,2,3])
print(tensor1)
tensor2 = tf.reshape(tensor1, [2,3,1])
print(tensor2)
# -1 tells the tensor to calculate the size of the dimension in that place
tensor3 = tf.reshape(tensor2, [3, -1])
print(tensor3)



# Reshaping Examples
t = tf.zeros([5,5,5,5])
# print(t)
t = tf.reshape(t, [625])
print(t)
t = tf.reshape(t, [125, -1])
print(t)

