from a10sdk.common.A10BaseClass import A10BaseClass


class Options(A10BaseClass):
    
    """Class Description::
    Partition specific overlay-tunnel configuration.

    Class options supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param nvgre_key_mode_lower24: {"default": 0, "optional": true, "type": "number", "description": "Use the lower 24-bits of the GRE key as the VSID", "format": "flag"}
    :param tcp_mss_adjust_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable TCP MSS adjustment in SYN packet for tunnels", "format": "flag"}
    :param gateway_mac: {"optional": true, "type": "string", "description": "MAC to be used with Gateway segment Id (MAC Address for the Gateway segment)", "format": "mac-address"}
    :param ip_dscp_preserve: {"default": 0, "optional": true, "type": "number", "description": "Copy DSCP bits from inner IP to outer IP header", "format": "flag"}
    :param nvgre_disable_flow_id: {"default": 0, "optional": true, "type": "number", "description": "Disable Flow-ID computation for NVGRE", "format": "flag"}
    :param vxlan_dest_port: {"description": "VXLAN UDP Destination Port (UDP Port Number (default 4789))", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/overlay-tunnel/options`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "options"
        self.a10_url="/axapi/v3/overlay-tunnel/options"
        self.DeviceProxy = ""
        self.nvgre_key_mode_lower24 = ""
        self.tcp_mss_adjust_disable = ""
        self.gateway_mac = ""
        self.ip_dscp_preserve = ""
        self.nvgre_disable_flow_id = ""
        self.vxlan_dest_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


