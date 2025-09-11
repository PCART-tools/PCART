import tensorflow as tf
from tensorflow.keras.layers import Layer
from tensorflow.keras.utils import register_keras_serializable

@register_keras_serializable(package="MyLayers")
class CustomLayer(Layer):
    def __init__(self, units=32, **kwargs):
        super().__init__(**kwargs)
        self.units = units
    
    def build(self, input_shape):
        self.w = self.add_weight(shape=(input_shape[-1], self.units))
    
    def call(self, inputs):
        return tf.matmul(inputs, self.w)
    
    def get_config(self):
        config = super().get_config()
        config.update({"units": self.units})
        return config

model = tf.keras.Sequential([CustomLayer(10, input_shape=(5,))]) 
model.compile(optimizer="adam", loss="mse")

model.save("custom_model.keras")

loaded_model = tf.keras.models.load_model("custom_model.keras")
print(loaded_model.summary())
