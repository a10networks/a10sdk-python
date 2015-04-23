from a10sdk.common.A10BaseClass import A10BaseClass


class Sip(A10BaseClass):
    
    """Class Description::
    SIP type.

    Class sip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param sip: {"default": 0, "optional": true, "type": "number", "description": "SIP type", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param register: {"default": 0, "optional": true, "type": "number", "description": "Send SIP REGISTER message, default is to send OPTION message", "format": "flag"}
    :param expect_response_code: {"description": "Specify accepted response codes (e.g. 200, 400-430, any) (Format is xxx,xxx-xxx,any (xxx between [100,899]))", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param sip_port: {"description": "Specify the SIP port, default is 5060 (Port Number)", "format": "number", "default": 5060, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param sip_tcp: {"default": 0, "optional": true, "type": "number", "description": "Use TCP for transmission, default is UDP", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/sip`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sip"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/sip"
        self.DeviceProxy = ""
        self.sip = ""
        self.uuid = ""
        self.register = ""
        self.expect_response_code = ""
        self.sip_port = ""
        self.sip_tcp = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


