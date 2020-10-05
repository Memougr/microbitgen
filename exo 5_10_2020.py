import serial
port = "COM9"
conn = serial.Serial(port, 115200)
message = input("Message: ")

while True:


    print(message)


    msg = (message).encode()


    conn.write(msg)
