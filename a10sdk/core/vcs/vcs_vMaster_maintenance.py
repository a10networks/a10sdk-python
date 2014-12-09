from a10sdk.common.A10BaseClass import A10BaseClass


class VmasterMaintenance(A10BaseClass):
    
    """    :param vMaster_maintenance: {"description": "the seconds vMaster will be maintained, 60 by default", "format": "number", "default": 60, "optional": true, "maximum": 3600, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    During this period, vMaster can leave and come back to be vMaster again.

    Class vMaster-maintenance supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vcs/vMaster-maintenance`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vMaster-maintenance"
        self.a10_url="/axapi/v3/vcs/vMaster-maintenance"
        self.DeviceProxy = ""
        self.vMaster_maintenance = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


