import jax
from jax.experimental import jax2tf
import jax.numpy as jnp

def sum_of_squares(x):
    return jnp.sum(x ** 2)
jax2tf.convert(polymorphic_shapes=None, native_serialization='default', with_gradient=True, fun_jax=sum_of_squares, enable_xla=True, experimental_native_lowering='default', _DefaultNativeSerialization]=DEFAULT_NATIVE_SERIALIZATION, native_serialization_disabled_checks=())
