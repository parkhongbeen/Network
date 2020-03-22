### WWW 란?

- WWW 란?
  - W3 또는 (Web)
  - 주요요소: HTML, URL, HTTP
- HTMl: markup언어, hypertext와 hyperlink로 구성

### HTTP(hypertext Transfer Protocol)

- Server/Client모델로 Request/Response사용
  - Client에서 요청을 보내면, Server에서 응답을 준다.
  - HTTP는 Connectionless한 프로토콜 - 1회성 Request 및 Respose
  - TCP/IP socket을 이요해서 연결됨

![image-20200320001056736](/Users/hongbeen/Library/Application Support/typora-user-images/image-20200320001056736.png)

### HTTP 1.1

- HTTP는 Connectionless 방식
- HTTP 1.1은 keepalive 기능을 통해, 서버에서 설정된 keepalive timeout까지는 연결과정 없이 데이터 송수신 가능
  - 내부적으로 결국 매번 TCP 3-way-handshake과정을 거칠 필요가 없어짐

![image-20200320001218591](/Users/hongbeen/Library/Application Support/typora-user-images/image-20200320001218591.png)

### 일반적인 HTTP송수신

![image-20200320001253972](/Users/hongbeen/Library/Application Support/typora-user-images/image-20200320001253972.png)

### HTTP Request / Response

> HTTP 헤더는 읽을 수 있음(1.1버전 기준)

### 주요 Request Method

- GET: 정보읽기(SELECT)

  - 전달이 필요한 파라미터들은 URL을 통해 전달

  ![image-20200320001544055](/Users/hongbeen/Library/Application Support/typora-user-images/image-20200320001544055.png)

- POST: 정보입력하기(INSERT)

  - 전달이 필요한 파라미터들은 HTTP body에 포함되어 전달되므로, 사용자는 직접적인 확인 불가

  

![image-20200320001625641](/Users/hongbeen/Library/Application Support/typora-user-images/image-20200320001625641.png)

- PUT: 정보 수정하기(UPDATE)
- DELETE: 정보 삭제하기(DELETE)

- 웹사이트는 접속시 일반적으로 GET을 통해 HTML을 가져옴

- 주요 HTTP응답 코드

| 상태 코드 | 의미                                    |
| --------- | --------------------------------------- |
| 200       | 정상                                    |
| 400       | 유효하지 않은 파라미터 또는 잘못된 요청 |
| 401       | 승인되지 않은 엑세스                    |
| 403       | 엑세스 금지                             |
| 404       | 리소스를 찾을 수 없음                   |
| 500       | 내부 서버 오류                          |

### 쿠키와 세션

- HTTP는 Stateless: 통신이 끝나면 상태를 유지하지 않음
- 이를 보완하기 위한 기법이 쿠키와 세션
- 쿠키/세션의 유효기간
  - expires 설정이 있으면, 로컬 디스크에 저장 및 유효기간 경과시 삭제
  - expires 설정이 없으면, 메모리에 저장 및 브라우저 종료시 삭제

### URL(Uniform Resource Locator)

- 인터넷 상의 자원 위치 표기를 위한 규약
- WWW 주요 요소 중 하나: HTML, URL, HTTP

### URL vs URI

- URI: 통합 자원 식별자
- URI의 하위 개념이 URL
  - https://test.com 주소
    - https://test.com이라는 서버를 나타내는 URL이면서 URI
  - https://test.com/input:html 은 URL
  - https://tesst.com/input:html?id=hong&pw=1111은 URI
    - 내가 원하는 정보를 얻기 위해서는 ?id=hong&pw=1111이라는 식별자가 필요하기 때문

----

HTTPS

- HTTP통신시 사용하는 TCP/IP소켓 통신에서, 일반 텍스트 대신, SSL또는 TLS프로토콜을 통해 데이터 암호화하여 송수신
- HTTPS 기본 port는 443
- http:// 대신 https:// 로 시작



