from a10sdk.common.A10BaseClass import A10BaseClass


class HostName(A10BaseClass):
    
    """Class Description::
    Specify IPV6 hosts to receive SNMP traps.

    Class host-name supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param hostname: {"description": "Hostname of SNMP trap host", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param udp_port: {"description": "The trap host's UDP port number(default: 162)", "format": "number", "default": 162, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param v1_v2c_comm: {"description": "SNMPv1/v2c community string", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param user: {"description": "SNMPv3 user to send traps (User Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param version: {"description": "'v1': Use SNMPv1; 'v2c': Use SNMPv2c; 'v3': User SNMPv3; ", "format": "enum", "default": "v2c", "type": "string", "enum": ["v1", "v2c", "v3"], "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/host/host-name/{hostname}+{version}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "hostname","version"]

        self.b_key = "host-name"
        self.a10_url="/axapi/v3/snmp-server/host/host-name/{hostname}+{version}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.hostname = ""
        self.udp_port = ""
        self.v1_v2c_comm = ""
        self.user = ""
        self.version = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


