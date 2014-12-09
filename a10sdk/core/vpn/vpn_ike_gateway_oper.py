from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Status: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param Remote_IP: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param Hash: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param Encryption: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param Responder_SPI: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param Local_IP: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param Lifetime: {"type": "number", "format": "number"}
    :param Initiator_SPI: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.Status = ""
        self.Remote_IP = ""
        self.Hash = ""
        self.Encryption = ""
        self.Responder_SPI = ""
        self.Local_IP = ""
        self.Lifetime = ""
        self.Initiator_SPI = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IkeGateway(A10BaseClass):
    
    """Class Description::
    Operational Status for the object ike-gateway.

    Class ike-gateway supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "IKE-gateway name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vpn/ike-gateway/{name}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ike-gateway"
        self.a10_url="/axapi/v3/vpn/ike-gateway/{name}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


