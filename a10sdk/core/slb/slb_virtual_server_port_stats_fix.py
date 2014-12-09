from a10sdk.common.A10BaseClass import A10BaseClass


class Port(A10BaseClass):
    
    """Class Description::
    Statistics for the object fix.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/virtual-server/{name}/port/{port_number}+{protocol}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port_number","protocol"]

        self.b_key = "port"
        self.a10_url="/axapi/v3/slb/virtual-server/{name}/port/{port_number}+{protocol}/stats"
        self.DeviceProxy = ""
        
        for keys, value in kwargs.items():
            setattr(self,keys, value)


