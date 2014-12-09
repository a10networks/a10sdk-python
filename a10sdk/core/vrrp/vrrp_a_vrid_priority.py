from a10sdk.common.A10BaseClass import A10BaseClass


class Priority(A10BaseClass):
    
    """Class Description::
    HA VRRP-A Global Commands.

    Class priority supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param priority_value: {"description": "VRRP-A priorty. help-val Priority, default is 150", "format": "number", "default": 150, "optional": true, "maximum": 255, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/vrid/{vrid_val}/priority`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "priority"
        self.a10_url="/axapi/v3/vrrp-a/vrid/{vrid_val}/priority"
        self.DeviceProxy = ""
        self.priority_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


