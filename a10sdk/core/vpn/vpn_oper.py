from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Num_hardware_devices: {"type": "number", "format": "number"}
    :param IPsec_mode: {"type": "string", "format": "string"}
    :param IKE_Gateway_total: {"type": "number", "format": "number"}
    :param IPsec_SA_total: {"type": "number", "format": "number"}
    :param Crypto_cores_assigned_to_IPsec: {"type": "number", "format": "number"}
    :param IKE_SA_total: {"type": "number", "format": "number"}
    :param Crypto_cores_total: {"type": "number", "format": "number"}
    :param IPsec_total: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.Num_hardware_devices = ""
        self.IPsec_mode = ""
        self.IKE_Gateway_total = ""
        self.IPsec_SA_total = ""
        self.Crypto_cores_assigned_to_IPsec = ""
        self.IKE_SA_total = ""
        self.Crypto_cores_total = ""
        self.IPsec_total = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Vpn(A10BaseClass):
    
    """Class Description::
    Operational Status for the object vpn.

    Class vpn supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ike_gateway_list: {"minItems": 1, "items": {"type": "ike-gateway"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"oper": {"type": "object", "properties": {"Status": {"type": "string", "format": "string"}, "Remote-IP": {"type": "string", "format": "string"}, "Hash": {"type": "string", "format": "string"}, "Encryption": {"type": "string", "format": "string"}, "Responder-SPI": {"type": "string", "format": "string"}, "Local-IP": {"type": "string", "format": "string"}, "Lifetime": {"type": "number", "format": "number"}, "Initiator-SPI": {"type": "string", "format": "string"}}}, "name": {"description": "IKE-gateway name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/vpn/ike-gateway/{name}"}
    :param ipsec_list: {"minItems": 1, "items": {"type": "ipsec"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"oper": {"type": "object", "properties": {"Hash-Algorithm": {"type": "string", "format": "string"}, "Protocol": {"type": "string", "format": "string"}, "DH-Group": {"type": "number", "format": "number"}, "Peer-IP": {"type": "string", "format": "string"}, "Local-IP": {"type": "string", "format": "string"}, "Anti-Replay": {"type": "string", "format": "string"}, "Lifebytes": {"type": "string", "format": "string"}, "NAT-Traversal": {"type": "number", "format": "number"}, "SA-Index": {"type": "number", "format": "number"}, "Remote-SPI": {"type": "string", "format": "string"}, "Mode": {"type": "string", "format": "string"}, "Encryption-Algorithm": {"type": "string", "format": "string"}, "Local-SPI": {"type": "string", "format": "string"}, "Lifetime": {"type": "number", "format": "number"}}}, "name": {"description": "IPsec name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 31, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/vpn/ike-gateway/{name}/ipsec/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vpn/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vpn"
        self.a10_url="/axapi/v3/vpn/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.ike_gateway_list = []
        self.ipsec_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


