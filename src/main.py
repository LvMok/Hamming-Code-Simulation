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

#------------------------------------------------------------------------
hamming = int(input(), 2) #전송 하려는 이진수 값 입력 받음
hamming = list(str(format(hamming, 'b'))) #입력받은 이진수 값 리스트로 전환
i = 0
while(1):
    if 2**i >= len(hamming) + i + 1:
        parity = i #parity는 페리티 비트의 개수
        break
    i += 1
bit_leng = len(hamming) + parity #총 비트 길이

for k in range(bit_leng): #리스트에 페리티 비트가 들어갈 공간 만들기
    if k <= parity:
            hamming.insert(2**k-1, '0')
    else:
        continue

bit_leng = len(hamming)

for k in range(parity):
    index = 2**k
    xor = 0

    for m in range(1, bit_leng + 1):
        if m & index and m != index:
             xor = xor ^ int(hamming[m-1])

    hamming[index - 1] = str(xor)

for k in range(bit_leng-1):
    print(int(hamming[k]), end = '')
