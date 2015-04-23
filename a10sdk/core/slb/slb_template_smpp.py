from a10sdk.common.A10BaseClass import A10BaseClass


class Smpp(A10BaseClass):
    
    """Class Description::
    SMPP template.

    Class smpp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "SMPP Template Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param server_enquire_link: {"default": 0, "optional": true, "type": "number", "description": "Send server ENQUIRE_LINK packet for every persist connection when enable conn-reuse", "format": "flag"}
    :param server_selection_per_request: {"default": 0, "optional": true, "type": "number", "description": "Force server selection on every SMPP request when enable conn-reuse", "format": "flag"}
    :param client_enquire_link: {"default": 0, "optional": true, "type": "number", "description": "Respond client ENQUIRE_LINK packet directly instead of forwarding to server", "format": "flag"}
    :param server_enquire_link_val: {"description": "Set interval of keep-alive packet for each persistent connection (second, default is 30)", "format": "number", "default": 30, "optional": true, "maximum": 300, "minimum": 5, "type": "number"}
    :param user: {"description": "Configure the user to bind (The name used to bind)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param password: {"description": "Configure the password used to bind", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/smpp/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "smpp"
        self.a10_url="/axapi/v3/slb/template/smpp/{name}"
        self.DeviceProxy = ""
        self.name = ""
        self.server_enquire_link = ""
        self.server_selection_per_request = ""
        self.client_enquire_link = ""
        self.server_enquire_link_val = ""
        self.user = ""
        self.password = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


