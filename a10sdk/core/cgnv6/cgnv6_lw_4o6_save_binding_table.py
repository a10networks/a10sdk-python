from a10sdk.common.A10BaseClass import A10BaseClass


class SaveBindingTable(A10BaseClass):
    
    """Class Description::
    Save LW-4over6 binding table.

    Class save-binding-table supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lw-4o6/save-binding-table`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "save-binding-table"
        self.a10_url="/axapi/v3/cgnv6/lw-4o6/save-binding-table"
        self.DeviceProxy = ""
        
        for keys, value in kwargs.items():
            setattr(self,keys, value)


