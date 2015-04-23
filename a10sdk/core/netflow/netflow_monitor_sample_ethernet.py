from a10sdk.common.A10BaseClass import A10BaseClass


class Ethernet(A10BaseClass):
    
    """Class Description::
    select ethernet interface to monitor.

    Class ethernet supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ifindex: {"optional": false, "$ref": "/axapi/v3/interface/ethernet", "type": "number", "description": "Ethernet interface number", "format": "interface"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/netflow/monitor/{name}/sample/ethernet/{ifindex}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ifindex"]

        self.b_key = "ethernet"
        self.a10_url="/axapi/v3/netflow/monitor/{name}/sample/ethernet/{ifindex}"
        self.DeviceProxy = ""
        self.ifindex = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


