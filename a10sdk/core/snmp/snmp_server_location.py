from a10sdk.common.A10BaseClass import A10BaseClass


class Location(A10BaseClass):
    
    """Class Description::
    Text for mib object sysLocation.

    Class location supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param loc: {"description": "The physical location of this node", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 20, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/location`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "location"
        self.a10_url="/axapi/v3/snmp-server/location"
        self.DeviceProxy = ""
        self.loc = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


