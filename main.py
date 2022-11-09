from CLI import ARGPARSER
import serial.tools.list_ports
from time import sleep

def checkMuxInf(port_name: str):
    with serial.Serial(
            port_name,
            baudrate=115200,
            timeout=1,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE
    ) as ser:
        try:
            ser.reset_input_buffer()
            ser.reset_output_buffer()
            ser.write(b'inf\n')
            sleep(1)
            data = ser.read(ser.in_waiting)  # read all input buffer
            lines = data.decode('UTF-8').split('\r\n')  # decode bytes data into string and split lines
            for line in lines:
                print(line)

        except Exception as err:
            print(err, f"happened at port {port_name}")
            print()
def checkMuxReboot(port_name: str):
    with serial.Serial(
            port_name,
            baudrate=115200,
            timeout=1,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE
    ) as ser:
        try:
            ser.reset_input_buffer()
            ser.reset_output_buffer()
            ser.write(b'r\n')
            sleep(1)
            data = ser.read(ser.in_waiting)  # read all input buffer
            lines = data.decode('UTF-8').split('\r\n')  # decode bytes data into string and split lines
            for line in lines:
                print(line)
            print("REBOOTED")

        except Exception as err:
            print(err, f"happened at port {port_name}")
            print()




if __name__ == '__main__':
    args = ARGPARSER.parse_args()
    if args.inf:
        name  = args.inf
        checkMuxInf(name)
    elif args.reboot:
        name = args.reboot
        checkMuxReboot(name)
    elif args.relayname:
        relayname = args.relayname