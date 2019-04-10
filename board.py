import serial
import time


def connect(port_name, port_rate):
    try:
        ser = serial.Serial(port_name, int(port_rate))
    except serial.serialutil.SerialException:
        return None
    return ser


def send_data(ser, recvd_data, datetime):
    if ser is None:
        return 'Port is not connected'
    if recvd_data is None:
        return 'Awaiting response'
    if len(recvd_data) <= 0:
        return 'Awaiting response'
    data = ''
    # data = recvd_data + '\r\n'

    s = str(datetime)
    s = s.split('.')[0]
    s = ''.join(s.split('-'))
    s = ''.join(s.split(' '))
    s = ''.join(s.split(':'))

    data += '$' + s
    s = '$' + s
    try:
        ser.write(s.encode())
    except:
        return 'Port is not connected'
    time.sleep(1)

    indexes = [1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    recvd_data = recvd_data.split(',')

    for idx in indexes:
        insert = recvd_data[idx]
        insert = insert.replace('!', '')
        data += '$' + insert
        insert = '$' + insert
        try:
            ser.write(insert.encode())
        except:
            return 'Port is not connected'
        time.sleep(1)
    print(data)
    return data
