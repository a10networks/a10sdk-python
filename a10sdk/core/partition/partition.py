from a10sdk.common.A10BaseClass import A10BaseClass


class Partition(A10BaseClass):
    
    """Class Description::
    Create/unload a Network partition.

    Class partition supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param partition_name: {"description": "Object partition name", "format": "string", "minLength": 1, "optional": false, "maxLength": 14, "type": "string"}
    :param application_type: {"optional": true, "enum": ["adc", "cgnv6"], "type": "string", "description": "'adc': Application type ADC; 'cgnv6': Application type CGNv6; ", "format": "enum"}
    :param id: {"description": "Specify unique Partition id", "format": "number", "optional": true, "maximum": 127, "minimum": 1, "modify-not-allowed": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/partition/{partition_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "partition_name"]

        self.b_key = "partition"
        self.a10_url="/axapi/v3/partition/{partition_name}"
        self.DeviceProxy = ""
        self.partition_name = ""
        self.application_type = ""
        self.A10WW_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


