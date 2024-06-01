import yaml
import time
from pyModbusTCP.client import ModbusClient

class PLC_ModBus_TCPIP:
    def __init__(self, id, kind, ip, port):
        self.id = id
        self.kind = kind
        self.ip = ip
        self.port = port
        self.conn = ModbusClient(host=self.ip, port=self.port, auto_open=True, debug=False)

    def read_coil(self,):
        coils_l = self.conn.read_coils(0, 10)
        return None

if __name__ == "__main__":
    print(True)
