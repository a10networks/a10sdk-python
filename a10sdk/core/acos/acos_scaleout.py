from a10sdk.common.A10BaseClass import A10BaseClass


class AcosScaleout(A10BaseClass):
    
    """Class Description::
    Configure ACOS Scaleout.

    Class acos-scaleout supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param enable: {"default": 0, "optional": true, "partition-visibility": "private", "type": "number", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/acos-scaleout`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "acos-scaleout"
        self.a10_url="/axapi/v3/acos-scaleout"
        self.DeviceProxy = ""
        self.local_device = {}
        self.enable = ""
        self.cluster_config = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


