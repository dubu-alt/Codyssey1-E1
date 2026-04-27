# Mini NPU Simulator - 핵심 개념 정리

이 프로젝트를 이해하기 위해 알아야 할 개념들을 정리한 문서입니다.

---

## 1. 객체지향 프로그래밍 (OOP)

### 클래스(Class)와 객체(Object)

클래스는 **데이터와 기능을 묶은 설계도**입니다. 객체는 그 설계도로 만든 실제 결과물입니다.

```python
class Matrix:
    def __init__(self, data):   # 생성자: 객체가 만들어질 때 실행
        self.data = data        # self: 이 객체 자신을 가리킴
        self.size = len(data)
```

```python
# 클래스(설계도) → 객체(실제 생성)
m = Matrix([[1, 0], [0, 1]])   # Matrix 객체 생성
print(m.size)                   # 2
```

> `self`는 "나 자신(이 객체)"을 뜻합니다. `self.data`는 이 객체의 data 변수라는 의미입니다.

---

### 메서드(Method)

클래스 안에 정의된 함수를 메서드라고 합니다.

| 메서드 | 역할 |
|---|---|
| `__init__()` | 객체 생성 시 자동 실행되는 초기화 함수 |
| `__repr__()` | `print(객체)` 할 때 출력될 문자열 정의 |
| `get(i, j)` | 일반 메서드 - 직접 호출해서 사용 |
| `set(i, j, v)` | 일반 메서드 - 직접 호출해서 사용 |

`__init__`, `__repr__` 처럼 앞뒤에 `__`가 붙은 메서드는 **파이썬이 특별하게 다루는 메서드**입니다.

---

### 캡슐화(Encapsulation)

데이터를 직접 건드리지 않고, **메서드를 통해서만 접근**하게 만드는 것입니다.

```python
# 나쁜 방법: 내부 데이터 직접 접근
value = m.data[1][2]

# 좋은 방법: 메서드를 통해 접근 (캡슐화)
value = m.get(1, 2)
```

메서드로 감싸두면, 나중에 범위 검사나 로그를 추가할 때 메서드 하나만 수정하면 됩니다.

---

## 2. 2차원 배열 (2D Array)

### 구조

행(row)과 열(column)로 이루어진 표 형태의 자료구조입니다.

```
        열(j)
        0    1    2
행(i) 0 [ 1.0  0.0  1.0 ]
      1 [ 0.0  1.0  0.0 ]
      2 [ 1.0  0.0  1.0 ]
```

파이썬에서는 리스트 안에 리스트를 넣어서 표현합니다:

```python
data = [
    [1.0, 0.0, 1.0],   # 0번 행
    [0.0, 1.0, 0.0],   # 1번 행
    [1.0, 0.0, 1.0]    # 2번 행
]

data[1][2]   # 1번 행, 2번 열 → 0.0
```

### 이중 for문으로 순회

```python
for i in range(n):       # 행 순서대로
    for j in range(n):   # 열 순서대로
        print(data[i][j])

# 순서: (0,0) → (0,1) → (0,2) → (1,0) → (1,1) → ...
```

---

## 3. MAC 연산 (Multiply-Accumulate)

### 개념

**"같은 위치끼리 곱하고, 전부 더한다"** 는 연산입니다.

```
필터:         패턴:         곱셈 결과:
1  0  1       1  1  0       1  0  0
0  1  0   ×   0  1  0   =   0  1  0   → 합산 → 점수: 4
1  0  1       1  0  1       1  0  1
```

### 왜 점수 = 유사도인가?

- 두 자리가 **둘 다 1** → `1 × 1 = 1` (유사도 기여 ✅)
- 한 쪽만 1 → `1 × 0 = 0` (기여 없음)
- **겹치는 부분이 많을수록 점수가 높아짐** → 점수 = 유사도

### 시간 복잡도: O(N²)

n×n 행렬이면 이중 for문이 `n × n = N²`번 실행됩니다.

| 크기 | 반복 횟수 |
|---|---|
| 5×5 | 25번 |
| 13×13 | 169번 |
| 25×25 | 625번 |

크기가 2배가 되면 연산은 **4배** 증가합니다.

---

## 4. 타입 힌트 (Type Hint)

파이썬은 변수 타입을 명시하지 않아도 되지만, **힌트를 적어서 코드 가독성을 높일 수 있습니다.**

```python
from typing import List, Dict, Optional

def compute_mac(filter_matrix: Matrix, pattern_matrix: Matrix) -> float:
#               ↑ 입력 타입 힌트                                  ↑ 반환 타입 힌트
```

| 타입 힌트 | 의미 |
|---|---|
| `List[List[float]]` | float로 이루어진 리스트의 리스트 (2차원 배열) |
| `Dict` | 키-값 쌍으로 이루어진 딕셔너리 |
| `Optional[str]` | str 또는 None (값이 없을 수도 있음) |
| `-> float` | 이 함수는 float를 반환함 |

> 타입 힌트는 **강제 사항이 아닙니다.** 틀려도 오류가 나지 않지만, 코드를 읽는 사람에게 큰 도움이 됩니다.

---

## 5. 예외 처리 (Exception Handling)

### 예외(Exception)란?

프로그램 실행 중 발생하는 오류입니다.

