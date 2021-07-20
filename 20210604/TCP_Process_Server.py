import socket

#숫자에 대한 영어 사전

table = {'박서연':'21173065'}

s=socket.socket() #AF_INET, SOCK_STREAM
address = ("", 2500)
s.bind(address)
s.listen(1)
print('waiting....')
c_socket, c_addr = s.accept()
print("Connection from", c_addr)

while True:
    data = c_socket.recv(1024).decode() #요청수신
    try:
        resp = table[data] #데이터를 key로 사용하여 value를 가져온다
    except:
        c_socket.send('잘못 입력하셨습니다.'.encode()) #오류가 있을 때
    else:
        c_socket.send(resp.encode()) #변화 값을 전송
