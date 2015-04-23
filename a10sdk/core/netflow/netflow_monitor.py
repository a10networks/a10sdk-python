from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "packets-sent", "bytes-sent", "nat44-records-sent", "nat44-records-sent-failure", "nat64-records-sent", "nat64-records-sent-failure", "dslite-records-sent", "dslite-records-sent-failure", "session-event-nat44-records-sent", "session-event-nat44-records-sent-failure", "session-event-nat64-records-sent", "session-event-nat64-records-sent-failure", "session-event-dslite-records-sent", "session-event-dslite-records-sent-failure", "port-mapping-nat44-records-sent", "port-mapping-nat44-records-sent-failure", "port-mapping-nat64-records-sent", "port-mapping-nat64-records-sent-failure", "port-mapping-dslite-records-sent", "port-mapping-dslite-records-sent-failure", "netflow-v5-records-sent", "netflow-v5-records-sent-failure", "netflow-v5-ext-records-sent", "netflow-v5-ext-records-sent-failure"], "type": "string", "description": "'all': all; 'packets-sent': packets-sent; 'bytes-sent': bytes-sent; 'nat44-records-sent': nat44-records-sent; 'nat44-records-sent-failure': nat44-records-sent-failure; 'nat64-records-sent': nat64-records-sent; 'nat64-records-sent-failure': nat64-records-sent-failure; 'dslite-records-sent': dslite-records-sent; 'dslite-records-sent-failure': dslite-records-sent-failure; 'session-event-nat44-records-sent': session-event-nat44-records-sent; 'session-event-nat44-records-sent-failure': session-event-nat44-records-sent-failure; 'session-event-nat64-records-sent': session-event-nat64-records-sent; 'session-event-nat64-records-sent-failure': session-event-nat64-records-sent-failure; 'session-event-dslite-records-sent': session-event-dslite-records-sent; 'session-event-dslite-records-sent-failure': session-event-dslite-records-sent-failure; 'port-mapping-nat44-records-sent': port-mapping-nat44-records-sent; 'port-mapping-nat44-records-sent-failure': port-mapping-nat44-records-sent-failure; 'port-mapping-nat64-records-sent': port-mapping-nat64-records-sent; 'port-mapping-nat64-records-sent-failure': port-mapping-nat64-records-sent-failure; 'port-mapping-dslite-records-sent': port-mapping-dslite-records-sent; 'port-mapping-dslite-records-sent-failure': port-mapping-dslite-records-sent-failure; 'netflow-v5-records-sent': netflow-v5-records-sent; 'netflow-v5-records-sent-failure': netflow-v5-records-sent-failure; 'netflow-v5-ext-records-sent': netflow-v5-ext-records-sent; 'netflow-v5-ext-records-sent-failure': netflow-v5-ext-records-sent-failure; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Monitor(A10BaseClass):
    
    """Class Description::
    Configure NetFlow Monitor.

    Class monitor supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param source_ip_use_mgmt: {"default": 0, "optional": true, "type": "number", "description": "Use management interface's IP address for source ip of netflow packets", "format": "flag"}
    :param protocol: {"description": "'v9': Netflow version 9; 'v10': Netflow version 10 (IPFIX); ", "format": "enum", "default": "v9", "type": "string", "enum": ["v9", "v10"], "optional": true}
    :param name: {"description": "Name of netflow monitor", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "packets-sent", "bytes-sent", "nat44-records-sent", "nat44-records-sent-failure", "nat64-records-sent", "nat64-records-sent-failure", "dslite-records-sent", "dslite-records-sent-failure", "session-event-nat44-records-sent", "session-event-nat44-records-sent-failure", "session-event-nat64-records-sent", "session-event-nat64-records-sent-failure", "session-event-dslite-records-sent", "session-event-dslite-records-sent-failure", "port-mapping-nat44-records-sent", "port-mapping-nat44-records-sent-failure", "port-mapping-nat64-records-sent", "port-mapping-nat64-records-sent-failure", "port-mapping-dslite-records-sent", "port-mapping-dslite-records-sent-failure", "netflow-v5-records-sent", "netflow-v5-records-sent-failure", "netflow-v5-ext-records-sent", "netflow-v5-ext-records-sent-failure"], "type": "string", "description": "'all': all; 'packets-sent': packets-sent; 'bytes-sent': bytes-sent; 'nat44-records-sent': nat44-records-sent; 'nat44-records-sent-failure': nat44-records-sent-failure; 'nat64-records-sent': nat64-records-sent; 'nat64-records-sent-failure': nat64-records-sent-failure; 'dslite-records-sent': dslite-records-sent; 'dslite-records-sent-failure': dslite-records-sent-failure; 'session-event-nat44-records-sent': session-event-nat44-records-sent; 'session-event-nat44-records-sent-failure': session-event-nat44-records-sent-failure; 'session-event-nat64-records-sent': session-event-nat64-records-sent; 'session-event-nat64-records-sent-failure': session-event-nat64-records-sent-failure; 'session-event-dslite-records-sent': session-event-dslite-records-sent; 'session-event-dslite-records-sent-failure': session-event-dslite-records-sent-failure; 'port-mapping-nat44-records-sent': port-mapping-nat44-records-sent; 'port-mapping-nat44-records-sent-failure': port-mapping-nat44-records-sent-failure; 'port-mapping-nat64-records-sent': port-mapping-nat64-records-sent; 'port-mapping-nat64-records-sent-failure': port-mapping-nat64-records-sent-failure; 'port-mapping-dslite-records-sent': port-mapping-dslite-records-sent; 'port-mapping-dslite-records-sent-failure': port-mapping-dslite-records-sent-failure; 'netflow-v5-records-sent': netflow-v5-records-sent; 'netflow-v5-records-sent-failure': netflow-v5-records-sent-failure; 'netflow-v5-ext-records-sent': netflow-v5-ext-records-sent; 'netflow-v5-ext-records-sent-failure': netflow-v5-ext-records-sent-failure; ", "format": "enum"}}}]}
    :param disable: {"default": 0, "optional": true, "type": "number", "description": "Disable this netflow monitor", "format": "flag"}
    :param flow_timeout: {"description": "Configure timeout value to export flow records periodically for long-live session ( Number of minutes: default is 10, 0 means only send flow record when session is deleted)", "format": "number", "default": 10, "optional": true, "maximum": 1440, "minimum": 0, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/netflow/monitor/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "monitor"
        self.a10_url="/axapi/v3/netflow/monitor/{name}"
        self.DeviceProxy = ""
        self.source_ip_use_mgmt = ""
        self.protocol = ""
        self.name = ""
        self.source_address = {}
        self.destination = {}
        self.sample = {}
        self.record = {}
        self.sampling_enable = []
        self.disable = ""
        self.resend_template = {}
        self.flow_timeout = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


