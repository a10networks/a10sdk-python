from a10sdk.common.A10BaseClass import A10BaseClass


class Cgnv6(A10BaseClass):
    
    """    :param fixed_nat: {"default": 0, "optional": true, "type": "number", "description": "Delete fixed-nat port-mapping-file", "format": "flag"}
    :param filename: {"description": "Specify the port-mapping-file to be deleted", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Delete cgnv6 related files.

    Class cgnv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/delete/cgnv6`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "cgnv6"
        self.a10_url="/axapi/v3/delete/cgnv6"
        self.DeviceProxy = ""
        self.fixed_nat = ""
        self.filename = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


