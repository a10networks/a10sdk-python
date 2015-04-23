from a10sdk.common.A10BaseClass import A10BaseClass


class Record(A10BaseClass):
    
    """Class Description::
    Configure record types to be exported.

    Class record supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param sesn_event_nat64: {"optional": true, "enum": ["both", "creation", "deletion"], "type": "string", "description": "'both': Export both creation and deletion events; 'creation': Export only creation events; 'deletion': Export only deletion events; ", "format": "enum"}
    :param nat64: {"default": 0, "optional": true, "type": "number", "description": "NAT64 Flow Record Template", "format": "flag"}
    :param dslite: {"default": 0, "optional": true, "type": "number", "description": "DS-Lite Flow Record Template", "format": "flag"}
    :param nat44: {"default": 0, "optional": true, "type": "number", "description": "NAT44 Flow Record Template", "format": "flag"}
    :param netflow_v5_ext: {"default": 0, "optional": true, "type": "number", "description": "Extended NetFlow V5 Flow Record Template, supports ipv6", "format": "flag"}
    :param port_mapping_nat64: {"optional": true, "enum": ["both", "creation", "deletion"], "type": "string", "description": "'both': Export both creation and deletion events; 'creation': Export only creation events; 'deletion': Export only deletion events; ", "format": "enum"}
    :param sesn_event_dslite: {"optional": true, "enum": ["both", "creation", "deletion"], "type": "string", "description": "'both': Export both creation and deletion events; 'creation': Export only creation events; 'deletion': Export only deletion events; ", "format": "enum"}
    :param sesn_event_nat44: {"optional": true, "enum": ["both", "creation", "deletion"], "type": "string", "description": "'both': Export both creation and deletion events; 'creation': Export only creation events; 'deletion': Export only deletion events; ", "format": "enum"}
    :param netflow_v5: {"default": 0, "optional": true, "type": "number", "description": "NetFlow V5 Flow Record Template", "format": "flag"}
    :param port_mapping_dslite: {"optional": true, "enum": ["both", "creation", "deletion"], "type": "string", "description": "'both': Export both creation and deletion events; 'creation': Export only creation events; 'deletion': Export only deletion events; ", "format": "enum"}
    :param port_mapping_nat44: {"optional": true, "enum": ["both", "creation", "deletion"], "type": "string", "description": "'both': Export both creation and deletion events; 'creation': Export only creation events; 'deletion': Export only deletion events; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/netflow/monitor/{name}/record`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "record"
        self.a10_url="/axapi/v3/netflow/monitor/{name}/record"
        self.DeviceProxy = ""
        self.uuid = ""
        self.sesn_event_nat64 = ""
        self.nat64 = ""
        self.dslite = ""
        self.nat44 = ""
        self.netflow_v5_ext = ""
        self.port_mapping_nat64 = ""
        self.sesn_event_dslite = ""
        self.sesn_event_nat44 = ""
        self.netflow_v5 = ""
        self.port_mapping_dslite = ""
        self.port_mapping_nat44 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


