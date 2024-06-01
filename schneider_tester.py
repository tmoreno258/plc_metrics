import time
from pyModbusTCP.client import ModbusClient
from pprint import pprint
# init modbus client
c = ModbusClient(host='localhost', port=502, auto_open=True, debug=False)

# main read loop
while True:
    # read 10 bits (= coils) at address 0, store result in coils list
    coils_l = c.read_coils(20, 14)
    h_reg_l = c.read_holding_registers(40, 3)


    # if success display registers
    if coils_l and h_reg_l:
        print(coils_l)
        print(h_reg_l)
    else:
        print('unable to read coils')

    time.sleep(0.5)