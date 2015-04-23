from a10sdk.common.A10BaseClass import A10BaseClass


class Slb(A10BaseClass):
    
    """Class Description::
    Enable SLB group traps.

    Class slb supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param all: {"default": 0, "optional": true, "type": "number", "description": "Enable all SLB traps", "format": "flag"}
    :param server_down: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB server-down trap", "format": "flag"}
    :param vip_port_connratelimit: {"default": 0, "optional": true, "type": "number", "description": "Enable the virtual port reach conn-rate-limit trap", "format": "flag"}
    :param server_selection_failure: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB server selection failure trap", "format": "flag"}
    :param service_group_down: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB service-group-down trap", "format": "flag"}
    :param server_conn_limit: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB server connection limit trap", "format": "flag"}
    :param service_group_member_up: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB service-group-member-up trap", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param server_conn_resume: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB server connection resume trap", "format": "flag"}
    :param service_up: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB service-up trap", "format": "flag"}
    :param service_conn_limit: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB service connection limit trap", "format": "flag"}
    :param service_group_up: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB service-group-up trap", "format": "flag"}
    :param application_buffer_limit: {"default": 0, "optional": true, "type": "number", "description": "Enable application buffer reach limit trap", "format": "flag"}
    :param vip_connratelimit: {"default": 0, "optional": true, "type": "number", "description": "Enable the virtual server reach conn-rate-limit trap", "format": "flag"}
    :param vip_connlimit: {"default": 0, "optional": true, "type": "number", "description": "Enable the virtual server reach conn-limit trap", "format": "flag"}
    :param service_group_member_down: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB service-group-member-down trap", "format": "flag"}
    :param service_down: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB service-down trap", "format": "flag"}
    :param server_disabled: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB server-disabled trap", "format": "flag"}
    :param server_up: {"default": 0, "optional": true, "type": "number", "description": "Enable slb server up trap", "format": "flag"}
    :param vip_port_connlimit: {"default": 0, "optional": true, "type": "number", "description": "Enable the virtual port reach conn-limit trap", "format": "flag"}
    :param vip_port_down: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB virtual port down trap", "format": "flag"}
    :param vip_up: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB virtual server up trap", "format": "flag"}
    :param vip_port_up: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB virtual port up trap", "format": "flag"}
    :param vip_down: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB virtual server down trap", "format": "flag"}
    :param service_conn_resume: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB service connection resume trap", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/enable/traps/slb`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "slb"
        self.a10_url="/axapi/v3/snmp-server/enable/traps/slb"
        self.DeviceProxy = ""
        self.A10WW_all = ""
        self.server_down = ""
        self.vip_port_connratelimit = ""
        self.server_selection_failure = ""
        self.service_group_down = ""
        self.server_conn_limit = ""
        self.service_group_member_up = ""
        self.uuid = ""
        self.server_conn_resume = ""
        self.service_up = ""
        self.service_conn_limit = ""
        self.service_group_up = ""
        self.application_buffer_limit = ""
        self.vip_connratelimit = ""
        self.vip_connlimit = ""
        self.service_group_member_down = ""
        self.service_down = ""
        self.server_disabled = ""
        self.server_up = ""
        self.vip_port_connlimit = ""
        self.vip_port_down = ""
        self.vip_up = ""
        self.vip_port_up = ""
        self.vip_down = ""
        self.service_conn_resume = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


