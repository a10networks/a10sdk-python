from a10sdk.common.A10BaseClass import A10BaseClass


class Partition(A10BaseClass):
    
    """    :param partition_name: {"description": "Object partition name", "format": "string", "minLength": 1, "optional": true, "maxLength": 14, "type": "string"}
    :param id: {"description": "Specify unique Partition id", "format": "number", "optional": true, "maximum": 127, "minimum": 1, "modify-not-allowed": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    hard delete a partition.

    Class partition supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/delete/partition`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "partition"
        self.a10_url="/axapi/v3/delete/partition"
        self.DeviceProxy = ""
        self.partition_name = ""
        self.A10WW_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


