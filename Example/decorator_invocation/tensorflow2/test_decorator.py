import tensorflow as tf
from tensorflow.python.util import dispatch

class MyTensor(tf.experimental.ExtensionType):
    values: tf.Tensor
    metadata: str

@dispatch.dispatch_for_api(tf.math.add)
def add_my_tensor(x: MyTensor, y: MyTensor, name=None):
    return MyTensor(x.values + y.values, metadata="added")

a = MyTensor(tf.constant([1, 2]), "tensor_a")
b = MyTensor(tf.constant([3, 4]), "tensor_b")
c = tf.math.add(a, b)  # Call add_my_tensor
print(c.values)  # Output: [4, 6]
