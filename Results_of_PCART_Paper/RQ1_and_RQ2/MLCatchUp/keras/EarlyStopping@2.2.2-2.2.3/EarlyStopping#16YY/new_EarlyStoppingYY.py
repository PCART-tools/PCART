from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(100,)))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
early_stopping = EarlyStopping('val_loss', 0, 0, 0, 'auto', restore_best_weights=False)
