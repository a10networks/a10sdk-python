from a10sdk.common.A10BaseClass import A10BaseClass


class IpNatRedist(A10BaseClass):
    
    """Class Description::
    IP NAT redistribution.

    Class ip-nat-redist supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param metric_ip_nat: {"description": "OSPF default metric. help-val OSPF metric", "format": "number", "type": "number", "maximum": 16777214, "minimum": 0, "optional": true}
    :param route_map_ip_nat: {"description": "Route map reference. help-val Pointer to route-map entries", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param tag_ip_nat: {"optional": true, "type": "number", "description": "Set tag for routes redistributed into OSPF. help-val 32-bit tag value", "format": "number"}
    :param metric_type_ip_nat: {"description": "1: \"Set OSPF External Type 1 metrics\"; 2: \"Set OSPF External Type 2 metrics\"; ", "format": "enum", "default": "2", "type": "string", "enum": ["1", "2"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ospf/{process_id}/redistribute/ip-nat/ip-nat-redist`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ip-nat-redist"
        self.a10_url="/axapi/v3/router/ospf/{process_id}/redistribute/ip-nat/ip-nat-redist"
        self.DeviceProxy = ""
        self.metric_ip_nat = ""
        self.route_map_ip_nat = ""
        self.tag_ip_nat = ""
        self.metric_type_ip_nat = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


