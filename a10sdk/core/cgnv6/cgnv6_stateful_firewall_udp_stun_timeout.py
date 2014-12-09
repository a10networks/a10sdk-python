from a10sdk.common.A10BaseClass import A10BaseClass


class StunTimeout(A10BaseClass):
    
    """Class Description::
    Set STUN timeout for endpoint-independent filtering.

    Class stun-timeout supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param stun_timeout_val_port_range: {"description": "STUN timeout (default: 2 minutes)", "format": "number", "default": 2, "optional": true, "maximum": 60, "minimum": 0, "type": "number"}
    :param port: {"description": "Single Destination Port or Port Range Start", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param port_end: {"description": "Port Range End", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/udp/stun-timeout/{port}+{port_end}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port","port_end"]

        self.b_key = "stun-timeout"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/udp/stun-timeout/{port}+{port_end}"
        self.DeviceProxy = ""
        self.stun_timeout_val_port_range = ""
        self.port = ""
        self.port_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