```python
int("abc")        # ValueError: 숫자가 아닌 문자열
data[10][0]       # IndexError: 범위를 벗어난 인덱스
open("없는파일")   # FileNotFoundError: 파일 없음
```

### try / except

```python
try:
    # 오류가 날 수 있는 코드
    value = int(input("숫자 입력: "))
except ValueError:
    # 오류가 났을 때 실행
    print("숫자를 입력하세요.")
```

### raise - 의도적으로 예외 발생

```python
def normalize_label(label: str) -> str:
    if label in ('+', 'cross'):
        return 'Cross'
    else:
        raise ValueError(f"인식 불가능한 라벨: {label}")
        # ↑ 잘못된 입력이 들어오면 직접 오류를 발생시킴
```

> `raise`는 "이 상황은 오류입니다"라고 **명시적으로 알리는** 것입니다.

---

## 6. JSON 파일 다루기

### JSON이란?

데이터를 텍스트로 저장하는 형식입니다. 파이썬의 딕셔너리/리스트와 구조가 거의 같습니다.

```json
{
  "filters": {
    "size_5": {
      "+": [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    }
  }
}
```

### 파이썬에서 읽기

```python
import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)   # JSON 파일 → 파이썬 딕셔너리

print(data['filters']['size_5'])   # 딕셔너리처럼 접근
```

### with 문

파일을 열고 자동으로 닫아주는 구문입니다.

```python
# with 없이
f = open('data.json')
data = json.load(f)
f.close()   # 직접 닫아야 함

# with 사용 (권장)
with open('data.json') as f:
    data = json.load(f)
    # 블록이 끝나면 자동으로 f.close() 실행
```

---

## 7. 부동소수점과 Epsilon 비교

### 부동소수점 오차란?

컴퓨터는 소수를 **2진수**로 저장하기 때문에 미세한 오차가 생깁니다.

```python
print(0.1 + 0.2)        # 0.30000000000000004
print(0.1 + 0.2 == 0.3) # False ← 위험!
```

### Epsilon 기반 비교

```python
EPSILON = 1e-9   # 0.000000001

# 나쁜 방법
if score_a == score_b:   # 부동소수점 오차로 틀릴 수 있음

# 좋은 방법
if abs(score_a - score_b) < EPSILON:   # 차이가 아주 작으면 같다고 판단
    return 'UNDECIDED'
```

> `1e-9`는 `1 × 10⁻⁹ = 0.000000001` 을 뜻하는 과학적 표기법입니다.

---

## 8. 문자열 처리

### 자주 쓰이는 문자열 메서드

```python
label = "  Cross  "

label.strip()    # "Cross"        ← 앞뒤 공백 제거
label.lower()    # "  cross  "    ← 소문자로 변환
label.split()    # ["Cross"]      ← 공백 기준으로 나누기
label.split('_') # ["Cross"]      ← 특정 문자 기준으로 나누기

"size_5_1".rsplit('_', 1)   # ["size_5", "1"] ← 오른쪽에서 1번만 나누기
```

### f-string (포맷 문자열)

```python
name = "Matrix"
size = 5
print(f"{name}({size}×{size})")   # Matrix(5×5)
print(f"{score:.6f} ms")          # 소수점 6자리까지 출력
```

---

## 9. 성능 측정

### time 모듈

```python
import time

start = time.time()        # 현재 시각 (초 단위)
compute_mac(filter, pattern)
end = time.time()

elapsed_ms = (end - start) * 1000   # 초 → 밀리초 변환
```

### 왜 여러 번 측정해서 평균을 내나?

한 번 측정하면 OS 스케줄링, 메모리 상태 등 외부 요인으로 값이 튈 수 있습니다. **10번 측정 후 평균**을 내면 더 신뢰할 수 있는 값을 얻습니다.

```python
for _ in range(10):   # _ 는 "이 변수는 쓰지 않겠다"는 관례
    start = time.time()
    compute_mac(filter_matrix, pattern_matrix)
    end = time.time()
    total += (end - start) * 1000

average = total / 10
```

---

## 10. CPU vs NPU 병렬 처리

### CPU (지금 코드)

한 번에 하나의 연산만 처리합니다 (직렬 처리).

```
(0,0)곱 → (0,1)곱 → (0,2)곱 → ... → 끝   (순서대로 하나씩)
```

### NPU / GPU

모든 위치의 곱셈을 **동시에** 처리합니다 (병렬 처리).

```
(0,0)곱
(0,1)곱  ← 동시에 실행
(0,2)곱
   ↓
전체 합산도 병렬로
```

### 왜 AI에서 NPU가 필요한가?

| 구분 | 처리 방식 | 속도 |
|---|---|---|
| CPU | 직렬 (하나씩) | 느림 |
| NPU/GPU | 병렬 (동시에) | 빠름 |

실제 AI 모델은 수십억 번의 MAC 연산이 필요하기 때문에, CPU만으로는 실시간 처리가 불가능합니다.

---

## 개념 간 연결 관계

```
JSON 파일
    ↓ (json 모듈로 읽기)
딕셔너리 (파이썬 자료구조)
    ↓ (2차원 배열 추출)
Matrix 클래스 (OOP)
    ↓ (이중 for문, O(N²))
MAC 연산
    ↓ (부동소수점 오차 → Epsilon 비교)
점수 판정
    ↓ (라벨 정규화 → 문자열 처리)
PASS / FAIL 출력
```