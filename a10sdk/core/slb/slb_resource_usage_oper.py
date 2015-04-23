from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param server_ssl_template_min: {"type": "number", "format": "number"}
    :param fast_tcp_template_default: {"type": "number", "format": "number"}
    :param virtual_port_min: {"type": "number", "format": "number"}
    :param service_group_min: {"type": "number", "format": "number"}
    :param nat_pool_addr_min: {"type": "number", "format": "number"}
    :param stream_template_max: {"type": "number", "format": "number"}
    :param real_port_min: {"type": "number", "format": "number"}
    :param virtual_port_default: {"type": "number", "format": "number"}
    :param conn_reuse_template_min: {"type": "number", "format": "number"}
    :param real_port_default: {"type": "number", "format": "number"}
    :param proxy_template_max: {"type": "number", "format": "number"}
    :param http_template_default: {"type": "number", "format": "number"}
    :param http_template_max: {"type": "number", "format": "number"}
    :param real_server_min: {"type": "number", "format": "number"}
    :param client_ssl_template_default: {"type": "number", "format": "number"}
    :param proxy_template_min: {"type": "number", "format": "number"}
    :param persist_srcip_template_min: {"type": "number", "format": "number"}
    :param virtual_server_default: {"type": "number", "format": "number"}
    :param persist_srcip_template_default: {"type": "number", "format": "number"}
    :param stream_template_min: {"type": "number", "format": "number"}
    :param server_ssl_template_default: {"type": "number", "format": "number"}
    :param fast_udp_template_max: {"type": "number", "format": "number"}
    :param nat_pool_addr_default: {"type": "number", "format": "number"}
    :param virtual_port_max: {"type": "number", "format": "number"}
    :param proxy_template_default: {"type": "number", "format": "number"}
    :param persist_cookie_template_min: {"type": "number", "format": "number"}
    :param service_group_max: {"type": "number", "format": "number"}
    :param client_ssl_template_min: {"type": "number", "format": "number"}
    :param fast_tcp_template_min: {"type": "number", "format": "number"}
    :param fast_tcp_template_max: {"type": "number", "format": "number"}
    :param client_ssl_template_max: {"type": "number", "format": "number"}
    :param stream_template_default: {"type": "number", "format": "number"}
    :param fast_udp_template_min: {"type": "number", "format": "number"}
    :param server_ssl_template_max: {"type": "number", "format": "number"}
    :param persist_srcip_template_max: {"type": "number", "format": "number"}
    :param conn_reuse_template_max: {"type": "number", "format": "number"}
    :param persist_cookie_template_default: {"type": "number", "format": "number"}
    :param http_template_min: {"type": "number", "format": "number"}
    :param fast_udp_template_default: {"type": "number", "format": "number"}
    :param virtual_server_max: {"type": "number", "format": "number"}
    :param service_group_default: {"type": "number", "format": "number"}
    :param real_server_default: {"type": "number", "format": "number"}
    :param real_port_max: {"type": "number", "format": "number"}
    :param nat_pool_addr_max: {"type": "number", "format": "number"}
    :param real_server_max: {"type": "number", "format": "number"}
    :param conn_reuse_template_default: {"type": "number", "format": "number"}
    :param persist_cookie_template_max: {"type": "number", "format": "number"}
    :param virtual_server_min: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.server_ssl_template_min = ""
        self.fast_tcp_template_default = ""
        self.virtual_port_min = ""
        self.service_group_min = ""
        self.nat_pool_addr_min = ""
        self.stream_template_max = ""
        self.real_port_min = ""
        self.virtual_port_default = ""
        self.conn_reuse_template_min = ""
        self.real_port_default = ""
        self.proxy_template_max = ""
        self.http_template_default = ""
        self.http_template_max = ""
        self.real_server_min = ""
        self.client_ssl_template_default = ""
        self.proxy_template_min = ""
        self.persist_srcip_template_min = ""
        self.virtual_server_default = ""
        self.persist_srcip_template_default = ""
        self.stream_template_min = ""
        self.server_ssl_template_default = ""
        self.fast_udp_template_max = ""
        self.nat_pool_addr_default = ""
        self.virtual_port_max = ""
        self.proxy_template_default = ""
        self.persist_cookie_template_min = ""
        self.service_group_max = ""
        self.client_ssl_template_min = ""
        self.fast_tcp_template_min = ""
        self.fast_tcp_template_max = ""
        self.client_ssl_template_max = ""
        self.stream_template_default = ""
        self.fast_udp_template_min = ""
        self.server_ssl_template_max = ""
        self.persist_srcip_template_max = ""
        self.conn_reuse_template_max = ""
        self.persist_cookie_template_default = ""
        self.http_template_min = ""
        self.fast_udp_template_default = ""
        self.virtual_server_max = ""
        self.service_group_default = ""
        self.real_server_default = ""
        self.real_port_max = ""
        self.nat_pool_addr_max = ""
        self.real_server_max = ""
        self.conn_reuse_template_default = ""
        self.persist_cookie_template_max = ""
        self.virtual_server_min = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ResourceUsage(A10BaseClass):
    
    """Class Description::
    Operational Status for the object resource-usage.

    Class resource-usage supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/resource-usage/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "resource-usage"
        self.a10_url="/axapi/v3/slb/resource-usage/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


