from a10sdk.common.A10BaseClass import A10BaseClass


class Force(A10BaseClass):
    
    """Class Description::
    Unconditional write to Non-volatile Memory.

    Class force supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param all_partitions: {"type": "number", "description": "All partition configurations", "format": "flag"}
    :param name: {"description": "Local Configuration Profile Name", "format": "string", "minLength": "1", "optional": false, "maxLength": "31", "type": "string"}
    :param primary: {"type": "number", "description": "Write to default Primary Configuration", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/write/force`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "force"
        self.a10_url="/axapi/v3/write/force"
        self.DeviceProxy = ""
        self.all_partitions = ""
        self.name = ""
        self.primary = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


