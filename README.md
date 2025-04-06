# Hamming Code Simulation

**What is Hamming Code?**
1) Hamming 코드는 데이터가 전송될 때 오류를 감지하고 수정할 수 있는 오류 수정 시스템이다.
2) Hamming 코드는 패리티 비트를 이용한다.
3) 튜링상을 받은 기록이 있는 발명가인 Richard W.Hamming의 이름을 따서 명명되었다.
------------------------------------------------------------
**Pros and Cons**

장점)
1. 단일비트에서 오류 탐지 및 수정에 효과적임
2. 수신 측에서 오류를 수정할 수 있으므로 재전송을 요청할 필요가 없음 -> 지연이 많은 환경에서 유리함

단점)
1. 해밍코드는 단일 비트 오류만 수정이 가능해서, 두 개 이상의 비트 오류가 발생하면 오류 위치를 파악하기 어려움.
2. 오류 검출 및 수정을 위해 데이터에 여러 개의 패리티 비트를 추가해야 하므로 전송시 데이터 크기가 증가함.
