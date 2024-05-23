import tensorflow as tf
# 텐서플로 라이브러리 안에 들어 있는 MNIST 데이터세트
mnist = tf.keras.datasets.mnist
# x_train: 학습 데이터 세트 특징
# y_train: 학습 데이터 세트 레이블
# x_test: 학습 데이터 세트 특징
# y_test: 학습 데이터 세트 레이블
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 데이터 세트 구조 출력
print('학습샘플의수 :', x_train.shape[0]) # 0번째 차원이 샘플 수
print('학습샘플의특징차원 :', x_train.shape[1:]) # 1번째부터의 차원이 특징 차원
print('학습샘플의레이블차원 :', y_train.shape[1:]) # 1번째부터의 차원이 레이블 차원 (스칼라값이
print('학습샘플하나의특징예시 :', x_train[0]) # 0번째 학습 샘플의 특징 확인
print('학습샘플하나의레이블예시 :', y_train[0]) # 0번째 학습 샘플의 레이블 확인
