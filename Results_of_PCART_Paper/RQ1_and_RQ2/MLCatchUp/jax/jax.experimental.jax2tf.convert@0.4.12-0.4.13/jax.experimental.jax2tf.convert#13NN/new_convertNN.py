import jax
from jax.experimental import jax2tf
import jax.numpy as jnp

def sum_of_squares(x):
    return jnp.sum(x ** 2)
jax2tf.convert(sum_of_squares, polymorphic_shapes=None, native_serialization='default', enable_xla=True, native_serialization_platforms=(), with_gradient=True, experimental_native_lowering='default', _DefaultNativeSerialization]=DEFAULT_NATIVE_SERIALIZATION, native_serialization_disabled_checks=())
