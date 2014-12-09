from a10sdk.common.A10BaseClass import A10BaseClass


class AdminSessionConnect(A10BaseClass):
    
    """    :param device: {"description": "Device (Device ID)", "format": "number", "type": "number", "maximum": 8, "minimum": 1, "optional": true}
    :param active_vrid: {"description": "VRRP vrid (Specify VRRP-A vrid)", "format": "number", "type": "number", "maximum": 31, "minimum": 0, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Which target device to manage.

    Class admin-session-connect supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vcs/admin-session-connect`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "admin-session-connect"
        self.a10_url="/axapi/v3/vcs/admin-session-connect"
        self.DeviceProxy = ""
        self.device = ""
        self.active_vrid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


