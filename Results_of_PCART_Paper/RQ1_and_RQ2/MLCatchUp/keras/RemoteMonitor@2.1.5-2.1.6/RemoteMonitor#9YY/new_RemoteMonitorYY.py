from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import RemoteMonitor
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(100,)))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
remote_monitor = RemoteMonitor('http://localhost:9000', path='/publish/epoch/end/', field='data', send_as_json=False)
