import socket
try:
    #creating socket
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #DGRAM = DataGram  A datagram is a basic unit of data transfer in packet-switched networks
    #AF_INET => AF_INET is a constant in Python's socket module, used when creating a socket. It specifies the address family for the socket, which is the type of addresses the socket can communicate with.
    #SOCK_DGRAM =>  In Python's socket programming, SOCK_DGRAM is a constant used to specify the type of socket being created. It indicates that the socket will use the User Datagram Protocol (UDP).
    print("socket.created")
    ip_add = "172.16.4.165"
    port = 7993
    target_add = (ip_add,port)
    message = input("Enter the message : 😁")
    encoded_msg = message.encode("ascii")
    s.sendto(encoded_msg,target_add)
    print("message sent successfully")
    s.close()

except Exception as e:
    print("An error occured",e)
