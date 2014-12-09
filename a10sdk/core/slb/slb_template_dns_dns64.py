from a10sdk.common.A10BaseClass import A10BaseClass


class Dns64(A10BaseClass):
    
    """Class Description::
    Enable DNS64.

    Class dns64 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param deep_check_rr_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable Check DNS Response Records", "format": "flag"}
    :param answer_only_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable Only translate the Answer Section", "format": "flag"}
    :param enable: {"default": 0, "optional": true, "type": "number", "description": "Enable DNS64 (Need to config this option before config any other dns64 options)", "format": "flag"}
    :param single_response_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable Single Response which is used to avoid ambiguity", "format": "flag"}
    :param max_qr_length: {"description": "Max Question Record Length, default is 128", "format": "number", "default": 128, "optional": true, "maximum": 1023, "minimum": 1, "type": "number"}
    :param ignore_rcode3_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable Ignore DNS error Response with rcode 3", "format": "flag"}
    :param ttl: {"description": "Specify Max TTL in DNS Response, unit: second", "format": "number", "type": "number", "maximum": 1000000000, "minimum": 1, "optional": true}
    :param auth_data: {"default": 0, "optional": true, "type": "number", "description": "Set AA flag in DNS Response", "format": "flag"}
    :param change_query: {"default": 0, "optional": true, "type": "number", "description": "Always change incoming AAAA DNS Query to A", "format": "flag"}
    :param drop_cname_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable Drop DNS CNAME Response", "format": "flag"}
    :param cache: {"default": 0, "optional": true, "type": "number", "description": "Generate Response by DNS Cache", "format": "flag"}
    :param passive_query_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable Generate A query upon empty or error Response", "format": "flag"}
    :param retry: {"description": "Retry count, default is 3 (Retry Number)", "format": "number", "default": 3, "optional": true, "maximum": 15, "minimum": 0, "type": "number"}
    :param parallel_query: {"default": 0, "optional": true, "type": "number", "description": "Forward AAAA Query & generate A Query in parallel", "format": "flag"}
    :param timeout: {"description": "Timeout to send additional Queries, unit: second, default is 1", "format": "number", "default": 1, "optional": true, "maximum": 15, "minimum": 0, "type": "number"}
    :param compress_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable Always try DNS Compression", "format": "flag"}
    :param trans_ptr_query: {"default": 0, "optional": true, "type": "number", "description": "Translate DNS PTR Query", "format": "flag"}
    :param trans_ptr: {"default": 0, "optional": true, "type": "number", "description": "Translate DNS PTR Records", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/dns/{name}/dns64`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dns64"
        self.a10_url="/axapi/v3/slb/template/dns/{name}/dns64"
        self.DeviceProxy = ""
        self.deep_check_rr_disable = ""
        self.answer_only_disable = ""
        self.enable = ""
        self.single_response_disable = ""
        self.max_qr_length = ""
        self.ignore_rcode3_disable = ""
        self.ttl = ""
        self.auth_data = ""
        self.change_query = ""
        self.drop_cname_disable = ""
        self.cache = ""
        self.passive_query_disable = ""
        self.retry = ""
        self.parallel_query = ""
        self.timeout = ""
        self.compress_disable = ""
        self.trans_ptr_query = ""
        self.trans_ptr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


