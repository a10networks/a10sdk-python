from a10sdk.common.A10BaseClass import A10BaseClass


class Global(A10BaseClass):
    
    """Class Description::
    Stateful Firewall Configuration (default:disabled).

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param stateful_firewall_value: {"optional": true, "enum": ["enable"], "type": "string", "description": "'enable': Enable stateful firewall; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/global"
        self.DeviceProxy = ""
        self.stateful_firewall_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


