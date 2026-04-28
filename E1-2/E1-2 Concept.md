# 핵심 개념 정리
본 과정에서 필요한 개념들을 정리한 파일입니다.\
자세한 코드는 E1-2 파일을 참고해 주시기 바랍니다.
[🏠처음으로 돌아가기](./README.md)

---

## 1. import (라이브러리 불러오기)

```python
import json  # JSON 파일 다루기
import os    # 파일 확인하기
```

**정의**: 이미 만들어진 코드를 가져와서 사용
**비유**: 자동차 부품을 사서 조립하는 것 (직접 만들지 않음)

---

## 2. 클래스 (Class)

```python
class Quiz:  # 설계도
    pass

quiz = Quiz()  # 설계도로 물건 만들기
```

**정의**: 물건을 만드는 설계도
**비유**: 붕어빵 기계 = 클래스, 붕어빵 = 객체

---

## 3. self (이 객체 자신)

```python
class Quiz:
    def __init__(self, question):
        self.question = question  # 이 객체의 question
```

**정의**: 지금 다루고 있는 객체를 가리킴
**역할**: quiz1과 quiz2를 구분함

```python
quiz1 = Quiz("문제1")
quiz2 = Quiz("문제2")

quiz1.question  # "문제1"
quiz2.question  # "문제2"
```

---

## 4. __init__ (초기화 메서드)

```python
def __init__(self, question, choices, answer):
    self.question = question
    self.choices = choices
    self.answer = answer
```

**정의**: 객체가 만들어질 때 자동으로 실행되는 함수
**언제**: `Quiz("문제", [...], 2)` 이렇게 쓸 때

---

## 5. 메서드 (클래스 안의 함수)

```python
class Quiz:
    def display(self):  # 메서드
        print(self.question)
    
    def check_answer(self, user_answer):  # 메서드
        return user_answer == self.answer

# 사용
quiz.display()
quiz.check_answer(2)
```

**정의**: 클래스 안에 있는 함수
**특징**: 항상 첫 번째 매개변수가 `self`

---

## 6. 속성 (객체가 갖는 데이터)

```python
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question    # 속성
        self.choices = choices      # 속성
        self.answer = answer        # 속성

quiz = Quiz("문제", [...], 2)
print(quiz.question)  # "문제" 출력
```

**정의**: 객체가 갖는 정보
**접근**: `객체.속성명`

---

## 7. 리스트문 (여러 값 저장)

```python
fruits = ["apple", "banana", "cherry"]

# 접근 (인덱싱)
fruits[0]  # "apple"
fruits[1]  # "banana"

# 추가
fruits.append("date")

# 반복
for fruit in fruits:
    print(fruit)
```

**정의**: 순서가 있는 여러 값 저장
**특징**: 인덱스는 0부터 시작

---

## 8. 딕셔너리 (키-값 쌍)

```python
student = {
    "name": "Alice",
    "age": 25,
    "score": 95
}

# 접근 (키로 접근)
student["name"]   # "Alice"
student["age"]    # 25

# 추가
student["email"] = "alice@example.com"
```

**정의**: 키(key)로 값(value)을 저장
**특징**: 순서 없음, 키로 값에 접근

---

## 9. if-elif-else (조건문)

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

**정의**: 조건에 따라 다른 코드 실행
**구조**: 
- `if`: 첫 조건
- `elif`: 다른 조건 (여러 개 가능)
- `else`: 모두 거짓일 때

---

## 10. for 반복문

```python
# 리스트 반복
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

# 숫자 반복
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# 순번과 함께
for idx, fruit in enumerate(["apple", "banana"], 1):
    print(f"{idx}. {fruit}")
    # 1. apple
    # 2. banana
```

**정의**: 정해진 횟수만큼 반복
**언제 사용**: 리스트의 모든 요소를 처리할 때

---

## 11. while 반복

```python
count = 0
while count < 5:
    print(count)
    count += 1
# 출력: 0, 1, 2, 3, 4

# 무한 반복 (조건으로 탈출)
while True:
    choice = input("입력: ")
    if choice == "exit":
        break  # 반복 탈출
```

