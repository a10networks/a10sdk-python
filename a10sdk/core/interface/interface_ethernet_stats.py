from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param giants: {"description": "Giants", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param transmitted_multicasts: {"description": "Transmitted multicasts", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param received_broadcasts: {"description": "Received broadcasts", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param received_multicasts: {"description": "Received multicasts", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param packets_input: {"description": "Input packets", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param transmitted_unicasts: {"description": "Transmitted unicasts", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param crc: {"description": "CRC", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param packets_output: {"description": "Output packets", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param received_unicasts: {"description": "Received unicasts", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param runts: {"description": "Runts", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param bytes_output: {"description": "Output bytes", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param collisions: {"description": "Collisions", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param input_errors: {"description": "Input errors", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param bytes_input: {"description": "Input bytes", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param transmitted_broadcasts: {"description": "Transmitted braodcasts", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param frame: {"description": "Frames", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param output_errors: {"description": "Output errors", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.giants = ""
        self.transmitted_multicasts = ""
        self.received_broadcasts = ""
        self.received_multicasts = ""
        self.packets_input = ""
        self.transmitted_unicasts = ""
        self.crc = ""
        self.packets_output = ""
        self.received_unicasts = ""
        self.runts = ""
        self.bytes_output = ""
        self.collisions = ""
        self.input_errors = ""
        self.bytes_input = ""
        self.transmitted_broadcasts = ""
        self.frame = ""
        self.output_errors = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ethernet(A10BaseClass):
    
    """Class Description::
    Statistics for the object ethernet.

    Class ethernet supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param trunk_group_list: {"minItems": 1, "items": {"type": "trunk-group"}, "uniqueItems": true, "array": [{"required": ["trunk-number"], "properties": {}}], "type": "array", "$ref": "/axapi/v3/interface/ethernet/{ifnum}/lldp/ddos/ip/ipv6/lw-4o6/trunk-group/{trunk-number}"}
    :param ifnum: {"optional": false, "oid": "1001", "type": "number", "description": "Ethernet interface number", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ethernet/{ifnum}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ifnum"]

        self.b_key = "ethernet"
        self.a10_url="/axapi/v3/interface/ethernet/{ifnum}/stats"
        self.DeviceProxy = ""
        self.lldp = {}
        self.stats = {}
        self.bfd = {}
        self.ip = {}
        self.ddos = {}
        self.trunk_group_list = []
        self.ifnum = ""
        self.lw_4o6 = {}
        self.ipv6 = {}
        self.isis = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


