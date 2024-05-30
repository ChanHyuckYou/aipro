import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# MNIST 데이터 로드
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 학습 세트 준비
x_train = x_train[:59000] / 255.0
x_train = x_train.reshape((-1, 28, 28, 1))
y_train = to_categorical(y_train[:59000], 10)

# 검증 세트 준비
x_val = x_train[-1000:] / 255.0
x_val = x_val.reshape((-1, 28, 28, 1))
y_val = to_categorical(y_train[-1000:], 10)

# 평가 세트 준비
x_test = x_test / 255.0
x_test = x_test.reshape((-1, 28, 28, 1))
y_test = to_categorical(y_test, 10)
import os



# 모델 구성
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# 컴파일: Optimizer와 손실 함수, 평가 메트릭을 정의
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 모델 요약 정보 저장
if not os.path.exists('version_1'):
    os.makedirs('version_1')
with open('version_1/model_summary.txt', 'w') as f:
    model.summary(print_fn=lambda x: f.write(x + '\n'))

# 모델 학습
history = model.fit(x_train, y_train, epochs=10, batch_size=128, validation_data=(x_val, y_val))

# 학습 결과 저장
with open('version_1/train_result.txt', 'w') as f:
    f.write(f'Validation loss: {history.history["val_loss"][-1]}\n')
    f.write(f'Validation accuracy: {history.history["val_accuracy"][-1]}\n')

# 모델 저장
model.save('version_1/mnist_model.h5')
