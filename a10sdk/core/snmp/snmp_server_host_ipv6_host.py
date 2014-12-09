from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv6Host(A10BaseClass):
    
    """Class Description::
    Specify IPV6 hosts to receive SNMP traps.

    Class ipv6-host supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param udp_port: {"description": "The trap host's UDP port number(default: 162)", "format": "number", "default": 162, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param version: {"description": "'v1': Use SNMPv1; 'v2c': Use SNMPv2c; 'v3': User SNMPv3; ", "format": "enum", "default": "v2c", "type": "string", "enum": ["v1", "v2c", "v3"], "optional": false}
    :param ipv6_addr: {"optional": false, "type": "string", "description": "help IPV4 address of SNMP trap host", "format": "ipv6-address"}
    :param user: {"description": "SNMPv3 user to send traps (User Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param v1_v2c_comm: {"description": "SNMPv1/v2c community string", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/host/ipv6-host/{ipv6_addr}+{version}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv6_addr","version"]

        self.b_key = "ipv6-host"
        self.a10_url="/axapi/v3/snmp-server/host/ipv6-host/{ipv6_addr}+{version}"
        self.DeviceProxy = ""
        self.udp_port = ""
        self.version = ""
        self.ipv6_addr = ""
        self.user = ""
        self.v1_v2c_comm = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


