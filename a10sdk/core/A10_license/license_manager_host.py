from a10sdk.common.A10BaseClass import A10BaseClass


class Host(A10BaseClass):
    
    """Class Description::
    Configure license manager host.

    Class host supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param host_ipv4: {"description": "license server ip address (length:1-31)", "format": "host", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param port: {"description": "Configure the license manager port, default is 443", "format": "number", "default": 443, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/license-manager/host/{host_ipv4}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "host_ipv4"]

        self.b_key = "host"
        self.a10_url="/axapi/v3/license-manager/host/{host_ipv4}"
        self.DeviceProxy = ""
        self.host_ipv4 = ""
        self.port = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


