from a10sdk.common.A10BaseClass import A10BaseClass


class Sync(A10BaseClass):
    
    """    :param all_partitions: {"default": 0, "optional": true, "type": "number", "description": "All partition configurations", "format": "flag"}
    :param partition_name: {"description": "Partition name", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param pwd: {"minLength": 1, "maxLength": 128, "type": "string", "optional": true, "format": "string"}
    :param auto_authentication: {"default": 0, "optional": true, "type": "number", "description": "Authenticate with local username and password", "format": "flag"}
    :param address: {"optional": true, "type": "string", "description": "Specify the destination ip address to sync", "format": "ipv4-address"}
    :param shared: {"default": 0, "optional": true, "type": "number", "description": "Shared partition", "format": "flag"}
    :param type: {"optional": true, "enum": ["running", "all"], "type": "string", "description": "'running': Sync local running to peer's running configuration; 'all': Sync local running to peer's running configuration, and local startup to peer's startup configuration; ", "format": "enum"}
    :param usr: {"minLength": 1, "maxLength": 128, "type": "string", "optional": true, "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Sync operation.

    Class sync supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/configure/sync`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sync"
        self.a10_url="/axapi/v3/configure/sync"
        self.DeviceProxy = ""
        self.all_partitions = ""
        self.partition_name = ""
        self.pwd = ""
        self.auto_authentication = ""
        self.address = ""
        self.shared = ""
        self.A10WW_type = ""
        self.usr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


