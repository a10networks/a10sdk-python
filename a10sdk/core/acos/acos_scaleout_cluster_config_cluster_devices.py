from a10sdk.common.A10BaseClass import A10BaseClass


class Devicelist(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param device_id: {"description": "scaletout device id", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param ip: {"type": "string", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "deviceList"
        self.DeviceProxy = ""
        self.device_id = ""
        self.ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ClusterDevices(A10BaseClass):
    
    """Class Description::
    Configure devices in the cluster.

    Class cluster-devices supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param deviceList: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"device-id": {"description": "scaletout device id", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "optional": true, "ip": {"type": "string", "format": "ipv4-address"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/acos-scaleout/cluster-config/cluster-devices`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "cluster-devices"
        self.a10_url="/axapi/v3/acos-scaleout/cluster-config/cluster-devices"
        self.DeviceProxy = ""
        self.deviceList = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


