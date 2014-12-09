from a10sdk.common.A10BaseClass import A10BaseClass


class ClassList(A10BaseClass):
    
    """Class Description::
    Class List.

    Class class-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Class List Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/nat/inside/source/class-list`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "class-list"
        self.a10_url="/axapi/v3/ip/nat/inside/source/class-list"
        self.DeviceProxy = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


