from a10sdk.common.A10BaseClass import A10BaseClass


class PostModifyChild(A10BaseClass):
    
    """Class Description::
    Unit test of post modify ineligible.

    Class post-modify-child supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param f1: {"optional": true, "minimum": 1, "type": "number", "maximum": 32, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cm-ut/post-modify-parent/{k1}/post-modify-child`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "post-modify-child"
        self.a10_url="/axapi/v3/cm-ut/post-modify-parent/{k1}/post-modify-child"
        self.DeviceProxy = ""
        self.f1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


