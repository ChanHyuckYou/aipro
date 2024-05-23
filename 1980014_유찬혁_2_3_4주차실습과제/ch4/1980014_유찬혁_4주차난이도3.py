import numpy as np
import numpy.random as nr

def load_data(filename):
    # np.loadtxt 함수를 사용하여 파일에서 데이터를 로드합니다.
    # 이 함수는 텍스트 파일에서 데이터를 불러올 때 유용합니다.
    return np.loadtxt(filename)

# 데이터 로드
salmon_train = load_data("data/salmon_train.rtf")  # 연어 학습 데이터 로드
seabass_train = load_data("data/seabass_train.rtf")  # 농어 학습 데이터 로드

# 데이터 확인
# 마지막 데이터 포인트를 출력하여 데이터가 제대로 로드되었는지 확인합니다.
print("연어 데이터 특징:", salmon_train[-1])
print("농어 데이터 특징:", seabass_train[-1])

Population = 25  # 개체군의 크기 설정
# nr.uniform 함수를 사용하여 -1과 1 사이의 균일 분포에서 무작위 값으로 이루어진 염색체를 생성합니다.
# Population x 3 크기의 배열 생성: 각 행은 개체를, 열은 염색체 값을 나타냅니다.
chromosomes = nr.uniform(-1, 1, (Population, 3))

# 생성한 개체들의 인덱스와 염색체 출력
for i, chromosome in enumerate(chromosomes):
    print(f"인덱스 {i}: {chromosome}")

def classify(features, chromosome):
    # np.dot 함수를 사용하여 특징(features)와 가중치(chromosome[:2])의 점곱을 계산합니다.
    # 이후 임계값(chromosome[2])을 더하여 0 이상이면 1, 미만이면 0으로 분류합니다.
    return np.dot(features, chromosome[:2]) + chromosome[2] >= 0

def calculate_fitness(X, y, chromosome):
    # 예측값을 계산하고, 실제값(y)과 비교하여 분류 오류율을 계산합니다.
    predictions = classify(X, chromosome)
    cost = np.sum(predictions != y) / len(y)  # 오류율 계산
    # 적합도는 오류율의 역수로 계산하여, 적합도가 높을수록 오류율이 낮은 것을 의미합니다.
    return 1.0 / (1.0 + cost), cost

# 학습 데이터 준비
# np.vstack 함수를 사용하여 연어와 농어 데이터를 수직으로 결합합니다.
X_train = np.vstack((salmon_train, seabass_train))
# 연어는 1, 농어는 0으로 라벨링합니다.
y_train = np.array([1] * len(salmon_train) + [0] * len(seabass_train))

# 분류 성능 평가
fitness_scores = []
for i, chromosome in enumerate(chromosomes):
    fitness, cost = calculate_fitness(X_train, y_train, chromosome)
    fitness_scores.append(fitness)

    # 각 개체의 인덱스와 함께 분류 오류율 및 적합도를 출력합니다.
    print(f"인덱스 {i} - 분류 오류율: {cost}, 적합도: {fitness}")

# 최고 적합도를 가진 개체를 찾습니다.
best_index = np.argmax(fitness_scores)
# 가장 높은 적합도를 가진 개체의 인덱스와, 그 때의 분류 오류율 및 적합도를 출력합니다.
print(f"가장 높은 적합도를 가진 개체의 인덱스: {best_index}, 분류 오류율: {1-fitness_scores[best_index]}, 적합도: {fitness_scores[best_index]}")
