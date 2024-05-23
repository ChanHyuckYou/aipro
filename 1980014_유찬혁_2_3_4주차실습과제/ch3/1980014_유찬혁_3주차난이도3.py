import numpy as np


total_count = 0
error_count = 0
parameters = [2.0, -1.0, -180.0]
# 데이터 로드 함수
def load_data(filename):
    lengths = []
    tails = []
    with open(filename, 'r') as file:
        for line in file:
            length, tail = line.strip().split('\t')
            lengths.append(float(length))
            tails.append(float(tail))
    return np.array(lengths), np.array(tails)           #np배열을 이용하여 순차적으로 데이터를 저장한다.

# 데이터 로드
salmon_lengths, salmon_tails = load_data('salmon_train.rtf')
seabass_lengths, seabass_tails = load_data('seabass_train.rtf')

def classify_fish(length, tail, parameters):

    return "salmon" if np.dot(parameters, [length, tail, 1]) > 0 else "seabass" 
    #2*길이 - 꼬리 - 180 > 0이상이라면 salmon 아니라면 seabass

# 연어 데이터 처리
for length, tail in zip(salmon_lengths, salmon_tails):      #zip함수를 이용해 연속되는 데이터 저장
    print(f"body: {length} tail: {tail}")
    result = classify_fish(length, tail, parameters)
    print(f"result: {result}")
    if result != "salmon":                              #연어가 아니라면, 에러 증가
        error_count += 1
    total_count += 1

# 농어 데이터 처리
for length, tail in zip(seabass_lengths, seabass_tails):    
    print(f"body: {length} tail: {tail}")
    result = classify_fish(length, tail, parameters)    #초기파라미터로 계산한 값 가져옴
    print(f"result: {result}")
    if result != "seabass":
        error_count += 1                                #100마리이므로 1씩 증가
    total_count += 1
        

errot_rate = error_count/total_count
print(errot_rate)