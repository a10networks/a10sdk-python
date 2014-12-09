from a10sdk.common.A10BaseClass import A10BaseClass


class Ve(A10BaseClass):
    
    """Class Description::
    select VE interface to monitor.

    Class ve supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ve_num: {"description": "VE interface number", "format": "number", "optional": false, "maximum": 4094, "minimum": 2, "type": "number", "$ref": "/axapi/v3/interface/ve"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/netflow/monitor/{name}/sample/ve/{ve_num}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ve_num"]

        self.b_key = "ve"
        self.a10_url="/axapi/v3/netflow/monitor/{name}/sample/ve/{ve_num}"
        self.DeviceProxy = ""
        self.ve_num = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