**정의**: 조건이 참인 동안 계속 반복
**언제 사용**: 언제까지 반복할지 모를 때

---

## 12. break와 continue

```python
# break: 반복 탈출
for i in range(10):
    if i == 5:
        break  # 반복 종료
    print(i)
# 출력: 0, 1, 2, 3, 4

# continue: 이번 반복 건너뛰기
for i in range(5):
    if i == 2:
        continue  # print 건너뜀
    print(i)
# 출력: 0, 1, 3, 4
```

**정의**:
- `break`: 반복 완전히 빠져나가기
- `continue`: 지금부터 다음 반복으로

---

## 13. try-except (에러 처리)

```python
try:
    number = int("abc")  # 에러 발생 가능
except ValueError:  # 에러가 발생했을 때
    print("숫자를 입력해주세요")
    # 프로그램은 계속 실행됨
```

**정의**: 에러가 발생해도 프로그램이 종료되지 않게 처리
**장점**: 안정적인 프로그램

---

## 14. with 문 (파일 안전하게 다루기)

```python
# ❌ 파일을 닫지 않을 수 있음
f = open("data.txt", "r")
content = f.read()
f.close()  # 깜빡할 수 있음

# ✅ 자동으로 닫힘
with open("data.txt", "r") as f:
    content = f.read()
# 블록 끝나면 자동으로 파일 닫힘
```

**정의**: 파일을 열고 자동으로 닫기
**장점**: 파일 손상 방지

---

## 15. return (함수의 결과 반환)

```python
# return 없음
def greet():
    print("안녕")

greet()  # "안녕" 출력

# return 있음
def add(a, b):
    return a + b

result = add(3, 5)  # result = 8
print(result)  # 8
```

**정의**: 함수가 결과값을 돌려줌
**용도**: 함수의 계산 결과를 변수에 저장

---

## 종합 예시 살펴보기

```python
# 클래스 정의
class Quiz:
    # __init__으로 초기화
    def __init__(self, question, choices, answer):
        self.question = question      # 속성
        self.choices = choices
        self.answer = answer
    
    # 메서드 정의
    def display(self):
        print(self.question)
        for idx, choice in enumerate(self.choices, 1):  # for 반복
            print(f"{idx}. {choice}")
    
    def check_answer(self, user_answer):
        return user_answer == self.answer  # return

# 객체 생성
quiz = Quiz("1+1?", ["1", "2", "3"], 2)

# 메서드 호출
quiz.display()

# 답 입력받기 (while, try-except)
while True:
    try:
        answer = int(input("답: "))
    except ValueError:
        print("숫자를 입력해주세요")
        continue
    
    # 정답 확인 (if-else)
    if quiz.check_answer(answer):
        print("정답!")
    else:
        print("오답!")
    break

# 파일에 저장 (with, import json)
import json
with open("data.json", "w") as f:
    data = {"quiz": quiz.question}
    json.dump(data, f)
```

---

## 개념 한번에 정리

| 개념 | 뜻 | 예시 |
|------|----|----|
| import | 라이브러리 불러오기 | `import json` |
| 클래스 | 설계도 | `class Quiz:` |
| self | 이 객체 자신 | `self.question` |
| __init__ | 초기화 메서드 | `def __init__(self):` |
| 메서드 | 클래스 안의 함수 | `def display(self):` |
| 속성 | 객체가 갖는 데이터 | `self.answer = 2` |
| 리스트 | 여러 값 저장 | `[1, 2, 3]` |
| 딕셔너리 | 키-값 쌍 | `{"name": "Alice"}` |
| if-elif-else | 조건문 | `if x > 5: ...` |
| for | 정해진 횟수 반복 | `for i in range(5):` |
| while | 조건 반복 | `while True:` |
| break/continue | 반복 제어 | `break`, `continue` |
| try-except | 에러 처리 | `try: ... except:` |
| with | 파일 안전하게 | `with open(...):` |
| return | 결과 반환 | `return result` |

---