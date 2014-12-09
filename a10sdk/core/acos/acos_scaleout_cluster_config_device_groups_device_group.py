from a10sdk.common.A10BaseClass import A10BaseClass


class DeviceGroup(A10BaseClass):
    
    """Class Description::
    configure scaleout device groups.

    Class device-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param device_group: {"description": "scaletout device group", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": false}
    :param device_id_start: {"optional": true, "type": "number", "format": "number"}
    :param device_id_end: {"optional": true, "type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/acos-scaleout/cluster-config/device-groups/device-group/{device_group}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "device_group"]

        self.b_key = "device-group"
        self.a10_url="/axapi/v3/acos-scaleout/cluster-config/device-groups/device-group/{device_group}"
        self.DeviceProxy = ""
        self.device_group = ""
        self.device_id_start = ""
        self.device_id_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


