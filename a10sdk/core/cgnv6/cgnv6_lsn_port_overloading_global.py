from a10sdk.common.A10BaseClass import A10BaseClass


class Global(A10BaseClass):
    
    """Class Description::
    Configure Port-Overloading Behavior.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param unique: {"description": "'destination-address': Allow overloading when the destination addresses is unique; 'destination-address-and-port': Allow overloading when the destination address and port 2-tuple is unique (default); ", "format": "enum", "default": "destination-address-and-port", "type": "string", "enum": ["destination-address", "destination-address-and-port"], "optional": true}
    :param allow_different_user: {"default": 0, "optional": true, "type": "number", "description": "Allow different users to overload the same port (default: disabled)", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/port-overloading/global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/cgnv6/lsn/port-overloading/global"
        self.DeviceProxy = ""
        self.unique = ""
        self.allow_different_user = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


