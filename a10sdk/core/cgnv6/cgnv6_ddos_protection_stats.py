from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip_other_block_alloc: {"optional": true, "size": "8", "type": "number", "oid": "17", "format": "counter"}
    :param entry_match_drop: {"optional": true, "size": "8", "type": "number", "oid": "6", "format": "counter"}
    :param ip_port_block_free: {"optional": true, "size": "8", "type": "number", "oid": "15", "format": "counter"}
    :param ip_node_alloc_failure: {"optional": true, "size": "8", "type": "number", "oid": "13", "format": "counter"}
    :param entry_list_alloc_failure: {"optional": true, "size": "8", "type": "number", "oid": "10", "format": "counter"}
    :param ip_node_alloc: {"optional": true, "size": "8", "type": "number", "oid": "11", "format": "counter"}
    :param entry_added_shadow: {"optional": true, "size": "8", "type": "number", "oid": "20", "format": "counter"}
    :param ip_port_block_alloc_failure: {"optional": true, "size": "8", "type": "number", "oid": "16", "format": "counter"}
    :param ip_other_block_alloc_failure: {"optional": true, "size": "8", "type": "number", "oid": "19", "format": "counter"}
    :param entry_removed_from_hw: {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}
    :param entry_deleted: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
    :param entry_list_alloc: {"optional": true, "size": "8", "type": "number", "oid": "8", "format": "counter"}
    :param entry_list_free: {"optional": true, "size": "8", "type": "number", "oid": "9", "format": "counter"}
    :param entry_added_to_hw: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
    :param ip_node_free: {"optional": true, "size": "8", "type": "number", "oid": "12", "format": "counter"}
    :param entry_added: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param ip_other_block_free: {"optional": true, "size": "8", "type": "number", "oid": "18", "format": "counter"}
    :param entry_invalidated: {"optional": true, "size": "8", "type": "number", "oid": "21", "format": "counter"}
    :param ip_port_block_alloc: {"optional": true, "size": "8", "type": "number", "oid": "14", "format": "counter"}
    :param entry_match_drop_hw: {"optional": true, "size": "8", "type": "number", "oid": "7", "format": "counter"}
    :param hw_out_of_entries: {"optional": true, "size": "8", "type": "number", "oid": "5", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.ip_other_block_alloc = ""
        self.entry_match_drop = ""
        self.ip_port_block_free = ""
        self.ip_node_alloc_failure = ""
        self.entry_list_alloc_failure = ""
        self.ip_node_alloc = ""
        self.entry_added_shadow = ""
        self.ip_port_block_alloc_failure = ""
        self.ip_other_block_alloc_failure = ""
        self.entry_removed_from_hw = ""
        self.entry_deleted = ""
        self.entry_list_alloc = ""
        self.entry_list_free = ""
        self.entry_added_to_hw = ""
        self.ip_node_free = ""
        self.entry_added = ""
        self.ip_other_block_free = ""
        self.entry_invalidated = ""
        self.ip_port_block_alloc = ""
        self.entry_match_drop_hw = ""
        self.hw_out_of_entries = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DdosProtection(A10BaseClass):
    
    """Class Description::
    Statistics for the object ddos-protection.

    Class ddos-protection supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/ddos-protection/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ddos-protection"
        self.a10_url="/axapi/v3/cgnv6/ddos-protection/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


