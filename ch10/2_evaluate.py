import tensorflow as tf

# 모델 로드
model = tf.keras.models.load_model('mnist_model.h5')

# MNIST 데이터셋 로드
mnist = tf.keras.datasets.mnist
(_, _), (x_test, y_test) = mnist.load_data()

# 데이터 전처리
x_test = x_test / 255.0
y_test = tf.one_hot(y_test, 10).numpy()

# 모델 평가
loss, accuracy = model.evaluate(x_test, y_test, verbose=2)
error_rate = 1.0 - accuracy

print(f'테스트 데이터 세트에 대한 오류율은 {error_rate * 100:.2f}% 입니다.')
