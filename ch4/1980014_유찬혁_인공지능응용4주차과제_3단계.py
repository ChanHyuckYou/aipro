import numpy as np
import numpy.random as nr

def load_data(filename):
    # 파일에서 데이터를 읽어 numpy 배열로 반환하는 함수
    return np.loadtxt(filename)

def sigmoid(x):
    # 시그모이드 함수를 계산하여 반환
    return 1 / (1 + np.exp(-x))

def classify(X, params):
    # 주어진 파라미터로 데이터를 분류하는 함수
    # X는 데이터, params는 선형 분류기의 파라미터
    return sigmoid(np.dot(X, params[:2]) + params[2])

def calculate_cost(X, y, params):
    # 분류 오류를 계산하는 함수
    # X는 데이터, y는 레이블, params는 선형 분류기의 파라미터
    predictions = classify(X, params)
    errors = np.abs(predictions - y) * np.abs(predictions)
    return np.mean(errors)

def evaluate_population(population, X, y):
    # 개체군의 성능을 평가하는 함수
    # population은 개체군, X는 데이터, y는 레이블
    costs = np.array([calculate_cost(X, y, individual) for individual in population])
    fitness_scores = 1.0 / (1.0 + costs)  # 비용을 기반으로 적합도 점수 계산
    return costs, fitness_scores

# 데이터 로드
salmon_data = load_data("data/salmon_train.rtf")  # 연어 데이터 로드
seabass_data = load_data("data/seabass_train.rtf")  # 농어 데이터 로드

# 레이블 준비: 연어(1), 농어(0)
salmon_labels = np.ones(len(salmon_data))
seabass_labels = np.zeros(len(seabass_data))

# 데이터 합치기 및 레이블 합치기
X = np.vstack((salmon_data, seabass_data))
y = np.concatenate((salmon_labels, seabass_labels))

# 인구 초기화
population_size = 25  # 개체군 크기
population = nr.uniform(low=-1.0, high=1.0, size=(population_size, 3))  # 개체군 초기화

# 성능 평가
costs, fitness_scores = evaluate_population(population, X, y)

# 결과 출력
for index, (cost, fitness) in enumerate(zip(costs, fitness_scores)):
    print(f"인덱스 {index}: 분류 오류율 {cost:.4f}, 적합도 {fitness:.4f}")

# 가장 높은 적합도를 가진 개체 찾기
best_index = np.argmax(fitness_scores)
print(f"\n가장 높은 적합도를 가진 개체의 인덱스: {best_index}, 분류 오류율: {costs[best_index]:.4f}, 적합도: {fitness_scores[best_index]:.4f}")
