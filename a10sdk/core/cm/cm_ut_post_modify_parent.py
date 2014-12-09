from a10sdk.common.A10BaseClass import A10BaseClass


class PostModifyParent(A10BaseClass):
    
    """Class Description::
    Unit test of post modify ineligible.

    Class post-modify-parent supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param k1: {"minLength": 1, "maxLength": 32, "type": "string", "optional": false, "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cm-ut/post-modify-parent/{k1}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "k1"]

        self.b_key = "post-modify-parent"
        self.a10_url="/axapi/v3/cm-ut/post-modify-parent/{k1}"
        self.DeviceProxy = ""
        self.post_modify_child = {}
        self.k1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


