## TCP와 UDP의 특징과 차이

![image](https://user-images.githubusercontent.com/53684676/83508949-9f0bed80-a505-11ea-846d-6aa693623423.png)

### TCP(Transmission Control Protocol)란?

> 인터넷상에서 데이터를 메시지의 형태로 보내기위해 IP와 함께 사용하는 프로토콜

일반적으로 TCP와 IP를 함께 사용하는데, IP가 데이터의 배달을 처리한다면 TCP는 *패킷*을 추적 및 관리하게 됩니다. **연결형 서비스를 지원하는 프로토콜**로 인터넷 환경에서 기본으로 사용합니다.

#### TCP 특징

- 연결형 프로토콜
- 3-way handshacking과정을 통해 연결을 설정, 4-way handshaking을 통해 해제
- 흐름 제어 및 혼잡 제어
- 높은 신뢰성을 보장
- UDP보다 속도가 느림

TCP가 가상 회선 방식을 제공한다는 것은 발신지와 수신지를 연결하여 패킷을 전송하기 위한 논리적 경로를 배정한다는 뜻입니다. 3-way handshacking과정은 목적지와 수신지를 확실히하여 정확한 전송을 보장하기 위해서 세션을 수립하는 과정을 의미합니다. TCP는 연결형 서비스로 신뢰성을 보장하기 떄문에 3-way handshacking의 과정도 사용하는 것이고, 데이터의 흐름제어나 혼잡제어와 같은 기능도 합니다. 이러한 기능때문에 UDP보다 속도가 느리게 됩니다.**TCP는 연속성보다 신뢰성있는 전송이 중요할 때에 사용하는 프로토콜**입니다.

#### TCP 서버의 특징

- 서버소켓은 연결만을 담당
- 서버와 클라이언트는 1대1로 연결된다.
- 스트림 전송으로 전송 데이터의 크기가 무제한이다.
- 패킷에 대한 응답을 해야하때문에 성능이 낮다.
- Streaming 서비스에 불리하다.(손실된 경우 재전송 요청을 하므로)

```
패킷이란?
인터넷 내에서 데이터를 보내기 위한 경로배정을 효율적으로 하기 위해서 데이터를 여러 개의 조각들로 나누어 전송하는데 이 때, 이 조각을 패킷이라고 합니다.
```

### UDP(User Datagram Protocol)

> 데이터를 데이터그램 단위로 처리하는 프로토콜

여기서 데이터그램이란 독립적인 관계를 지니는 패킷이라는 뜻입니다. UDP는 TCP와 반대로 **비연결형 서비스를 지원하는 프로토콜**로 각각의 패킷은 다른 경로로 전송되고, 각 각의 패킷은 독립적인 관계를 지니게 됩니다.

#### UDP 특징

- 비연결형 프로토콜
- 정보를 주고 받을 때 정보를 보내거나 받는다는 신호절차를 거치지 않음
- UDP헤더의 CheckSum필드를 통해 최소한의 오류만 검출
- 낮은 신뢰성
- TCP보다 속도가 빠름

UDP는 비연결형 서비스이기 때문에, 연결을 설정하고 해제하는 과정이 존재하지 않습니다.서로 다른 경로로 독립적으로 처리함에도 패킷에 순서를 부여하여 재조립을 하거나 *흐름 제어* 또는 *혼잡 제어*와 같은 기능도 처리하지 않기에 TCP보다 속도가 빠르며 네트워크 부하가 적다는 장점이 있지만 신뢰성있는 데이터의 전송을 보장하지는 못 합니다. **UDP는 신뢰성보다는 연속성이 중요한 서비스**에서 자주 사용됩니다.

#### UDP 서버의 특징

- 연결 자체가 없어서 서버 소켓과 클라이언트 소켓의 구분이 없음
- 소켓 대힌 IP를 기반으로 데이터를 전송
- 서버와 클라이언트는 1대1, 1대N, N대N 등으로 연결될 수 있음
- 흐름제어가 없어서 패킷이 제대로 전송되었는지, 오류가 없는지 확인할 수 없음
- 파일 전송과 같은 신뢰성이 필요한 서비스보다 성능이 중요시 되는 경우에 사용

```
흐름제어와 혼잡제어란?
흐름제어는 데이터를 송수신하는 곳의 데이터 처리 속도를 조절하여 수신자의 버퍼 오버플로우를 방지하는 것입니다.예를 들어 송신하느 곳에서 감당이 안되게 데이터를 빠르게 많이 보내면 수신자에서 문제가 발생하기 때문입니다.
혼잡제어는 네트워크 내의 패킷 수가 넘치게 증가하지 않도록 방지하는 것입니다. 만약 정보의 소통량이 과다하면 패킷을 조금만 전송하여 혼잡 붕괴 현상이 일어나는 것을 막습니다.
```

#### 채팅 서버-클라이언트 간에는 어떤 프로토콜을 사용하는 것이 유리할까?

채팅 서버는 클라이언트간에 빠른 데이터 송신보다도 신뢰성 있는 데이터 송수신이 더 중요합니다.
그래서 신뢰성 있는 데이터 송수신을 지원하는 TCP 프로토콜을 사용하는 것이 좋습니다.

#### 동영상 스트리밍 서비스에서는 어떤 프로토콜을 사용하는 것이 유리할까?

데이터의 유실이 일부 있어도 문제없고 빠른 전송이 필요한 서비스이기 때문에 UDP 프로토콜을 사용하는 것이 좋습니다. UDP는 TCP와 달리 브로드캐스팅을 지원합니다.