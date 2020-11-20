# Chatbot Project

## Environment

### Web

Language and Framework

- Front : JavaScript, React

- Back : Python, Flask
  - DB
    - 내부 DB : SQL? NOSQL?
    - 서버 DB : SQL? NOSQL?
  - Machine Learning 어떡하냐...

### Data Analysis

Language : Python

DB

- 내부 DB : SQL? NOSQL?



## Architecture

Front Server, Back Server -> 총 2개의 서버를 둔다.

- client
  - public
  - src

- server
  - serverwork
  - machinelearning
  - analysis



## Algorithm

### Front

1. 챗봇 톡창
2. 사용자가 S(문장) 입력
3. S를 Back으로 전송

### Back

4. S 수신

5. #### Machine Learning

   - S에서

     C(지역), P(장소), A(형용사) 인식

     - C=PN : 고유 명사 -> 함덕, 애월, 조천, ...
     - P=N : 명사 -> 카페, 박물관, ...
     - A=A : 형용사 -> 가격이 싼, 뷰가 이쁜, 자몽 음료가 맛있는, ... 

6. #### Data Analysis
   - PN, N, A를 가지고 내부 DB와 매핑하며 R(결과값) 추출

   - R Front로 전송

### Front

7. R 수신
8. R 클릭 시 지도 출력(링크)

## To Do

Front - 세부적인 것은 다음 회의

- 화면 디자인 작성

- 프로토타입 작성

Back

- 모델링한 데이터를 기반으로 해서 파일 전송, 수신

Machine Learning : 김진, 이태양, 허지식

- 

Data Mining : 지영, 나연, 근형, 소영, 윤주

- 로그인
- 크롤링
- 크롤링 데이터 추출
- 분석
- db저장

----

- db저장

## 기타

사용자 질문 형식 : ~~에서 ~~한 ~~ 추천해줘 ...........





## 과제