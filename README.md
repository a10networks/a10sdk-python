# A10 Networks Python Client SDK

A10 github repos:

- [a10-openstack-lbaas](https://github.com/a10networks/a10-openstack-lbaas) - OpenStack LBaaS driver, identical to the files that are currently merged into Juno. Also supports Icehouse. Pypi package 'a10-openstack-lbaas'.
- [a10-openstack-lbaas, havana branch](https://github.com/a10networks/a10-openstack-lbaas/tree/havana) - OpenStack LBaaS driver, for the Havana release. Pypi package 'a10-openstack-lbaas-havana'.
- [a10-neutron-lbaas](https://github.com/a10networks/a10-neutron-lbaas) - Middleware sitting between the openstack driver and our API client, mapping openstack constructs to A10's AxAPI.
- [acos-client](https://github.com/a10networks/acos-client) - AxAPI client used by A10's OpenStack driver.
- [a10sdk-python](https://github.com/a10networks/a10sdk-python) - Alternate AxAPI client.
- [neutron-thirdparty-ci](https://github.com/a10networks/neutron-thirdparty-ci) - Scripts used by our Jenkins/Zuul/Devstack-Gate setup, used to test every openstack code review submission against A10 appliances and our drivers.
- [a10_lbaas_driver](https://github.com/a10networks/a10_lbaas_driver) - An older revision of A10's LBaaS driver; no longer supported.

## Usage

In order to get a session ID for continued use we need to create a `DeviceProxy` object. The DeviceProxy class requires the hostname/IP, port, username, and password.

```python
from a10sdk.common.device_proxy import DeviceProxy
host = "10.48.5.181"
port = 443
username = "admin"
password = "a10"
dp = DeviceProxy(host, port, username, password, use_https=False)
```

#### Example setting up an SLB:

To utilize the sdk you must import the modules for the objects you would like to manage.

```python
from a10sdk.core.slb.slb_virtual_server import VirtualServer
vs = VirtualServer(name='s1', ip_address="1.1.1.1", DeviceProxy=dp)
vs.create()
```

## Contributing

1. Fork it ( http://github.com/a10networks/a10sdk-python/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
