import tensorflow as tf

# MNIST 데이터셋 로드
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 학습 세트, 검증 세트 준비
x_train, x_valid = x_train[:59000], x_train[59000:]
y_train, y_valid = y_train[:59000], y_train[59000:]

# 데이터 정규화 (0-255 값을 0-1 범위로 스케일링)
x_train, x_valid, x_test = x_train / 255.0, x_valid / 255.0, x_test / 255.0

# 각 데이터 세트의 shape 출력
print("학습 세트 shape:", x_train.shape)
print("검증 세트 shape:", x_valid.shape)
print("평가 세트 shape:", x_test.shape)

# 모델 정의
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)), # 입력층
    tf.keras.layers.Dense(128, activation='relu'), # 첫 번째 은닉층
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax') # 출력층
])

# 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델 요약 출력 및 저장
model.summary()

with open("model_summary.txt", "w") as f:
    model.summary(print_fn=lambda x: f.write(x + '\n'))

# 모델 학습
model.fit(x_train, y_train, epochs=5, validation_data=(x_valid, y_valid))

# 모델 평가
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print("\n테스트 정확도:", test_acc)
