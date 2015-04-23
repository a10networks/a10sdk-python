from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param port_mapping_nat64_records_sent: {"optional": true, "size": "8", "type": "number", "oid": "17", "format": "counter"}
    :param netflow_v5_records_sent: {"optional": true, "size": "8", "type": "number", "oid": "21", "format": "counter"}
    :param port_mapping_nat44_records_sent_failure: {"optional": true, "size": "8", "type": "number", "oid": "16", "format": "counter"}
    :param session_event_nat64_records_sent: {"optional": true, "size": "8", "type": "number", "oid": "11", "format": "counter"}
    :param netflow_v5_ext_records_sent_failure: {"optional": true, "size": "8", "type": "number", "oid": "24", "format": "counter"}
    :param port_mapping_dslite_records_sent_failure: {"optional": true, "size": "8", "type": "number", "oid": "20", "format": "counter"}
    :param session_event_dslite_records_sent: {"optional": true, "size": "8", "type": "number", "oid": "13", "format": "counter"}
    :param netflow_v5_ext_records_sent: {"optional": true, "size": "8", "type": "number", "oid": "23", "format": "counter"}
    :param dslite_records_sent_failure: {"optional": true, "size": "8", "type": "number", "oid": "8", "format": "counter"}
    :param session_event_nat44_records_sent: {"optional": true, "size": "8", "type": "number", "oid": "9", "format": "counter"}
    :param port_mapping_nat64_records_sent_failure: {"optional": true, "size": "8", "type": "number", "oid": "18", "format": "counter"}
    :param nat64_records_sent: {"optional": true, "size": "8", "type": "number", "oid": "5", "format": "counter"}
    :param port_mapping_dslite_records_sent: {"optional": true, "size": "8", "type": "number", "oid": "19", "format": "counter"}
    :param bytes_sent: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
    :param session_event_dslite_records_sent_failure: {"optional": true, "size": "8", "type": "number", "oid": "14", "format": "counter"}
    :param nat44_records_sent_failure: {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}
    :param dslite_records_sent: {"optional": true, "size": "8", "type": "number", "oid": "7", "format": "counter"}
    :param port_mapping_nat44_records_sent: {"optional": true, "size": "8", "type": "number", "oid": "15", "format": "counter"}
    :param session_event_nat44_records_sent_failure: {"optional": true, "size": "8", "type": "number", "oid": "10", "format": "counter"}
    :param session_event_nat64_records_sent_failure: {"optional": true, "size": "8", "type": "number", "oid": "12", "format": "counter"}
    :param nat44_records_sent: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
    :param packets_sent: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param nat64_records_sent_failure: {"optional": true, "size": "8", "type": "number", "oid": "6", "format": "counter"}
    :param netflow_v5_records_sent_failure: {"optional": true, "size": "8", "type": "number", "oid": "22", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.port_mapping_nat64_records_sent = ""
        self.netflow_v5_records_sent = ""
        self.port_mapping_nat44_records_sent_failure = ""
        self.session_event_nat64_records_sent = ""
        self.netflow_v5_ext_records_sent_failure = ""
        self.port_mapping_dslite_records_sent_failure = ""
        self.session_event_dslite_records_sent = ""
        self.netflow_v5_ext_records_sent = ""
        self.dslite_records_sent_failure = ""
        self.session_event_nat44_records_sent = ""
        self.port_mapping_nat64_records_sent_failure = ""
        self.nat64_records_sent = ""
        self.port_mapping_dslite_records_sent = ""
        self.bytes_sent = ""
        self.session_event_dslite_records_sent_failure = ""
        self.nat44_records_sent_failure = ""
        self.dslite_records_sent = ""
        self.port_mapping_nat44_records_sent = ""
        self.session_event_nat44_records_sent_failure = ""
        self.session_event_nat64_records_sent_failure = ""
        self.nat44_records_sent = ""
        self.packets_sent = ""
        self.nat64_records_sent_failure = ""
        self.netflow_v5_records_sent_failure = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Monitor(A10BaseClass):
    
    """Class Description::
    Statistics for the object monitor.

    Class monitor supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Name of netflow monitor", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/netflow/monitor/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "monitor"
        self.a10_url="/axapi/v3/netflow/monitor/{name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


