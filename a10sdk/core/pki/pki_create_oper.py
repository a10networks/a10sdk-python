from a10sdk.common.A10BaseClass import A10BaseClass


class CreateOper(A10BaseClass):
    
    """    :param csr_generate: {"default": 0, "optional": true, "type": "number", "format": "flag"}
    :param division: {"minLength": 1, "maxLength": 63, "type": "string", "optional": true, "format": "string-rlx"}
    :param locality: {"minLength": 1, "maxLength": 63, "type": "string", "optional": true, "format": "string-rlx"}
    :param bits: {"description": "'1024': 1024; '2048': 2048; '4096': 4096; ", "format": "enum", "default": "1024", "type": "string", "enum": ["1024", "2048", "4096"], "optional": true}
    :param state_province: {"minLength": 1, "maxLength": 31, "type": "string", "optional": true, "format": "string-rlx"}
    :param filename: {"minLength": 1, "maxLength": 255, "type": "string", "optional": false, "format": "string"}
    :param common_name: {"minLength": 1, "maxLength": 64, "type": "string", "optional": true, "format": "string-rlx"}
    :param country: {"minLength": 2, "maxLength": 3, "type": "string", "optional": true, "format": "string"}
    :param organization: {"minLength": 1, "maxLength": 63, "type": "string", "optional": true, "format": "string-rlx"}
    :param valid_days: {"format": "number", "default": 730, "type": "number", "maximum": 3650, "minimum": 30, "optional": true}
    :param email: {"minLength": 1, "maxLength": 64, "type": "string", "optional": true, "format": "email-addr"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    .

    Class create-oper supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/pki/create-oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "create-oper"
        self.a10_url="/axapi/v3/pki/create-oper"
        self.DeviceProxy = ""
        self.csr_generate = ""
        self.division = ""
        self.locality = ""
        self.bits = ""
        self.state_province = ""
        self.filename = ""
        self.common_name = ""
        self.country = ""
        self.organization = ""
        self.valid_days = ""
        self.email = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


