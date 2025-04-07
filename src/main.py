from colorama import init, Style, Fore

# 초기화
#init(autoreset=True)

# 함수: 최소 패리티 비트 수 구하기
def find_minimum_k(data_len):
    k = 1
    while True:
        if (2**k - 1) >= data_len + k:
            return k
        k += 1

# 함수: 터미널 스타일 리셋
def reset_style():
    print(Style.RESET_ALL + "", end='')

# 시작
print("================== < Hamming Code Simulation > ==================")
data = input("Input Binary Data >>> ")  # 데이터 입력

p_num = find_minimum_k(len(data))  # 패리티 수 계산
print(f"패리티 비트 수 : {p_num}\n")

# 1. 비트 배치
print(Style.BRIGHT + "1. 비트배치")
reset_style()

bits = []
data_index = 0
total_len = len(data) + p_num

# 비트 라벨 출력
print(Fore.GREEN + "", end='')
for i in range(1, total_len + 1):
    if i & (i - 1) == 0:
        print(f"p{i}", end=' ')
    else:
        print(f"d{data_index + 1}", end=' ')
        data_index += 1

print("")

# 실제 비트 배치 출력
bits = []
data_index = 0
for i in range(1, total_len + 1):
    if i & (i - 1) == 0:
        print("?", end='  ')
        bits.append("?")
    else:
        print(data[data_index], end='  ')
        bits.append(data[data_index])
        data_index += 1

reset_style()

input()

# 2. 패리티 비트 계산
print(Style.BRIGHT + "\n\n2. 패리티비트 계산")
reset_style()

for k in range(p_num):
    index = 2**k
    xor = 0

    print(Fore.CYAN + f"p{index} 값")
    reset_style()

    for m in range(1, total_len + 1):
        if m & index and m != index:
            print(f"{int(bits[m-1])} ⊕", end=' ')
            xor ^= int(bits[m-1])
    print(f"\b\b= {xor}")

    bits[index - 1] = str(xor)

# 최종 송신 비트 출력
print(Style.BRIGHT + "\n최종 송신비트")
for b in bits:
    print(Fore.BLUE + b, end=' ')
reset_style()

# 3. 오류 비트 적용
print("\n")
error_bits = input("Input Error Sector(split with ,) >>> ")
error_bits = [e.strip() for e in error_bits.split(',') if e.strip().isdigit()]
error = list(bits)

for index in error_bits:
    idx = int(index) - 1
    error[idx] = str(int(not int(error[idx])))

# 4. 수신 & 오류 검출
print(Style.BRIGHT + "\n3. 수신")
reset_style()

error_p = []
for k in range(p_num):
    index = 2**k
    xor = int(error[index - 1])

    print(Fore.CYAN + f"p{index} 체크")
    reset_style()

    for i in range(1, total_len + 1):
        if i & index and i != index:
            print(f"{int(error[i - 1])} ⊕", end=' ')
            xor ^= int(error[i - 1])

    print(f"\b\b= {xor}", end=' ')
    if xor:
        print(Fore.RED + f"p{index} 오류발생")
        reset_style()
        error_p.append(index)
    else:
        print("")

# 오류 위치 판별
print("")
error_pos = sum(error_p)
for index in error_p:
    print(f"{index} +", end=' ')
print(Fore.RED + f"\b\b= {error_pos}, {error_pos}번째 비트 오류확인")
reset_style()

input()

# 5. 오류 수정
print(Style.BRIGHT + "\n4. 수신 측 오류수정")
reset_style()

if error_pos == 0:
    print("오류 없음, 수정 불필요")
else:
    print(f"{error_pos}번째 비트를 반전 {error[error_pos - 1]} -> {int(not int(error[error_pos - 1]))}")
    error[error_pos - 1] = str(int(not int(error[error_pos - 1])))

input()

# 6. 최종 수신 측 비트 출력 (패리티 제거)
print(Style.BRIGHT + "\n5. 최종 수신 측 비트")
reset_style()

for index in sorted([2**k for k in range(p_num)], reverse=True):
    error.pop(index - 1)

for bit in error:
    print(Fore.GREEN + bit, end=' ')
reset_style()

print("\n================== < Hamming Code Simulation END > ==================")