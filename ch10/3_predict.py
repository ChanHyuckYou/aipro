import tensorflow as tf
import numpy as np

# 모델 로드
model = tf.keras.models.load_model('mnist_model.h5')

# MNIST 데이터셋 로드
mnist = tf.keras.datasets.mnist
(_, _), (x_test, y_test) = mnist.load_data()

# 사용자 입력
index = int(input("몇 번 테스트 이미지를 인식해 볼까요? (1~10000) "))

# 데이터 전처리
x_test = x_test / 255.0

# 예측
prediction = model.predict(np.expand_dims(x_test[index-1], 0))
predicted_label = np.argmax(prediction)

print(f'{index}번 테스트 이미지는 {predicted_label}입니다.')
