from a10sdk.common.A10BaseClass import A10BaseClass


class ClusterConfig(A10BaseClass):
    
    """Class Description::
    Cluster configuration.

    Class cluster-config supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param device_id: {"description": "Enter the device-id to gracefully shutdown", "format": "number", "type": "number", "maximum": 64, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/acos-scaleout/cluster-config`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "cluster-config"
        self.a10_url="/axapi/v3/acos-scaleout/cluster-config"
        self.DeviceProxy = ""
        self.device_id = ""
        self.device_groups = {}
        self.cluster_devices = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


