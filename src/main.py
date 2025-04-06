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

#-------------------------------------------- 1번 <- 비트 적용
print(Style.BRIGHT + "1. 비트배치")
reset_style()

bits = list() #전송할 비트 배열
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
        bits.append("?")
    else:
        print(data[i-p_num-1],end='  ')
        bits.append(data[i-p_num-1])
        
reset_style()

#-------------------------------------------- 2번 <- 패리티 비트 계산
print(Style.BRIGHT + "\n\n2. 패리티비트 계산")

bit_leng = len(bits)

reset_style()
for k in range(p_num):
    index = 2**k
    xor = 0 #XOR 합 초기화
    
    print(f"p{index} 값")
    for m in range(1, bit_leng + 1):
        if m & index and m != index:
            print(f"{int(bits[m-1])} ⊕",end=' ')
            xor = xor ^ int(bits[m-1])
    print(f"\b\b= {xor}")      

    bits[index - 1] = str(xor)

print(Style.BRIGHT + "\n최종 송신비트")
for k in range(bit_leng):
    print(Fore.BLUE + bits[k], end = ' ')

reset_style()

#-------------------------------------------- 3번 <- 오류비트 적용
print("\n")
error_bits = input("Input Error Sector(split with ,) >>> ") #오류 발생 부분 입력
error_bits = error_bits.split(',')
error = list(bits) #에러비트

for index in error_bits:
    error[int(index)-1] = str(int(not int(bits[int(index)-1]))) #비트 배열에 적용

#-------------------------------------------- 4번 <- 수신
print(Style.BRIGHT + "\n3. 수신")
reset_style()

error_p = list() #오류 패리티
for k in range(p_num):
    index = 2**k
    xor = int(error[index-1])
    
    print(Fore.CYAN + f"p{index} 체크")
    reset_style()
    
    for i in range(1,len(error)+1):
        if i&index and i != index:
            print(f"{int(error[i-1])} ⊕",end=' ')
            xor = xor ^ int(error[i-1])
    
    print(f"\b\b= {xor}",end=' ')
    
    if xor:
        print(Fore.RED + f"p{index} 오류발생")
        reset_style()
        error_p.append(index)
    else:
        print("")

print("")
sum = 0 #오류 패리티 합
for index in error_p:
    print(f"{index} +",end=' ')
    sum += index

print(Fore.RED + f"\b\b= {sum}, {sum}번째 비트 오류확인")
reset_style()

#-------------------------------------------- 5번 <- 오류 수정
print(Style.BRIGHT + "\n4. 수신 측 오류수정")
reset_style()

print(f"{sum}번째 비트를 반전 {error[sum-1]} -> {int(not (int(error[sum-1])))}")
error[sum-1] = str(int(not (int(error[sum-1]))))

#-------------------------------------------- 6번 <- 최종
print(Style.BRIGHT + "\n5. 최종 수신 측 비트")
reset_style()

for index in sorted([2**k for k in range(p_num)], reverse=True):
    error.pop(index-1)

for bit in error:
    print(Fore.GREEN + f"{bit}",end=' ')
    
reset_style()