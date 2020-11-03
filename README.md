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

- Front
  - public
  - src

- Back
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

   1. S에서

      C(지역), P(장소), A(형용사) 인식

      - PN : 고유 명사 -> 함덕, 애월, 조천, ...
      - N : 명사 -> 카페, 박물관, ...
      - A : 형용사 -> 가격이 싼, 뷰가 이쁜, 자몽 음료가 맛있는, ... 

6. #### Data Analysis
   1. PN, N, A를 가지고 내부 DB와 매핑하며 R(결과값) 추출
   2. R Front로 전송

### Front

7. R 수신

8. R 클릭 시 지도 출력(링크)

