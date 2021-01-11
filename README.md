# GO BEACH OR NOT

## 공공데이터를 이용한 해수욕장 방문 적합 여부 판별 서비스

---

### 기능

1. 홈 화면에서 해수욕장 검색 및 지역별 해수욕장 목록 조회가 가능
2. 조회 후 목록이 출력되면, 이름, 개장일, 폐장일, 사이트 URL, 연락처와 같은 기본정보가 제공된다. 이때 각 해수욕장의 이름 클릭시, 해당 해수욕장에 대한 세부정보를 볼 수 있는 페이지로 들어감
3. 각 해수욕장별 페이지에서는 해수욕장에 대한 기본 정보 뿐만 아니라 연간 행사 정보를 제공하고, 수질 검사 결과, 혼잡도 측정 결과를 공개하여 이를 기반으로 최종적인 방문 적합 여부를 판별. 사용자는 이러한 정보를 고려하여 해수욕장 방문 여부를 선택할 수 있음
4. 회원가입 및 로그인∙로그아웃 기능
5. 로그인을 한 사용자가 관심 있는 해수욕장 정보를 쉽게 접근할 수 있도록 관심 해수욕장을 등록하고 조회하는 기능을 제공

---

### OpenAPI 방식의 공공데이터 활용 (공공데이터포털)

- 해수욕장 수질적합 여부 서비스 (REST)
- 해양수산부_해수욕장 혼잡도 신호등 (REST)
- 해수욕장정보 서비스 (REST)
- 해양수산부_해수욕장 개장 폐장 정보

### Total Architecture

![GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled.png](GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled.png)

### Serverless Computing & Microservice ( AWS Lambda + API Gateway )

- [Zappa](https://github.com/Miserlou/Zappa) 를 이용하여 Python Flask application을 AWS Lambda + API Gateway에 배포
- RESTful API 방식 동작

### NoSQL 기반 Data Management System ( EC2 + MongoDB )

- 회원가입 정보 + 나의 해수욕장 정보 관리

---

### 구현 결과

[ main ]

![GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled%201.png](GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled%201.png)

![GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled%202.png](GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled%202.png)

[ detail ]

![GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled%203.png](GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled%203.png)

[ signup ]

![GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled%204.png](GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled%204.png)

[ login ]

![GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled%205.png](GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled%205.png)

![GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled%206.png](GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled%206.png)

[ my beach ]

![GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled%207.png](GO%20BEACH%20OR%20NOT%20e474f4dd96b1476f9e36ba2048b6cd82/Untitled%207.png)