from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=100))
model.add(Dense(1, activation='sigmoid'))
adam_optimizer = Adam(0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, amsgrad=False)
