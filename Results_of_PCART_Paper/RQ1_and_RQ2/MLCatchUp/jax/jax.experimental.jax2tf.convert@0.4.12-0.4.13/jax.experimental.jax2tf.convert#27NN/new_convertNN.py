import jax
from jax.experimental import jax2tf
import jax.numpy as jnp

def sum_of_squares(x):
    return jnp.sum(x ** 2)
jax2tf.convert(experimental_native_lowering='default', with_gradient=True, fun_jax=sum_of_squares, polymorphic_shapes=None, enable_xla=True, native_serialization_platforms=(), native_serialization='default', _DefaultNativeSerialization]=DEFAULT_NATIVE_SERIALIZATION, native_serialization_disabled_checks=())
