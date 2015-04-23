from a10sdk.common.A10BaseClass import A10BaseClass


class Global(A10BaseClass):
    
    """    :param create_port_mapping_file: {"default": 0, "optional": true, "type": "number", "description": "Create Port Mapping File", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Fixed NAT Global configuration and Stats.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/fixed-nat/global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/cgnv6/fixed-nat/global"
        self.DeviceProxy = ""
        self.create_port_mapping_file = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


