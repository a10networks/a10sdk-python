from a10sdk.common.A10BaseClass import A10BaseClass


class Terminal(A10BaseClass):
    
    """Class Description::
    Write to terminal.

    Class terminal supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param partition: {"type": "number", "description": "Per-partition configurations", "format": "flag"}
    :param all_partitions: {"type": "number", "description": "All partition configurations", "format": "flag"}
    :param name: {"description": "Local Configuration Profile Name", "format": "string", "minLength": "1", "optional": false, "maxLength": "31", "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/write/terminal`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "terminal"
        self.a10_url="/axapi/v3/write/terminal"
        self.DeviceProxy = ""
        self.partition = ""
        self.all_partitions = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


