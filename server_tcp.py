import socket
from time import sleep


# host, port = '121.179.45.130', 15300

message_sequence_no = 105
local_PM10_value = 37
local_PM25_value = 13
sw_data = 190304
latitude = 37.81774409
longitude = 127.7158708


def get_request(client_id, ip='121.179.45.130', port=15300):
    # request_string = f"#AQS_REQ,{client_id},{message_sequence_no},VER:1.1,{local_PM10_value}" \
    #     f",{local_PM25_value},{sw_data},{latitude},{longitude}!"
    request_string = "#AQS_REQ," + client_id + ',' + "105,VER:1.1,37,13,190304,37.81774409,127.7158708!"

    # request_string = '#AQS_REQ,01082238595,105,0,0!'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, port))
    except:
        return '', ''

    # request_byte = bytes(request_string, 'utf-8')
    reply = ""
    try:
        sock.sendall((request_string.encode('utf-8')))
        sleep(1)
        reply = sock.recv(1024)
        print("recvd: ", reply.decode('utf-8'))
    except KeyboardInterrupt:
        print("Connection Lost")
    sock.close()
    return request_string, reply.decode('utf-8')


# if __name__ == '__main__':
#     print(get_request('01082238595'))
