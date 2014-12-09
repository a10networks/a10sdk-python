from a10sdk.common.A10BaseClass import A10BaseClass


class PriorityPartition(A10BaseClass):
    
    """Class Description::
    Configure partition to always poll for techreport.

    Class priority-partition supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param part_name: {"description": "Name of partition always want to show in showtech (shared is always shown by default)", "format": "string", "minLength": 1, "optional": false, "maxLength": 14, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/techreport/priority-partition/{part_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "part_name"]

        self.b_key = "priority-partition"
        self.a10_url="/axapi/v3/techreport/priority-partition/{part_name}"
        self.DeviceProxy = ""
        self.part_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


