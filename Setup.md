# Setup 5G Testbed

This document will provide steps to setup a 5G testbed based on open-source software. It is assumed that you already gained basic knowledge of Linux OS (Ubuntu), networking, docker, and Kubernetes before starting to setup the testbed.

![Overview](./images/overview.png)

## Hardware Specifications

In our testbed, we used a single physical server with two Intel Xeon Gold 5218 CPUs (20 core per CPU) and 128GB RAM. The server was installed Ubuntu 20.04 LTS and VMware Workstation Pro v16.2.4 to create virtual machines.

## VM Preparation

We created 6 VMs for the testbed. Below are the settings of each VM

| VM   | CPU | RAM  | NIC                                                                        | Note                                                     |
| ---- | --- | ---- | -------------------------------------------------------------------------- | -------------------------------------------------------- |
| VM 1 | 4   | 8GB  | NIC1: NAT (Internet)<br /> NIC2: RAN Network                               | For installing UE simulation                             |
| VM 2 | 4   | 8GB  | NIC1: NAT (Internet)<br /> NIC2: RAN Network                               | For installing gNB (base station)                        |
| VM 3 | 4   | 8GB  | NIC1: NAT (Internet)<br /> NIC2: RAN Network<br /> NIC3: Access Network    | Router to connect between RAN and Access networks        |
| VM 4 | 20  | 32GB | NIC1: NAT (Internet)<br /> NIC2: Access Network<br /> NIC3: Data Network   | For installing 5G Core                                   |
| VM 5 | 4   | 4GB  | NIC1: NAT (Internet)<br /> NIC2: Data Network<br /> NIC3: External Network | Router to connect between 5G Core and external networks  |
| VM 6 | 8   | 16GB | NIC1: NAT (Internet)<br /> NIC2: External Network                          | For installing applications (act as MEC or cloud server) |

## Network Settings

We need to prepare virtual networks to connect VMs together. Open **Virtual Network Editor** in VMware and create 3 virtual network (vmnet) as below.

![Overview](./images/vmnet.png)

Basically, we have 3 seperated networks (subnets) to simulate the real scenario.

RAN Subnet (192.168.252.x): to connect all base stations (gNB) to the Access gateway. Note that VM1 (UE) onlly need to communicate with VM2 (gNB), so we can put VM1 in the RAN subnet also.

Access Subnet (192.168.252.x): to connect all UPFs with the RAN subnet.

Core Subnet (192.168.250x): to connect all core network (UPFs) to external networks (i.e., MEC or internet)

![Overview](./images/network.png)

### IP Settings

| VM   | IP Address                                                                                                                                                                             |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VM 1 | NIC1: NAT (dynamic allocation)<br />NIC2: RAN (static IP)<br />IP: 192.168.251.6 <br />GW: 192.168.251.1                                                                               |
| VM 2 | NIC1: NAT (dynamic allocation)<br />NIC2: RAN (static IP)<br />IP: 192.168.251.6 <br />GW: 192.168.251.1                                                                               |
| VM 3 | NIC1: NAT (dynamic allocation)<br />NIC2: RAN GW (static IP)<br />IP: 192.168.251.1 <br />NIC3: Access GW (static IP)<br />IP: 192.168.252.1                                           |
| VM 4 | NIC1: NAT (dynamic allocation)<br />NIC2: Access (static IP)<br />IP: 192.168.252.3 <br />GW: 192.168.252.1<br />NIC3: Core (static IP)<br />IP: 192.168.250.3 <br />GW: 192.168.250.1 |
| VM 5 | NIC1: NAT (dynamic allocation)<br />NIC2: Core GW (static IP)<br />IP: 192.168.250.1 <br />NIC3: External network (can be NAT or other subnet                                          |
| VM 6 | NIC1: NAT (dynamic allocation)<br />NIC2: MEC IP (static IP)<br />IP: 192.168.250.12 <br />GW: 192.168.250.1                                                                           |

### Notes

- To simlify settings, we allow VM6 to use the same subnnet with VM4, however the communication between UE to MEC server will go through VM1 --> VM2 --> VM3 --> VM4 --> VM5 --> VM6.

- You need to enable IP forwarding in VM3, then it will forward the packets between two subnets (.251.x and .252.x), check ping between VM2 and VM4 to ensure that gNB can communicate with UPF

```
# Edit /etc/sysctl.conf and search for the following lines:
# Uncomment the next line to enable packet forwarding for IPv4
net.ipv4.ip_forward=1

```

## 5G Core Installation

## UE & RAN Installation
