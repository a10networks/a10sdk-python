from a10sdk.common.A10BaseClass import A10BaseClass


class Pcp(A10BaseClass):
    
    """Class Description::
    Set Port Control Protocol parameters.

    Class pcp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param default_template: {"description": "Bind the default template for PCP (Bind a PCP template)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/pcp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "pcp"
        self.a10_url="/axapi/v3/cgnv6/pcp"
        self.DeviceProxy = ""
        self.default_template = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


