import tensorflow as tf
im1 = tf.image.decode_image(tf.io.read_file('/home/zhang/Packages/tensorflow_file/better_last.png'))
im2 = tf.image.decode_image(tf.io.read_file('/home/zhang/Packages/tensorflow_file/better_last.png'))
tf.shape(im1)
tf.shape(im2)
im1 = tf.expand_dims(im1, axis=0)
im2 = tf.expand_dims(im2, axis=0)
ssim1 = tf.image.ssim(im1, im2, 255, 11, filter_sigma=1.5, k1=0.01, k2=0.03, return_index_map=False)
