from colorama import init, Style, Fore

# 함수들
def find_minimum_k(data_len): #최소 패리티 비트 수 구하는 함수
    k = 1
    while True:
        if(2**k-1 >= 4+k) : return k
        k+=1

def reset_style(): #터미널 스타일 리셋
    print(Style.RESET_ALL + "",end='')

#코드들
print("================== < Hamming Code Simulation > ==================")
data = input("Input Binary Data >>> ") #데이터 입력
p_num = find_minimum_k(len(data)) #패리티 수

print(f"패리티 비트 수 : {p_num}\n")


print(Style.BRIGHT + "1. 비트배치")
reset_style()

print(Fore.GREEN + "",end='') #터미널 색상
for i in range(1,len(data)+p_num+1):
    if(i&(i-1) == 0):
        print(f"p{i}",end=' ')
    else:
        print(f"d{i-p_num+1}",end=' ')
print("")
for i in range(1,len(data)+p_num+1):
    if(i&(i-1) == 0):
        print("?",end='  ')
    else:
        print(data[i-p_num-1],end='  ')
        
reset_style()