import random

file = open('data/salmon_train.rtf','r')         #salmon파일 읽기
salmonFileLines = file.readlines()
file.close()

file = open('data/seabass_train.rtf','r')        #seabass파일 읽기
seabassFileLines = file.readlines()
file.close()

a, b, c = 2.0, -1.0, -180.0
T = 100         #
T_min = 0.001   #최종값

while T > T_min:
    correct = 0  # 올바르게 분류된 개수
    totalcount = 0  # 전체 데이터 개수
    a += random.uniform(-0.01, 0.01)            #random함수를 이용하여 -0.01을 더하거나 0.01을 더한다.
    b += random.uniform(-0.01, 0.01)
    c += random.uniform(-10.0, 10.0)
    
    # salmon 파일 처리
    for salmonFileLine in salmonFileLines:
        features = salmonFileLine.strip().split()
        body = float(features[0])
        tail = float(features[1])
        
        if a * body + b *tail + c > 0:      #주어진 수식에 맞다면 salmon으로 저장하고 아니라면 seabass를 저장한다.
            result = 'salmon'
        else: result = 'seabass'

        
        # 데이터 처리 로직은 동일하게 유지
        # 결과가 salmon일 경우만 correct 증가
        if result == 'salmon':
            correct += 1
        totalcount += 1
    
    # seabass 파일 처리
    for seabassFileLine in seabassFileLines:
        features = seabassFileLine.strip().split()
        body = float(features[0])
        tail = float(features[1])
        
        if a * body + b *tail + c > 0:      #주어진 수식에 맞다면 salmon을  result에 저장하고, 아니라면 seabass로 저장한다.
            result = 'salmon'
        else: result = 'seabass'

        
        if result == 'seabass':     #만약에 맞다면 정답률을 증가시키고 total을 1 증가시킨다.
            correct += 1            #정답률을 +=1증가시켜 정답률을 알 수 있다.
        totalcount += 1             #total +=1

    T *= 0.99  # 온도 감소
    print(f"Accuracy at T={T:.5f}f: {correct/totalcount}")  # 정확도 출력


Fcorrect = correct / totalcount
# 최종 정확도 출력
print(f"Final correct: {correct/totalcount}")
print(f"Final Error_Rate : {1-Fcorrect}" )