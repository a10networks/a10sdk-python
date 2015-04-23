from a10sdk.common.A10BaseClass import A10BaseClass


class Ip(A10BaseClass):
    
    """Class Description::
    Configure sFlow IPv4 collector.

    Class ip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param addr: {"optional": false, "type": "string", "description": "Configure sFlow collector IP address", "format": "ipv4-address"}
    :param port: {"description": "Port number (default is 6343)", "format": "number", "default": 6343, "optional": false, "maximum": 65535, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/sflow/collector/ip/{addr}+{port}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "addr","port"]

        self.b_key = "ip"
        self.a10_url="/axapi/v3/sflow/collector/ip/{addr}+{port}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.addr = ""
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


