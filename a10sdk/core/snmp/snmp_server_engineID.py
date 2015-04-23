from a10sdk.common.A10BaseClass import A10BaseClass


class Engineid(A10BaseClass):
    
    """Class Description::
    Define local engineID.

    Class engineID supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param engId: {"description": "Define local engineID HEX WORD", "format": "string", "minLength": 10, "optional": true, "maxLength": 24, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/engineID`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "engineID"
        self.a10_url="/axapi/v3/snmp-server/engineID"
        self.DeviceProxy = ""
        self.uuid = ""
        self.engId = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


