from a10sdk.common.A10BaseClass import A10BaseClass


class Oid(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param mib: {"not": "asn", "enum": ["sysDescr", "sysUpTime", "sysName"], "type": "string", "description": "'sysDescr': The MIB-2 OID of system description, 1.1.0; 'sysUpTime': The MIB-2 OID of system up time, 1.3.0; 'sysName': The MIB-2 OID of system nume, 1.5.0; ", "format": "enum"}
    :param asn: {"description": "Specify the format in ASN.1 style", "format": "string-rlx", "minLength": 1, "maxLength": 128, "not": "mib", "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oid"
        self.DeviceProxy = ""
        self.mib = ""
        self.asn = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Operation(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param oper_type: {"enum": ["getnext", "get"], "type": "string", "description": "'getnext': Get-Next-Request command; 'get': Get-Request command; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "operation"
        self.DeviceProxy = ""
        self.oper_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Snmp(A10BaseClass):
    
    """Class Description::
    SNMP type.

    Class snmp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param snmp_port: {"description": "Specify SNMP port, default is 161 (Port Number)", "format": "number", "default": 161, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param snmp: {"default": 0, "optional": true, "type": "number", "description": "SNMP type", "format": "flag"}
    :param community: {"description": "Specify SNMP community, default is \"public\" (Community String)", "format": "string-rlx", "default": "public", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/snmp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "snmp"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/snmp"
        self.DeviceProxy = ""
        self.snmp_port = ""
        self.uuid = ""
        self.oid = {}
        self.snmp = ""
        self.community = ""
        self.operation = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


