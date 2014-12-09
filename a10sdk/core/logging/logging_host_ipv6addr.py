from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv6Addr(A10BaseClass):
    
    """Class Description::
    ipv6 address of remote syslog server.

    Class ipv6addr supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param host_ipv6: {"optional": false, "type": "string", "description": "Set syslog host ipv6 address", "format": "ipv6-address"}
    :param tcp: {"description": "Use TCP as transport protocol", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param port: {"description": "Set remote syslog port number", "format": "number", "default": 514, "optional": true, "maximum": 32767, "minimum": 1, "type": "number"}
    :param use_mgmt_port: {"description": "Use management port for connections", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/host/ipv6addr/{host_ipv6}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "host_ipv6"]

        self.b_key = "ipv6addr"
        self.a10_url="/axapi/v3/logging/host/ipv6addr/{host_ipv6}"
        self.DeviceProxy = ""
        self.host_ipv6 = ""
        self.tcp = ""
        self.port = ""
        self.use_mgmt_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


