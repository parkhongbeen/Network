## TCP 3 Way-Handshake & 4 Way-Handshake

-----

### TCP 3-way Handshake란?

> TCP  통신을 위한 연결 설정 과정

![image-20200310205155287](/Users/hongbeen/Library/Application Support/typora-user-images/image-20200310205155287.png)

#### STEP1

클라이언트는 서버에 접속을 요청하는 SYN패킷을 보낸다.이 때 클라이언트는 SYN을 보내고 SYN/ACK응답을 기다리는 SYN_SENT상태가 되는 것이다.

#### STEP2

서버는 SYN요청을 받고 클라이언트에게 요청을 수락한다는 ACK와 SYN flag가 설정된 패킷을 발송하고 클라이언트가 다시 ACK로 응답하기를 기다린다.이 때 서버는 SYN_RECEIVED상태가 된다.

#### STEP3

클라이언트는 서버에게 ACK를 보내고 이후로부터는 연결리 이루어지고 데이터가 오가게 되는 것이다.이 때의 서버상태가 ESTABLISHED이다.

위와 같은 방식을 통신하는것이 신뢰성있는 연결을 맺어준다는 TCP의 3 Way Handshake방식이다.

-----

### TCP 4-Way Handshake

> TCP 통신종료를 위한 일련의 과정

![image-20200310205534109](/Users/hongbeen/Library/Application Support/typora-user-images/image-20200310205534109.png)

#### STEP1

클라리언트가 연결을 종료하겠다는 FIN flag를 전송한다.

#### STEP2

서버는 일단 확인메시지를 보내고 자신의 통신이 끝날때까지 기다리는데 이 상태가 TIME_WAIT상태다.

#### STEP3

서버가 통신이 끝났으면 연결이 종료되었다고 클라이언트에게 FIN flag를 전송한다.

#### STEP4

클라이언트는 확인했다는 메시지를 보낸다.

-----

그런데 만약 "Server에서 Fin을 전송하기 전에 전송한 패킷이 Routing지연이나 패킷 유실로 인한 재전송등으로 인해 Fin패킷보다 늦게 도착하는 상황"이 발생한다면?

Client에서 세션을 종료시킨 후 뒤늦게 도착하는 패킷이 있다면 이 패킷은 Drop되고 데이터는 유실될 것이다.

이러한 현상을 대비해서 Client는 Server로부터 Fin을 수신하더라도 일정시간동안 세션을 남겨놓고 잉여패킷을 기다리는 과정을 거치게 되는데 이 과정을 "TIME_WAIT"이라고 한다.

