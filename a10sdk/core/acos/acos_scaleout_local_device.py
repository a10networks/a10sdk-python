from a10sdk.common.A10BaseClass import A10BaseClass


class LocalDevice(A10BaseClass):
    
    """Class Description::
    Local device configuration.

    Class local-device supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param acos_scaleout_rev_mac: {"optional": true, "type": "string", "format": "mac-address"}
    :param acos_scaleout_mac: {"optional": true, "type": "string", "format": "mac-address"}
    :param priority: {"optional": true, "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param acos_scaleout_ip: {"optional": true, "type": "string", "format": "ipv4-address"}
    :param acos_scaleout_rev_ip: {"optional": true, "type": "string", "format": "ipv4-address"}
    :param id: {"optional": true, "minimum": 1, "type": "number", "maximum": 64, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/acos-scaleout/local-device`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "local-device"
        self.a10_url="/axapi/v3/acos-scaleout/local-device"
        self.DeviceProxy = ""
        self.acos_scaleout_rev_mac = ""
        self.acos_scaleout_mac = ""
        self.priority = ""
        self.acos_scaleout_ip = ""
        self.acos_scaleout_rev_ip = ""
        self.A10WW_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


