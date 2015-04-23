from a10sdk.common.A10BaseClass import A10BaseClass


class Tcp(A10BaseClass):
    
    """Class Description::
    Set TCP STUN timeout.

    Class tcp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param port_start: {"description": "Port Range (Port Range Start)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param port_end: {"description": "Port Range (Port Range End)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param timeout: {"description": "STUN timeout in minutes (default: 2 minutes)", "format": "number", "type": "number", "maximum": 60, "minimum": 0, "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/stun-timeout/tcp/{port_start}+{port_end}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port_start","port_end"]

        self.b_key = "tcp"
        self.a10_url="/axapi/v3/cgnv6/lsn/stun-timeout/tcp/{port_start}+{port_end}"
        self.DeviceProxy = ""
        self.port_start = ""
        self.port_end = ""
        self.timeout = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


