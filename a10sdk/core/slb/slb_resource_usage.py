from a10sdk.common.A10BaseClass import A10BaseClass


class ResourceUsage(A10BaseClass):
    
    """Class Description::
    Configure SLB Resource Usage.

    Class resource-usage supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param virtual_server_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total Virtual Servers in the System", "format": "number", "optional": true, "type": "number"}
    :param nat_pool_addr_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total configurable NAT Pool addresses in the System", "format": "number", "optional": true, "type": "number"}
    :param fast_tcp_template_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total configurable Fast TCP Templates in the System", "format": "number", "optional": true, "type": "number"}
    :param virtual_port_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total Virtual Server Ports in the System", "format": "number", "optional": true, "type": "number"}
    :param proxy_template_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total configurable Proxy Templates in the System", "format": "number", "optional": true, "type": "number"}
    :param fast_udp_template_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total configurable Fast UDP Templates in the System", "format": "number", "optional": true, "type": "number"}
    :param client_ssl_template_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total configurable Client SSL Templates in the System", "format": "number", "optional": true, "type": "number"}
    :param service_group_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total Service Groups in the System", "format": "number", "optional": true, "type": "number"}
    :param class_list_ipv6_addr_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total IPv6 addresses for class-list", "format": "number", "optional": true, "type": "number"}
    :param stream_template_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total configurable Streaming media in the System", "format": "number", "optional": true, "type": "number"}
    :param conn_reuse_template_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total configurable Connection reuse Templates in the System", "format": "number", "optional": true, "type": "number"}
    :param persist_cookie_template_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total configurable Persistent cookie Templates in the System", "format": "number", "optional": true, "type": "number"}
    :param persist_srcip_template_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total configurable Source IP Persistent Templates in the System", "format": "number", "optional": true, "type": "number"}
    :param server_ssl_template_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total configurable Server SSL Templates in the System", "format": "number", "optional": true, "type": "number"}
    :param real_server_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total Real Servers in the System", "format": "number", "optional": true, "type": "number"}
    :param real_port_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total Real Server Ports in the System", "format": "number", "optional": true, "type": "number"}
    :param http_template_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total configurable HTTP Templates in the System", "format": "number", "optional": true, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/resource-usage`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "resource-usage"
        self.a10_url="/axapi/v3/slb/resource-usage"
        self.DeviceProxy = ""
        self.virtual_server_count = ""
        self.nat_pool_addr_count = ""
        self.fast_tcp_template_count = ""
        self.virtual_port_count = ""
        self.proxy_template_count = ""
        self.fast_udp_template_count = ""
        self.client_ssl_template_count = ""
        self.service_group_count = ""
        self.class_list_ipv6_addr_count = ""
        self.stream_template_count = ""
        self.conn_reuse_template_count = ""
        self.persist_cookie_template_count = ""
        self.persist_srcip_template_count = ""
        self.server_ssl_template_count = ""
        self.real_server_count = ""
        self.real_port_count = ""
        self.http_template_count = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


