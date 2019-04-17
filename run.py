from pylogix.eip import PLC
class PLCMonitor:
    def __init__(self):
        self.pylogixPLC = PLC()
        self.pylogixPLC.IPAddress = "192.168.111.249"
        self.pylogixPLC.ProcessorSlot = 3
        self.pylogixPLC.Micro800 = False
        self.multiread = True

    def Read (self):
        if self.multiread:
            connected = False
            try:
                values = self.pylogixPLC.Read(["bool01", "int01", "float01", "string01"])
                connected = True
            except Exception as err:
                print("ERROR [" + self.pylogixPLC.IPAddress + "]: " + str(err))
                if "Multi-read failed" in str(err):
                    self.multiread = False
                elif str(err) == "timed out":
                    self.connected = False

if not self.multiread or not values:
    # Read tags individually
