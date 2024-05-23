import numpy as np
import numpy.random as nr

# 데이터 로드 함수 정의
def load_data(filename):
    return np.loadtxt(filename)

# 연어 및 농어 데이터 로드
salmon_train = load_data("data/salmon_train.rtf")
seabass_train = load_data("data/seabass_train.rtf")

# 데이터 확인
print("연어 데이터 특징:", salmon_train[-1])
print("농어 데이터 특징:", seabass_train[-1])

# GA 첫 세대의 개체 랜덤 생성
Population = 25  # 개체군의 크기
# (-1, 1) 범위 내에서 랜덤하게 초기화된 염색체를 가진 개체 생성
chromosomes = nr.uniform(-1, 1, (Population, 3))

# 생성한 개체들의 인덱스와 염색체 출력
for i, chromosome in enumerate(chromosomes):
    print(f"인덱스 {i}: {chromosome}")
