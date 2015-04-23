from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Hash_Algorithm: {"type": "string", "format": "string"}
    :param Protocol: {"type": "string", "format": "string"}
    :param DH_Group: {"type": "number", "format": "number"}
    :param Peer_IP: {"type": "string", "format": "string"}
    :param Local_IP: {"type": "string", "format": "string"}
    :param Anti_Replay: {"type": "string", "format": "string"}
    :param Lifebytes: {"type": "string", "format": "string"}
    :param NAT_Traversal: {"type": "number", "format": "number"}
    :param SA_Index: {"type": "number", "format": "number"}
    :param Remote_SPI: {"type": "string", "format": "string"}
    :param Mode: {"type": "string", "format": "string"}
    :param Encryption_Algorithm: {"type": "string", "format": "string"}
    :param Local_SPI: {"type": "string", "format": "string"}
    :param Lifetime: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.Hash_Algorithm = ""
        self.Protocol = ""
        self.DH_Group = ""
        self.Peer_IP = ""
        self.Local_IP = ""
        self.Anti_Replay = ""
        self.Lifebytes = ""
        self.NAT_Traversal = ""
        self.SA_Index = ""
        self.Remote_SPI = ""
        self.Mode = ""
        self.Encryption_Algorithm = ""
        self.Local_SPI = ""
        self.Lifetime = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipsec(A10BaseClass):
    
    """Class Description::
    Operational Status for the object ipsec.

    Class ipsec supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "IPsec name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vpn/ipsec/{name}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ipsec"
        self.a10_url="/axapi/v3/vpn/ipsec/{name}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


