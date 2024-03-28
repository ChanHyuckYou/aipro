with open('input_data.rtf', 'r') as file:                   #with 문을 사용하여, open과 close를 생략하고, input_data읽어오기
    fish_data = file.readlines()                            #한 줄씩 읽기

with open('output_result.rtf', 'w+') as file:                   #with 문을 사용하여, open과 close를 생략하고, output파일에 출력하고 없으면 생성

    for data in fish_data:                                  #'data'에 'fish_data'한 라인씩 생성
        length, tail_length = map(int, data.split())
        fish_type = ""

        if length > 81 and tail_length < 13:                #몸길이가 81이상이고 꼬리길이가 13보다 작으면 농어 아니면 연어
            fish_type = "seabass"
        else:
            fish_type = "salmon"
        
        file.write(f"body: {length} tail: {tail_length} ==> {fish_type}\n")
        print(f"body: {length} tail: {tail_length} ==> {fish_type}")
        
