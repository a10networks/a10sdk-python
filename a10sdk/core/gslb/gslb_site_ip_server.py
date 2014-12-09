from a10sdk.common.A10BaseClass import A10BaseClass


class IpServer(A10BaseClass):
    
    """Class Description::
    Specify a real server for the GSLB site.

    Class ip-server supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip_server_name: {"description": "Specify the real server name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/gslb/service-ip"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/site/{site_name}/ip-server/{ip_server_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ip_server_name"]

        self.b_key = "ip-server"
        self.a10_url="/axapi/v3/gslb/site/{site_name}/ip-server/{ip_server_name}"
        self.DeviceProxy = ""
        self.ip_server_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


