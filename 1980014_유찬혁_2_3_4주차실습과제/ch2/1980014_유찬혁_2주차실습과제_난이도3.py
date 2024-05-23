fd = open('data/input_data.rtf', 'r')
lines = fd.readlines()
fd.close()                              #변수 저장이 완료되었으므로 닫기
fish_type=""                            #fish type지정
fw = open('data/output_data.rtf','w')        #파일 생성 및 쓰기
for line in lines:                      #line만큼 반복
    newline = line.strip()
    divs = newline.split()
    body = int(divs[0])
    tail = (int(divs[1]))

    
    if body > 81 and tail < 13:                #몸길이가 81이상이고 꼬리길이가 13보다 작으면 농어 아니면 연어
        fish_type = "seabass"
    else:
        fish_type = "salmon"

    fw.write(f"body: {body} tail: {tail} ==> {fish_type}\n")    #파일 작성
    print(f"body: {body} tail: {tail} ==> {fish_type}\n")       #test  문
fw.close()