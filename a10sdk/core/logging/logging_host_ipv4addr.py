from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv4Addr(A10BaseClass):
    
    """Class Description::
    host DNS name or ipv4 address of remote syslog server.

    Class ipv4addr supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param tcp: {"description": "Use TCP as transport protocol", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param host_ipv4: {"optional": false, "type": "string", "description": "Set syslog host ip address", "format": "host"}
    :param port: {"description": "Set remote syslog port number", "format": "number", "default": 514, "optional": true, "maximum": 32767, "minimum": 1, "type": "number"}
    :param use_mgmt_port: {"description": "Use management port for connections", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/host/ipv4addr/{host_ipv4}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "host_ipv4"]

        self.b_key = "ipv4addr"
        self.a10_url="/axapi/v3/logging/host/ipv4addr/{host_ipv4}"
        self.DeviceProxy = ""
        self.tcp = ""
        self.host_ipv4 = ""
        self.port = ""
        self.use_mgmt_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


