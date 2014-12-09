from a10sdk.common.A10BaseClass import A10BaseClass


class ObjKey1(A10BaseClass):
    
    """Class Description::
    Unit test of optional key.

    Class obj-key-1 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param k2: {"optional": false, "minimum": 1, "type": "number", "maximum": 32, "format": "number"}
    :param k1: {"minLength": 1, "maxLength": 32, "type": "string", "optional": false, "format": "string"}
    :param d1: {"description": "some data", "format": "string", "minLength": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cm-ut/obj-key-1/{k1}+{k2}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "k1","k2"]

        self.b_key = "obj-key-1"
        self.a10_url="/axapi/v3/cm-ut/obj-key-1/{k1}+{k2}"
        self.DeviceProxy = ""
        self.k2 = ""
        self.k1 = ""
        self.d1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


