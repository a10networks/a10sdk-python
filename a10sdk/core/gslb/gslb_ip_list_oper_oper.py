from a10sdk.common.A10BaseClass import A10BaseClass


class IpListOper(A10BaseClass):
    
    """Class Description::
    Operational Status for the object ip-list-oper.

    Class ip-list-oper supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/ip-list-oper/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ip-list-oper"
        self.a10_url="/axapi/v3/gslb/ip-list-oper/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


