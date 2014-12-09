from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv6(A10BaseClass):
    
    """Class Description::
    Configure sFlow IPv6 collector.

    Class ipv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param addr: {"optional": false, "type": "string", "description": "Configure sFlow collector IPv6 address", "format": "ipv6-address"}
    :param port: {"description": "Port number (default is 6343)", "format": "number", "default": 6343, "optional": false, "maximum": 65535, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/sflow/collector/ipv6/{addr}+{port}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "addr","port"]

        self.b_key = "ipv6"
        self.a10_url="/axapi/v3/sflow/collector/ipv6/{addr}+{port}"
        self.DeviceProxy = ""
        self.addr = ""
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


