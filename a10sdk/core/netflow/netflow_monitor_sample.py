from a10sdk.common.A10BaseClass import A10BaseClass


class Sample(A10BaseClass):
    
    """Class Description::
    Configure filters for monitoring traffic (All traffic is monitored if no filters configured).

    Class sample supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ve_list: {"minItems": 1, "items": {"type": "ve"}, "uniqueItems": true, "array": [{"required": ["ve-num"], "properties": {"ve-num": {"description": "VE interface number", "format": "number", "optional": false, "maximum": 4094, "minimum": 2, "type": "number", "$ref": "/axapi/v3/interface/ve"}}}], "type": "array", "$ref": "/axapi/v3/netflow/monitor/{name}/sample/ve/{ve-num}"}
    :param nat_pool_list: {"minItems": 1, "items": {"type": "nat-pool"}, "uniqueItems": true, "array": [{"required": ["pool-name"], "properties": {"pool-name": {"description": "Name of nat pool", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/netflow/monitor/{name}/sample/nat-pool/{pool-name}"}
    :param ethernet_list: {"minItems": 1, "items": {"type": "ethernet"}, "uniqueItems": true, "array": [{"required": ["ifindex"], "properties": {"ifindex": {"optional": false, "$ref": "/axapi/v3/interface/ethernet", "type": "number", "description": "Ethernet interface number", "format": "interface"}}}], "type": "array", "$ref": "/axapi/v3/netflow/monitor/{name}/sample/ethernet/{ifindex}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/netflow/monitor/{name}/sample`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sample"
        self.a10_url="/axapi/v3/netflow/monitor/{name}/sample"
        self.DeviceProxy = ""
        self.ve_list = []
        self.nat_pool_list = []
        self.ethernet_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


