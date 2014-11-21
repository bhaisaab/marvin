# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

test_data = {
    "region": {
        "regionid": "2",
        "regionname": "Region2",
        "regionendpoint": "http://region2:8080/client"
    },
    "zone": "NA",
    "hypervisor": "XenServer",
    "deleteDC": True,
    "vdomain": {
            "name": "domain"
    },
    "domain": {"name": "domain"},
    "email": "test@test.com",
    "gateway": "172.1.1.1",
    "netmask": "255.255.255.0",
    "startip": "172.1.1.10",
    "endip": "172.1.1.20",
    "regionid": "1",
    "vlan": "10",
    "isportable": "true",

    "project": {
            "name": "Project",
        "displaytext": "Test project"
    },
    "private_gateway": {
       "ipaddress": "172.16.1.2",
       "gateway": "172.16.1.1",
       "netmask": "255.255.255.0",
       "vlan":"10",
       "name":"test_private_gateway"
    },
    "account": {
        "email": "test-account@test.com",
        "firstname": "test",
        "lastname": "test",
        "username": "test-account",
        "password": "password"
    },
    "account2": {
        "email": "test-account2@test.com",
        "firstname": "test2",
        "lastname": "test2",
        "username": "test-account2",
        "password": "password"
    },
    "vmware_cluster" : {
            "hypervisor": 'VMware',
            "clustertype": 'ExternalManaged',
            "username": 'administrator',
            "password": 'password_123',
            "url": 'http://10.147.60.15/42xescauto spaces/42xesc Clusters',
            "clustername": 'VMWare Cluster with Space in DC name',
        },
    "small": {
        "displayname": "testserver",
        "username": "root",
        "password": "password",
        "ssh_port": 22,
        "hypervisor": "XenServer",
        "privateport": 22,
        "publicport": 22,
        "protocol": 'TCP',
    },
    "medium": {
        "displayname": "testserver",
        "username": "root",
        "password": "password",
        "ssh_port": 22,
        "hypervisor": 'XenServer',
        "privateport": 22,
        "publicport": 22,
        "protocol": 'TCP',
    },
    "service_offering": {
        "name": "Tiny Instance",
        "displaytext": "Tiny Instance",
        "cpunumber": 1,
        "cpuspeed": 100,  # in MHz
        "memory": 128,  # In MBs
    },
    "service_offerings": {
        "name": "Tiny Instance",
        "displaytext": "Tiny Instance",
        "cpunumber": 1,
        "cpuspeed": 100,
        "memory": 128,

        "tiny": {
            "name": "Tiny Instance",
            "displaytext": "Tiny Instance",
            "cpunumber": 1,
            "cpuspeed": 100,
            "memory": 128,
        },
        "small": {
            "name": "Small Instance",
            "displaytext": "Small Instance",
            "cpunumber": 1,
            "cpuspeed": 100,
            "memory": 256
        },
        "medium": {
            "name": "Medium Instance",
            "displaytext": "Medium Instance",
            "cpunumber": 1,
            "cpuspeed": 100,
            "memory": 256,
        },
        "big": {
            "name": "BigInstance",
            "displaytext": "BigInstance",
            "cpunumber": 1,
            "cpuspeed": 100,
            "memory": 512,
        },
        "hasmall": {
            "name": "HA Small Instance",
            "displaytext": "HA Small Instance",
            "cpunumber": 1,
            "cpuspeed": 100,
            "memory": 256,
            "hosttags": "ha",
            "offerha": True,
        },
        "taggedsmall": {
            "name": "Tagged Small Instance",
            "displaytext": "Tagged Small Instance",
            "cpunumber": 1,
            "cpuspeed": 100,
            "memory": 256,
            "hosttags": "vmsync",
        },
    },
    "disk_offering": {
        "name": "Disk offering",
        "displaytext": "Disk offering",
        "disksize": 1
    },
    'resized_disk_offering': {
        "displaytext": "Resized",
        "name": "Resized",
        "disksize": 3
    },
    "network": {
        "name": "Test Network",
        "displaytext": "Test Network",
        "acltype": "Account",
    },
    "network2": {
        "name": "Test Network Shared",
        "displaytext": "Test Network Shared",
        "vlan": 1201,
        "gateway": "172.16.15.1",
        "netmask": "255.255.255.0",
        "startip": "172.16.15.21",
        "endip": "172.16.15.41",
        "acltype": "Account",
    },
    "network_offering": {
        "name": 'Test Network offering',
        "displaytext": 'Test Network offering',
        "guestiptype": 'Isolated',
        "supportedservices": 'Dhcp,Dns,SourceNat,PortForwarding',
        "traffictype": 'GUEST',
        "availability": 'Optional',
        "serviceProviderList": {
                "Dhcp": 'VirtualRouter',
            "Dns": 'VirtualRouter',
            "SourceNat": 'VirtualRouter',
            "PortForwarding": 'VirtualRouter',
        },
    },
    "nw_off_isolated_netscaler": {
                "name": 'Netscaler',
                "displaytext": 'Netscaler',
                "guestiptype": 'Isolated',
                "supportedservices": 'Dhcp,Dns,SourceNat,PortForwarding,Vpn,Firewall,Lb,UserData,StaticNat',
                "traffictype": 'GUEST',
                "availability": 'Optional',
                "serviceProviderList": {
                    "Dhcp": 'VirtualRouter',
                    "Dns": 'VirtualRouter',
                    "SourceNat": 'VirtualRouter',
                    "PortForwarding": 'VirtualRouter',
                    "Vpn": 'VirtualRouter',
                    "Firewall": 'VirtualRouter',
                    "Lb": 'Netscaler',
                    "UserData": 'VirtualRouter',
                    "StaticNat": 'VirtualRouter',
                },
    },
    "nw_off_isolated_persistent": {
        "name": 'Test Nw off isolated persistent',
        "displaytext": 'Test Nw off isolated persistent',
        "guestiptype": 'Isolated',
        "supportedservices": 'Dhcp,Dns,SourceNat,PortForwarding',
        "traffictype": 'GUEST',
        "ispersistent": 'True',
        "availability": 'Optional',
        "serviceProviderList": {
                "Dhcp": 'VirtualRouter',
            "Dns": 'VirtualRouter',
            "SourceNat": 'VirtualRouter',
            "PortForwarding": 'VirtualRouter',
        },
    },
    "nw_off_isolated_persistent_lb": {
        "name": 'Test Nw off isolated persistent',
        "displaytext": 'Test Nw off isolated persistent',
        "guestiptype": 'Isolated',
        "supportedservices": 'Dhcp,Dns,SourceNat,PortForwarding,Lb',
        "traffictype": 'GUEST',
        "ispersistent": 'True',
        "availability": 'Optional',
        "serviceProviderList": {
            "Dhcp": 'VirtualRouter',
            "Dns": 'VirtualRouter',
            "SourceNat": 'VirtualRouter',
            "PortForwarding": 'VirtualRouter',
	    "Lb": "VirtualRouter"
        },
    },
    "isolated_network_offering": {
        "name": "Network offering-DA services",
        "displaytext": "Network offering-DA services",
        "guestiptype": "Isolated",
        "supportedservices":
        "Dhcp,Dns,SourceNat,PortForwarding,Vpn,Firewall,Lb,UserData,StaticNat",
        "traffictype": "GUEST",
        "availability": "Optional'",
        "serviceProviderList": {
                "Dhcp": "VirtualRouter",
            "Dns": "VirtualRouter",
            "SourceNat": "VirtualRouter",
            "PortForwarding": "VirtualRouter",
            "Vpn": "VirtualRouter",
            "Firewall": "VirtualRouter",
            "Lb": "VirtualRouter",
            "UserData": "VirtualRouter",
            "StaticNat": "VirtualRouter"
        }
    },
	"network_offering_vlan": {
		    "name": 'Test Network offering',
		    "displaytext": 'Test Network offering',
		    "guestiptype": 'Isolated',
		    "supportedservices": 'Dhcp,Dns,SourceNat,PortForwarding',
		    "traffictype": 'GUEST',
		    "specifyvlan": 'False',
		    "availability": 'Optional',
		    "serviceProviderList" : {
								   "Dhcp": 'VirtualRouter',
								   "Dns": 'VirtualRouter',
								   "SourceNat": 'VirtualRouter',
								   "PortForwarding": 'VirtualRouter',
			                     },
	},
	"network_offering_without_sourcenat": {
	   "name": 'Test Network offering',
	   "displaytext": 'Test Network offering',
	   "guestiptype": 'Isolated',
	   "supportedservices": 'Dhcp,Dns,UserData',
	   "traffictype": 'GUEST',
	   "availability": 'Optional',
	   "serviceProviderList" : {
							   "Dhcp": 'VirtualRouter',
							   "Dns": 'VirtualRouter',
							   "UserData": 'VirtualRouter',
		},
	},
    "isolated_network": {
        "name": "Isolated Network",
        "displaytext": "Isolated Network"
    },
    "netscaler_VPX": {
        "ipaddress": "10.223.240.174",
        "username": "nsroot",
        "password": "nsroot",
        "networkdevicetype": "NetscalerVPXLoadBalancer",
        "publicinterface": "1/1",
        "privateinterface": "1/2",
        "numretries": 2,
        "lbdevicededicated": "True",
        "lbdevicecapacity": 2,
        "port": 22
    },
    "netscaler_network": {
        "name": "Netscaler",
        "displaytext": "Netscaler",
    },
    "network_without_acl": {
        "name": "TestNetwork",
        "displaytext": "TestNetwork",
	},
    "virtual_machine": {
        "displayname": "Test VM",
        "username": "root",
        "password": "password",
        "ssh_port": 22,
        "privateport": 22,
        "publicport": 22,
        "protocol": "TCP",
        "affinity": {
            "name": "webvms",
            "type": "host anti-affinity",
        },
    },
    "virtual_machine2": {
        "name": "testvm2",
        "displayname": "Test VM2",
    },
    "virtual_machine3": {
        "name": "testvm3",
        "displayname": "Test VM3",
    },
    "server_without_disk": {
        "displayname": "Test VM-No Disk",
        "username": "root",
        "password": "password",
        "ssh_port": 22,
        "hypervisor": 'XenServer',
        "privateport": 22,
        "publicport": 22,
        "protocol": 'TCP',
    },
    "shared_network": {
        "name": "MySharedNetwork - Test",
        "displaytext": "MySharedNetwork",
        "vlan": "",
        "gateway": "",
        "netmask": "",
        "startip": "",
        "endip": "",
        "acltype": "Domain",
        "scope": "all"
    },
    "shared_network_offering": {
        "name": "MySharedOffering-shared",
        "displaytext": "MySharedOffering",
        "guestiptype": "Shared",
        "supportedservices": "Dhcp,Dns,UserData",
        "specifyVlan": "False",
        "specifyIpRanges": "False",
        "traffictype": "GUEST",
        "serviceProviderList": {
                "Dhcp": "VirtualRouter",
            "Dns": "VirtualRouter",
            "UserData": "VirtualRouter"
        }
    },
    "shared_network_offering_all_services": {
            "name": "shared network offering with services enabled",
            "displaytext": "Shared network offering",
            "guestiptype": "Shared",
            "supportedservices": "Dhcp,Dns,SourceNat,PortForwarding,Vpn,Firewall,Lb,UserData,StaticNat",
            "specifyVlan": "False",
            "specifyIpRanges": "False",
            "traffictype": "GUEST",
            "serviceProviderList": {
                "Dhcp": "VirtualRouter",
                "Dns": "VirtualRouter",
                "UserData": "VirtualRouter",
                "SourceNat": "VirtualRouter",
                "PortForwarding": "VirtualRouter",
                "Vpn": "VirtualRouter",
                "Firewall": "VirtualRouter",
                "Lb": "VirtualRouter",
                "UserData": "VirtualRouter",
                "StaticNat": "VirtualRouter"
            }
    },
    "shared_network_offering_sg": {
        "name": "MySharedOffering-sg",
        "displaytext": "MySharedOffering-sg",
        "guestiptype": "Shared",
        "supportedservices": "Dhcp,Dns,UserData,SecurityGroup",
        "specifyVlan": "False",
        "specifyIpRanges": "False",
        "traffictype": "GUEST",
        "serviceProviderList": {
                "Dhcp": "VirtualRouter",
            "Dns": "VirtualRouter",
            "UserData": "VirtualRouter",
            "SecurityGroup": "SecurityGroupProvider"
        }
    },
    "shared_network_sg": {
        "name": "Shared-Network-SG-Test",
        "displaytext": "Shared-Network_SG-Test",
        "networkofferingid": "1",
        "vlan": "",
        "gateway": "",
        "netmask": "255.255.255.0",
        "startip": "",
        "endip": "",
        "acltype": "Domain",
        "scope": "all"
    },
    "vpc_offering": {
        "name": "VPC off",
        "displaytext": "VPC off",
        "supportedservices":
        "Dhcp,Dns,SourceNat,PortForwarding,Vpn,Lb,UserData,StaticNat,NetworkACL"
    },
    "vpc": {
        "name": "TestVPC",
        "displaytext": "TestVPC",
        "cidr": "10.0.0.1/24"
    },
	"vpc_network_domain": {
		"name": "TestVPC",
		"displaytext": "TestVPC",
		"cidr": '10.0.0.1/24',
		"network_domain": "TestVPC"
	},
    "clusters": {
        0: {
            "clustername": "Xen Cluster",
            "clustertype": "CloudManaged",
            "hypervisor": "XenServer",
        },
        1: {
            "clustername": "KVM Cluster",
            "clustertype": "CloudManaged",
            "hypervisor": "KVM",
        },
        2: {
            "hypervisor": 'VMware',
            "clustertype": 'ExternalManaged',
            "username": 'administrator',
            "password": 'fr3sca',
            "url": 'http://192.168.100.17/CloudStack-Clogeny-Pune/Pune-1',
            "clustername": 'VMWare Cluster',
        },
    },
    "hosts": {
        "xenserver": {
            "hypervisor": 'XenServer',
            "clustertype": 'CloudManaged',
            "url": 'http://192.168.100.211',
            "username": "root",
            "password": "fr3sca",
        },
        "kvm": {
            "hypervisor": 'KVM',
            "clustertype": 'CloudManaged',
            "url": 'http://192.168.100.212',
            "username": "root",
            "password": "fr3sca",
        },
        "vmware": {
            "hypervisor": 'VMware',
            "clustertype": 'ExternalManaged',
            "url": 'http://192.168.100.203',
            "username": "administrator",
            "password": "fr3sca",
        },
    },
    "network_offering_shared": {
        "name": 'Test Network offering shared',
        "displaytext": 'Test Network offering Shared',
        "guestiptype": 'Shared',
        "supportedservices": 'Dhcp,Dns,UserData',
        "traffictype": 'GUEST',
        "specifyVlan": "True",
        "specifyIpRanges": "True",
        "serviceProviderList": {
                "Dhcp": 'VirtualRouter',
            "Dns": 'VirtualRouter',
            "UserData": 'VirtualRouter',
        },
    },
    "nw_off_isolated_RVR": {
        "name": "Network offering-RVR services",
        "displaytext": "Network off-RVR services",
        "guestiptype": "Isolated",
        "supportedservices": "Vpn,Dhcp,Dns,SourceNat,PortForwarding,Firewall,Lb,UserData,StaticNat",
        "traffictype": "GUEST",
        "availability": "Optional",
        "ispersistent": "False",
        "serviceProviderList": {
            "Vpn": "VirtualRouter",
            "Dhcp": "VirtualRouter",
            "Dns": "VirtualRouter",
            "SourceNat": "VirtualRouter",
            "PortForwarding": "VirtualRouter",
            "Firewall": "VirtualRouter",
            "Lb": "VirtualRouter",
            "UserData": "VirtualRouter",
            "StaticNat": "VirtualRouter"
        },
        "serviceCapabilityList": {
            "SourceNat": {
                "SupportedSourceNatTypes": "peraccount",
                "RedundantRouter": "true"
            },
            "lb": {
                "SupportedLbIsolation": "dedicated"
            }
        }
    },
    "nw_off_persistent_RVR": {
        "name": 'Network offering-RVR services',
        "displaytext": 'Network off-RVR services',
        "guestiptype": 'Isolated',
        "supportedservices":
        'Vpn,Dhcp,Dns,SourceNat,PortForwarding,Firewall,Lb,UserData,StaticNat',
        "traffictype": 'GUEST',
        "ispersistent": 'True',
        "availability": 'Optional',
        "serviceProviderList": {
                "Vpn": 'VirtualRouter',
            "Dhcp": 'VirtualRouter',
            "Dns": 'VirtualRouter',
            "SourceNat": 'VirtualRouter',
            "PortForwarding": 'VirtualRouter',
            "Firewall": 'VirtualRouter',
            "Lb": 'VirtualRouter',
            "UserData": 'VirtualRouter',
            "StaticNat": 'VirtualRouter',
        },
        "serviceCapabilityList": {
            "SourceNat": {
                "SupportedSourceNatTypes": "peraccount",
                "RedundantRouter": "true",
            },
            "lb": {
                "SupportedLbIsolation": "dedicated"
            },
        },
    },
    "nw_offering_isolated_vpc": {
        "name": "Isolated Network for VPC",
        "displaytext": "Isolated Network for VPC",
        "guestiptype": "Isolated",
        "supportedservices": "Dhcp,Dns,SourceNat,PortForwarding,Vpn,UserData,StaticNat,NetworkACL,Lb",
        "traffictype": "GUEST",
        "availability": "Optional",
        "ispersistent": "False",
        "useVpc": "on",
        "serviceProviderList": {
            "Dhcp": "VpcVirtualRouter",
            "Dns": "VpcVirtualRouter",
            "SourceNat": "VpcVirtualRouter",
            "PortForwarding": "VpcVirtualRouter",
            "Vpn": "VpcVirtualRouter",
            "UserData": "VpcVirtualRouter",
            "StaticNat": "VpcVirtualRouter",
            "NetworkACL": "VpcVirtualRouter",
            "Lb": "VpcVirtualRouter"
        }
    },
    "nw_off_persistent_VPCVR_LB": {
        "name": "Persistent Network VPC with LB",
        "displaytext": "Persistent Network VPC No LB",
        "guestiptype": "Isolated",
        "supportedservices": "Dhcp,Dns,SourceNat,PortForwarding,Vpn,Lb,UserData,StaticNat,NetworkACL",
        "traffictype": "GUEST",
        "availability": "Optional",
        "ispersistent": "True",
        "useVpc": "on",
        "serviceProviderList": {
            "Dhcp": "VpcVirtualRouter",
            "Dns": "VpcVirtualRouter",
            "SourceNat": "VpcVirtualRouter",
            "PortForwarding": "VpcVirtualRouter",
            "Vpn": "VpcVirtualRouter",
            "Lb": "VpcVirtualRouter",
            "UserData": "VpcVirtualRouter",
            "StaticNat": "VpcVirtualRouter",
            "NetworkACL": "VpcVirtualRouter"
        }
    },
    "nw_off_persistent_VPCVR_NoLB": {
        "name": "Persistent Network VPC No LB",
        "displaytext": "Persistent Network VPC No LB",
        "guestiptype": "Isolated",
        "supportedservices": "Dhcp,Dns,SourceNat,PortForwarding,Vpn,UserData,StaticNat,NetworkACL",
        "traffictype": "GUEST",
        "availability": "Optional",
        "ispersistent": "True",
        "useVpc": "on",
        "serviceProviderList": {
            "Dhcp": "VpcVirtualRouter",
            "Dns": "VpcVirtualRouter",
            "SourceNat": "VpcVirtualRouter",
            "PortForwarding": "VpcVirtualRouter",
            "Vpn": "VpcVirtualRouter",
            "UserData": "VpcVirtualRouter",
            "StaticNat": "VpcVirtualRouter",
            "NetworkACL": "VpcVirtualRouter"
        }
    },
    "nw_offering_shared_persistent": {
        "name": "Network offering for Shared Persistent Network",
        "displaytext": "Network offering-DA services",
        "guestiptype": "Shared",
        "supportedservices": "Dhcp,Dns,SourceNat,PortForwarding,Vpn,Firewall,Lb,UserData,StaticNat",
        "traffictype": "GUEST",
        "availability": "Optional",
        "ispersistent": "True",
        "serviceProviderList": {
            "Dhcp": "VirtualRouter",
            "Dns": "VirtualRouter",
            "SourceNat": "VirtualRouter",
            "PortForwarding": "VirtualRouter",
            "Vpn": "VirtualRouter",
            "Firewall": "VirtualRouter",
            "Lb": "VirtualRouter",
            "UserData": "VirtualRouter",
            "StaticNat": "VirtualRouter"
        }
    },
    "fwrule": {
        "startport": 22,
        "endport": 22,
        "cidr": "0.0.0.0/0",
        "protocol": "TCP"
    },
    "nw_off_isolated_persistent_netscaler": {
        "name": 'Netscaler',
        "displaytext": 'Netscaler',
        "guestiptype": 'Isolated',
        "supportedservices":
        'Dhcp,Dns,SourceNat,PortForwarding,Vpn,Firewall,Lb,UserData,StaticNat',
        "traffictype": 'GUEST',
        "ispersistent": 'True',
        "availability": 'Optional',
        "serviceProviderList": {
            "Dhcp": 'VirtualRouter',
            "Dns": 'VirtualRouter',
            "SourceNat": 'VirtualRouter',
            "PortForwarding": 'VirtualRouter',
            "Vpn": 'VirtualRouter',
            "Firewall": 'VirtualRouter',
            "Lb": 'Netscaler',
            "UserData": 'VirtualRouter',
            "StaticNat": 'VirtualRouter',
        },

    },
	"network_acl_rule": {
		   "protocol":"TCP",
		   "traffictype":"ingress",
		   "cidrlist":"0.0.0.0/0",
		   "startport":"1",
		   "endport":"1"
	},
    "network_offering_internal_lb": {
        "name": "Network offering for internal lb service",
        "displaytext": "Network offering for internal lb service",
        "guestiptype": "Isolated",
        "traffictype": "Guest",
        "supportedservices":
        "Vpn,Dhcp,Dns,Lb,UserData,SourceNat,StaticNat,PortForwarding,NetworkACL",
        "serviceProviderList": {
                "Dhcp": "VpcVirtualRouter",
            "Dns": "VpcVirtualRouter",
            "Vpn": "VpcVirtualRouter",
            "UserData": "VpcVirtualRouter",
            "Lb": "InternalLbVM",
            "SourceNat": "VpcVirtualRouter",
            "StaticNat": "VpcVirtualRouter",
            "PortForwarding": "VpcVirtualRouter",
            "NetworkACL": "VpcVirtualRouter",
        },
        "serviceCapabilityList": {
            "SourceNat": {"SupportedSourceNatTypes": "peraccount"},
            "Lb": {"lbSchemes": "internal", "SupportedLbIsolation": "dedicated"}
        }
    },
    "natrule": {
        "privateport": 22,
        "publicport": 22,
        "protocol": "TCP"
    },
    "lbrule": {
        "name": "SSH",
        "alg": "roundrobin",
        "privateport": 22,
        "publicport": 2222,
        "protocol": 'TCP'
    },
    "vpclbrule": {
        "name": "SSH",
        "alg": "roundrobin",
        "privateport": 22,
        "publicport": 22,
        "protocol": 'TCP'
    },
    "icmprule": {
        "icmptype":-1,
        "icmpcode":-1,
        "cidrlist": "0.0.0.0/0",
        "protocol": "ICMP"
    },
    "iso": {
            "displaytext": "Test ISO",
            "name": "ISO",
            "url": "http://people.apache.org/~tsp/dummy.iso",
            "bootable": False,
            "ispublic": False,
            "ostype": "Other (64-bit)",
    },
    "iso1": {
        "displaytext": "Test ISO 1",
        "name": "ISO 1",
        "url": "http://people.apache.org/~tsp/dummy.iso",
        "isextractable": True,
        "isfeatured": True,
        "ispublic": True,
        "ostype": "CentOS 5.6 (64-bit)",
    },
    "iso2": {
        "displaytext": "Test ISO 2",
        "name": "ISO 2",
        "url": "http://people.apache.org/~tsp/dummy.iso",
        "isextractable": True,
        "isfeatured": True,
        "ispublic": True,
        "ostype": "CentOS 5.6 (64-bit)",
        "mode": 'HTTP_DOWNLOAD',
    },
    "isfeatured": True,
    "ispublic": True,
    "isextractable": True,
    "bootable": True,
    "passwordenabled": True,

    "template": {
        "displaytext": "xs",
        "name": "xs",
        "passwordenabled": False,
    },
    "template_2": {
        "displaytext": "Public Template",
        "name": "Public template",
        "ostype": "CentOS 5.6 (64-bit)",
        "isfeatured": True,
        "ispublic": True,
        "isextractable": True,
        "mode": "HTTP_DOWNLOAD",
        "templatefilter": "self"
    },
    "privatetemplate": {
        "displaytext": "Public Template",
        "name": "Public template",
        "ostype": "CentOS 5.6 (64-bit)",
        "isfeatured": True,
        "ispublic": False,
        "isextractable": True,
        "mode": "HTTP_DOWNLOAD",
        "templatefilter": "self"
    },
    "templatefilter": 'self',
    "templates": {
        "displaytext": 'Template',
        "name": 'Template',
        "ostype": "CentOS 5.3 (64-bit)",
        "templatefilter": 'self',
    },
    "win2012template": {
        "displaytext": "win2012",
        "name": "win2012",
        "passwordenabled": False,
        "url": "http://nfs1.lab.vmops.com/templates/vmware/new-test-win.ova",
        "format": "OVA",
        "ostype": "Windows 8 (64-bit)",
    },
    "rhel60template": {
        "displaytext": "Rhel60",
        "name": "Rhel60",
        "passwordenabled": False,
        "url": "http://10.147.28.7/templates/Rhel/Rhel6-64bit.ova",
        "format": "OVA",
        "ostype": "Red Hat Enterprise Linux 6.0 (64-bit)"
    },
    "templateregister": {
        "displaytext": "xs",
        "name": "xs",
        "passwordenabled": False,
        "url": "http://10.147.28.7/templates/ttylinux_pv.vhd",
        "format": "VHD"
    },
    "security_group": {"name": "custom_Sec_Grp"},
    "ingress_rule": {
        "protocol": "TCP",
        "startport": "22",
        "endport": "22",
        "cidrlist": "0.0.0.0/0"
    },
    "vpncustomergateway": {
            "ipsecpsk": "secreatKey",
            "ikepolicy": "aes128-sha1",
            "ikelifetime": "86400",
            "esppolicy": "aes128-sha1",
            "epslifetime": "3600",
            "dpd": "false"
    },
    "ostype": "CentOS 5.6 (64-bit)",
    "sleep": 90,
    "timeout": 10,
    "page": 1,
    "pagesize": 2,
    "listall": 'true',
    "host_password": "password",
    "advanced_sg": {
        "zone": {
            "name": "",
            "dns1": "8.8.8.8",
            "internaldns1": "192.168.100.1",
            "networktype": "Advanced",
            "securitygroupenabled": "true"
        },
        "securitygroupenabled": "true"
    },
    "vlan": "10",
    "portableiprange_vlan": {
        "part": ["4090-4091", "4092-4095"],
        "full": "4090-4095"
    },
    "nfs": {
        "url": "nfs://nfs/export/automation/1/testprimary",
        "name": "Primary XEN"
    },
    "iscsi": {
        "url":
        "iscsi://192.168.100.21/iqn.2012-01.localdomain.clo-cstack-cos6:iser/1",
        "name": "Primary iSCSI"
    },
    "volume": {"diskname": "Test Volume"},
    "custom_volume": {
        "customdisksize": 1,
        "diskname": "Custom disk",
    },
    "upload_volume": {
        "diskname": "UploadVol",
        "format": "VHD",
        "url":
        "http://10.147.28.7/templates/393d3550-05ef-330f-9b8c-745b0e699759.vhd",
        "checksum": "",
    },
    "recurring_snapshot": {
        "maxsnaps": 2,
        "timezone": "US/Arizona",
    },
    "volume_offerings": {
        0: {"diskname": "TestDiskServ"},
    },
    "diskdevice": ['/dev/vdc', '/dev/vdb', '/dev/hdb', '/dev/hdc',
                   '/dev/xvdd', '/dev/cdrom', '/dev/sr0', '/dev/cdrom1'],

    # test_vpc_vpn.py
    "vpn_user": {
        "username": "test",
        "password": "password",
    },
    "vpc": {
        "name": "vpc_vpn",
        "displaytext": "vpc-vpn",
        "cidr": "10.1.1.0/24"
    },
    "ntwk": {
        "name": "tier1",
        "displaytext": "vpc-tier1",
        "gateway": "10.1.1.1",
        "netmask": "255.255.255.192"
    },
    "vpc2": {
        "name": "vpc2_vpn",
        "displaytext": "vpc2-vpn",
        "cidr": "10.2.1.0/24"
    },
    "ntwk2": {
        "name": "tier2",
        "displaytext": "vpc-tier2",
        "gateway": "10.2.1.1",
        "netmask": "255.255.255.192"
    },
    "server": {
        "displayname": "TestVM",
        "username": "root",
        "password": "password",
        "ssh_port": 22,
        "hypervisor": 'XenServer',
        "privateport": 22,
        "publicport": 22,
        "protocol": 'TCP'
    },
    "privateport": 22,
    "publicport": 22,
    "protocol": 'TCP',
    "forvirtualnetwork": "true",
    "customdisksize": 1,
    "diskname": "Test Volume",
    "portableIpRange": {
        "gateway": "10.223.252.195",
        "netmask": "255.255.255.192",
        "startip": "10.223.252.196",
        "endip": "10.223.252.197",
        "vlan": "1001"
    },
    "sparse": {
        "name": "Sparse Type Disk offering",
        "displaytext":
        "Sparse Type Disk offering",
        "disksize": 1,  # in GB
        "provisioningtype": "sparse"
    },
    "fat": {
        "name": "Fat Type Disk offering",
        "displaytext":
        "Fat Type Disk offering",
        "disksize": 1,  # in GB
        "provisioningtype": "fat"
    },
    "sparse_disk_offering": {
        "displaytext": "Sparse",
        "name": "Sparse",
        "provisioningtype": "sparse",
        "disksize": 1
    },
    "host_anti_affinity": {
        "name": "hostantiaffinity",
        "type": "host anti-affinity",
    },
    "vgpu":{
        "disk_offering":{
                    "displaytext": "Small",
                    "name": "Small",
                    "disksize": 1
                        },
    "templateregister1": {
                              "displaytext": "win8withpv",
                              "name": "win8withpv",
                              "passwordenabled": False,
                              "url": "http://pleaseupdateURL/dummy.vhd",
                              "format": "VHD" ,
                              "ostype": "Windows 8 (64-bit)",
                              "ispublic": "true",
                              "hypervisor": "XenServer"
                              },
    "Windows 8 (64-bit)": {
                              "displaytext": "Windows 8 (64-bit)",
                              "name": "win8withpv",
                              "passwordenabled": False,
                              "url": "http://pleaseupdateURL/dummy.vhd",
                              "format": "VHD" ,
                              "ostype": "Windows 8 (64-bit)",
                              "ispublic": "true",
                              "hypervisor": "XenServer"
                              },
    "Windows Server 2012 (64-bit)": {
                              "displaytext": "Windows Server 2012 (64-bit)",
                              "name": "Windows Server 2012 (64-bit)",
                              "passwordenabled": False,
                              "url": "http://pleaseupdateURL/dummy.vhd",
                              "format": "VHD" ,
                              "ostype": "Windows Server 2012 (64-bit)",
                              "ispublic": "true",
                              "hypervisor": "XenServer"
                              },

    "Windows 7 (64-bit)": {
                              "displaytext": "Windows 7 (64-bit)",
                              "name": "Windows 7 (64-bit)",
                              "passwordenabled": False,
                              "url": "http://pleaseupdateURL/dummy.vhd",
                              "format": "VHD" ,
                              "ostype": "Windows 7 (64-bit)",
                              "ispublic": "true",
                              "hypervisor": "XenServer"
                              },
    "clusters": {
            "clustername": "Xen Cluster Vgpu",
            "clustertype": "CloudManaged",
            "hypervisor": "XenServer"
      },
    "hosts": {
        "nonvgpuxenserver": {
            "hypervisor": 'XenServer',
            "clustertype": 'CloudManaged',
            "url": 'http://10.102.192.57',
            "username": "root",
            "password": "freebsd",
             },
       },
        "account": {
                    "email": "test@test.com",
                    "firstname": "Test",
                    "lastname": "User",
                    "username": "test",
                    # Random characters are appended in create account to
                    # ensure unique username generated each time
                    "password": "password",
                    },
            "vgpu260q":   # Create a virtual machine instance with vgpu type as 260q
                    {   
                    "displayname": "testserver",
                    "username": "root", # VM creds for SSH
                    "password": "password",
                    "ssh_port": 22,
                    "hypervisor": 'XenServer',
                    "privateport": 22,
                    "publicport": 22,
                    "protocol": 'TCP',
                },
                "vgpu140q":   # Create a virtual machine instance with vgpu type as 140q
                {
                    "displayname": "testserver",
                    "username": "root",
                    "password": "password",
                    "ssh_port": 22,
                    "hypervisor": 'XenServer',
                    "privateport": 22,
                    "publicport": 22,
                    "protocol": 'TCP',
                },
                "service_offerings":
                {
                 "GRID K260Q":
                   {
                        "name": "vGPU260Q",
                        "displaytext": "vGPU260Q",
                        "cpunumber": 2,
                        "cpuspeed": 1600, # in MHz
                        "memory": 3072, # In MBs
                    },
                 "GRID K240Q":
                   {
                        "name": "vGPU240Q",
                        "displaytext": "vGPU240Q",
                        "cpunumber": 2,
                        "cpuspeed": 1600, # in MHz
                        "memory": 3072, # In MBs
                    },
                 "GRID K220Q":
                   {
                        "name": "vGPU220Q",
                        "displaytext": "vGPU220Q",
                        "cpunumber": 2,
                        "cpuspeed": 1600, # in MHz
                        "memory": 3072, # In MBs
                    },
                 "GRID K200":
                   {
                        "name": "vGPU200",
                        "displaytext": "vGPU200",
                        "cpunumber": 2,
                        "cpuspeed": 1600, # in MHz
                        "memory": 3072, # In MBs
                    },
                 "passthrough":
                   {
                        "name": "vGPU passthrough",
                        "displaytext": "vGPU passthrough",
                        "cpunumber": 2,
                        "cpuspeed": 1600, # in MHz
                        "memory": 3072, # In MBs
                    },
                 "GRID K140Q":
                    {
                     # Small service offering ID to for change VM
                     # service offering from medium to small
                        "name": "vGPU140Q",
                        "displaytext": "vGPU140Q",
                        "cpunumber": 2,
                        "cpuspeed": 1600,
                        "memory": 3072,
                    },
                   "GRID K120Q":
                    {
                        "name": "vGPU120Q",
                        "displaytext": "vGPU120Q",
                        "cpunumber": 2,
                        "cpuspeed": 1600,
                        "memory": 3072,
                    },
                   "GRID K100":
                     {
                        "name": "vGPU100",
                        "displaytext": "vGPU100",
                        "cpunumber": 2,
                        "cpuspeed": 1600,
                        "memory": 3072,
                     },
                   "nonvgpuoffering":
                     {
                        "name": "nonvgpuoffering",
                        "displaytext": "nonvgpuoffering",
                        "cpunumber": 2,
                        "cpuspeed": 1600,
                        "memory": 3072,
                     }

            },
            "diskdevice": ['/dev/vdc',  '/dev/vdb', '/dev/hdb', '/dev/hdc', '/dev/xvdd', '/dev/cdrom', '/dev/sr0', '/dev/cdrom1' ],
            # Disk device where ISO is attached to instance
            "mount_dir": "/mnt/tmp",
            "sleep": 180,
            "timeout": 60,
            "ostype": 'Windows 8 (64-bit)',
            "nongpu_host_ip":"10.102.192.57"
    },
      "acl":{
                #data for domains and accounts
                "domain1": {
                    "name": "D1",
                 },
                "accountD1": {
                    "email": "testD1@test.com",
                    "firstname": "testD1",
                    "lastname": "Admin",
                    "username": "testD1",
                    "password": "password",
                    "accounttype": "1",
                },
                "accountD1A": {
                    "email": "testD1A@test.com",
                    "firstname": "testD1A",
                    "lastname": "User",
                    "username": "testD1A",
                    "password": "password",
                },
                "accountD1B": {
                    "email": "testD1B@test.com",
                    "firstname": "testD1B",
                    "lastname": "User",
                    "username": "testD1B",
                    "password": "password",
                },
                "domain11": {
                    "name": "D11",
                 },
                "accountD11": {
                    "email": "testD11@test.com",
                    "firstname": "testD11",
                    "lastname": "Admin",
                    "username": "testD11",
                    "password": "password",
                    "accounttype": "1",
                },
                "accountD11A": {
                    "email": "testD11A@test.com",
                    "firstname": "testD11A",
                    "lastname": "User",
                    "username": "testD11A",
                    "password": "password",
                },
                "accountD11B": {
                    "email": "test11B@test.com",
                    "firstname": "testD11B",
                    "lastname": "User",
                    "username": "testD11B",
                    "password": "password",
                },
                "domain111": {
                    "name": "D111",
                 },
                "accountD111": {
                    "email": "testD111@test.com",
                    "firstname": "testD111",
                    "lastname": "Admin",
                    "username": "testD111",
                    "password": "password",
                },
                "accountD111A": {
                    "email": "testD111A@test.com",
                    "firstname": "testD111A",
                    "lastname": "User",
                    "username": "testD111A",
                    "password": "password",
                },
                "accountD111B": {
                    "email": "testD111B@test.com",
                    "firstname": "testD111B",
                    "lastname": "User",
                    "username": "testD111B",
                    "password": "password",
                },
               "domain12": {
                    "name": "D12",
                 },
                "accountD12A": {
                    "email": "testD12A@test.com",
                    "firstname": "testD12A",
                    "lastname": "User",
                    "username": "testD12A",
                    "password": "password",
                },
                "accountD12B": {
                    "email": "testD12B@test.com",
                    "firstname": "testD12B",
                    "lastname": "User",
                    "username": "testD12B",
                    "password": "password",
                },
                "domain2": {
                   "name": "D2",
                 },
                "accountD2": {
                    "email": "testD2@test.com",
                    "firstname": "testD2",
                    "lastname": "User",
                    "username": "testD2",
                    "password": "password",
                    "accounttype": "1",
                },
                "accountD2A": {
                    "email": "testD2A@test.com",
                    "firstname": "testD2A",
                    "lastname": "User",
                    "username": "testD2A",
                    "password": "password",
                },
                "accountROOTA": {
                    "email": "testROOTA@test.com",
                    "firstname": "testROOTA",
                    "lastname": "User",
                    "username": "testROOTA",
                    "password": "password",
                },

                "accountROOT": {
                    "email": "testROOTA@test.com",
                    "firstname": "testROOT",
                    "lastname": "admin",
                    "username": "testROOT",
                    "password": "password",
                },
                #data reqd for virtual machine creation
                "vmD1" : {
                    "name" : "d1",
                    "displayname" : "d1",
                },
                "vmD1A" : {
                    "name" : "d1a",
                    "displayname" : "d1a",
                },
                "vmD1B" : {
                    "name" : "d1b",
                    "displayname" : "d1b",
                },
                "vmD11" : {
                   "name" : "d11",
                   "displayname" : "d11",
                },
                "vmD11A" : {
                   "name" : "d11a",
                   "displayname" : "d11a",
                },
                "vmD11B" : {
                    "name" : "d11b",
                    "displayname" : "d11b",
                },
                "vmD111" : {
                    "name" : "d111",
                    "displayname" : "d111",
                },
                "vmD111A" : {
                    "name" : "d111a",
                    "displayname" : "d111a",
                },
                "vmD111B" : {
                    "name" : "d111b",
                    "displayname" : "d111b",
                },
                "vmD12A" : {
                    "name" : "d12a",
                    "displayname" : "d12a",
                },
                "vmD12B" : {
                    "name" : "d12b",
                    "displayname" : "d12b",
                },
                "vmD2A" : {
                    "name" : "d2a",
                    "displayname" : "d2a",
                },

                "vmROOTA" : {
                    "name" : "roota",
                    "displayname" : "roota",
                },
                "vmROOT" : {
                    "name" : "root",
                    "displayname" : "root",
                },

                #data reqd for Network creation
                "network_all": {
                     "name": "SharedNetwork-All",
                     "displaytext": "SharedNetwork-All",
                     "vlan" : "4001",
                     "gateway" :"10.223.1.1",
                     "netmask" :"255.255.255.0",
                     "startip" :"10.223.1.2",
                     "endip" :"10.223.1.100",
                     "acltype" : "Domain"
                },
                "network_domain_with_no_subdomain_access": {
                     "name": "SharedNetwork-Domain-nosubdomain",
                     "displaytext": "SharedNetwork-Domain-nosubdomain",
                     "vlan" : "4002",
                     "gateway" :"10.223.1.1",
                     "netmask" :"255.255.255.0",
                     "startip" :"10.223.1.2",
                     "endip" :"10.223.1.100",
                     "acltype" : "Domain",
                     "subdomainaccess" : "false"
                },
                "network_domain_with_subdomain_access": {
                     "name": "SharedNetwork-Domain-withsubdomain",
                     "displaytext": "SharedNetwork-Domain-withsubdomain",
                     "vlan" : "4003",
                     "gateway" :"10.223.1.1",
                     "netmask" :"255.255.255.0",
                     "startip" :"10.223.1.2",
                     "endip" :"10.223.1.100",
                     "acltype" : "Domain",
                     "subdomainaccess" : "true"
                },
                "network_account": {
                     "name": "SharedNetwork-Account",
                     "displaytext": "SharedNetwork-Account",
                     "vlan" : "4004",
                     "gateway" :"10.223.1.1",
                     "netmask" :"255.255.255.0",
                     "startip" :"10.223.1.2",
                     "endip" :"10.223.1.100",
                     "acltype" : "Account"
               },

                "network": {
                     "name": "Network-",
                     "displaytext": "Network-",
                     "gateway" :"10.223.1.1",
                     "netmask" :"255.255.255.0",
                     "startip" :"10.223.1.2",
                     "endip" :"10.223.1.100",
                },
                #small service offering
                "service_offering": {
                    "small": {
                        "name": "Small Instance",
                        "displaytext": "Small Instance",
                        "cpunumber": 1,
                        "cpuspeed": 100,
                        "memory": 128,
                    },
                },
                "ostype": 'CentOS 5.6 (64-bit)',
        },
        "ldap_account": {
            "email": "rmurphy@cloudstack.org",
            "firstname": "Ryan",
            "lastname": "Murphy",
            "username": "rmurphy",
            "password": "internalcloudstackpassword",
            },
        "ldapConfiguration_1": {
            "basedn": "dc=cloudstack,dc=org",
            "emailAttribute": "mail",
            "userObject": "inetOrgPerson",
            "usernameAttribute": "uid",
            "hostname": "localhost",
            "port": "10389",
            "ldapUsername": "rmurphy",
            "ldapPassword": "password"
            },

      "test_34_DeployVM_in_SecondSGNetwork": {
          "zone": "advsg",
          "config": "D:\ACS-Repo\setup\dev\\advancedsg.cfg",#Absolute path to cfg file
          #For sample configuration please refer to <ACS repo>/setup/dev/advancedsg.cfg
          "template": "CentOS 5.3(64-bit) no GUI (Simulator)",
          "dbSvr": {
              "dbSvr": "10.146.0.133",
              "passwd": "cloud",
              "db": "cloud",
              "port": 3306,
              "user": "cloud"
          },
          "mgtSvr": [
              {
                  "mgtSvrIp": "10.146.0.133",
                  "passwd": "password",
                  "user": "root",
                  "port": 8096
              }
          ],
          "ipranges": [
              {
                  "startip": "10.147.32.150",
                  "endip": "10.147.32.153",
                  "netmask": "255.255.255.0",
                  "vlan": "32",
                  "gateway": "10.147.32.1"
              }
          ]
      },
    "configurableData":
    {
        "portableIpRange": {
            "gateway": "",
            "netmask": "",
            "startip": "",
            "endip": "",
            "vlan": ""
        },
        "netscaler": {
            "ipaddress": "",
            "username": "",
            "password": "",
            "networkdevicetype": "",
            "publicinterface": "",
            "privateinterface": "",
            "numretries": "",
            "lbdevicededicated": "False",
            "lbdevicecapacity": 2,
            "port": 22
        },
        "iscsi": {
            "url": "",
            "name": "Primary iSCSI"
        },
    }
}
