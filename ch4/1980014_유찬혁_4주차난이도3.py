def fileLoad(fileName):
    file = open('data/'+fileName,'r')         #salmon파일 읽기
    fileName = file.readlines()
    file.close()