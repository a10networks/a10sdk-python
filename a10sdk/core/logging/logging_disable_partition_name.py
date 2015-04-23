from a10sdk.common.A10BaseClass import A10BaseClass


class DisablePartitionName(A10BaseClass):
    
    """Class Description::
    .

    Class disable-partition-name supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param disable_partition_name: {"description": "Disable partition name in logs", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/disable-partition-name`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "disable-partition-name"
        self.a10_url="/axapi/v3/logging/disable-partition-name"
        self.DeviceProxy = ""
        self.disable_partition_name = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


