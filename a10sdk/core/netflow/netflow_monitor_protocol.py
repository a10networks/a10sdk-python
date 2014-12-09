from a10sdk.common.A10BaseClass import A10BaseClass


class Protocol(A10BaseClass):
    
    """Class Description::
    Configure netflow protocol version to use, default is netflow v9.

    Class protocol supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param version: {"description": "v9: \"Netflow version 9\"; v10: \"Netflow version 10 (IPFIX)\"; ", "format": "enum", "default": "v9", "type": "string", "enum": ["v9", "v10"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/netflow/monitor/{name}/protocol`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "protocol"
        self.a10_url="/axapi/v3/netflow/monitor/{name}/protocol"
        self.DeviceProxy = ""
        self.version = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


