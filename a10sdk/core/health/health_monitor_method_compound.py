from a10sdk.common.A10BaseClass import A10BaseClass


class Compound(A10BaseClass):
    
    """Class Description::
    Compound type.

    Class compound supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param rpn_string: {"description": "Enter Reverse Polish Notation, example: sub hm1 sub hm2 and", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 512, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param compound: {"default": 0, "optional": true, "type": "number", "description": "Compound type", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/compound`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "compound"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/compound"
        self.DeviceProxy = ""
        self.rpn_string = ""
        self.uuid = ""
        self.compound = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


