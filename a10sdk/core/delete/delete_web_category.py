from a10sdk.common.A10BaseClass import A10BaseClass


class WebCategory(A10BaseClass):
    
    """    :param database: {"default": 0, "optional": true, "type": "number", "description": "Delete web-category database", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Delete web-category database.

    Class web-category supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/delete/web-category`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "web-category"
        self.a10_url="/axapi/v3/delete/web-category"
        self.DeviceProxy = ""
        self.database = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


