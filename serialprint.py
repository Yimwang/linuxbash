import serial

port = "/dev/ttyACM0"
baud = 9600

ser = serial.Serial(port, baud, timeout=1)
# open the serial port
if ser.isOpen():
    print(ser.name + ' is open...')
    try:  
        while(1):
            print(ser.read())
    except Exception:
        print("Keyboard Interrupt")
else:
    print("error")
