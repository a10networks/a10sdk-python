from a10sdk.common.A10BaseClass import A10BaseClass


class IdleTimeout(A10BaseClass):
    
    """Class Description::
    Configure TCP established-session idle timeout for IPv4 and IPv6.

    Class idle-timeout supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param idle_timeout_val_port_range: {"description": "Set Idle timeout for IPv4 and IPv6 TCP established sessions (Idle timeout for IPv4 and IPv6 TCP established sessions (default: 300 seconds))", "format": "number", "default": 300, "optional": true, "maximum": 15000, "minimum": 60, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param port: {"description": "Single Destination Port or Port Range Start", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param port_end: {"description": "Port Range End", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/tcp/idle-timeout/{port}+{port_end}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port","port_end"]

        self.b_key = "idle-timeout"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/tcp/idle-timeout/{port}+{port_end}"
        self.DeviceProxy = ""
        self.idle_timeout_val_port_range = ""
        self.uuid = ""
        self.port = ""
        self.port_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


