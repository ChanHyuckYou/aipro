import tensorflow as tf

# MNIST 데이터셋 로드
mnist = tf.keras.datasets.mnist
(x_train, y_train), (_, _) = mnist.load_data()

# 데이터 전처리
x_train = x_train / 255.0
y_train = tf.one_hot(y_train, 10).numpy()

# 모델 정의
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(10, activation='sigmoid')
])

# 모델 컴파일
model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.1, momentum=0.9),
              loss='mean_squared_error',
              metrics=['categorical_accuracy'])

# batch_size와 epochs 정의
batch_size = 1000
epochs = 10

# train_on_batch 사용하여 학습
for epoch in range(epochs):
    for i in range(0, len(x_train), batch_size):
        x_batch = x_train[i:i+batch_size]
        y_batch = y_train[i:i+batch_size]
        model.train_on_batch(x_batch, y_batch)
    print(f'Epoch {epoch+1}/{epochs} 완료')

# 모델 저장
model.save('mnist_model.h5')
