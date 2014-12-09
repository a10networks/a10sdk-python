from a10sdk.common.A10BaseClass import A10BaseClass


class BwList(A10BaseClass):
    
    """    :param file_name: {"description": "Blacklist/whitelist Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Blacklist/whitelist.

    Class bw-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/delete/bw-list`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "bw-list"
        self.a10_url="/axapi/v3/delete/bw-list"
        self.DeviceProxy = ""
        self.file_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


