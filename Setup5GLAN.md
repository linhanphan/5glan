# Setup 5G LAN feature on a working 5G testbed

## Introduction

This setup tutorial assumes you already have a working 5G Testbed. If you don't, please follow the [Setup 5G Testbed](Setup5GTestbed.md) tutorial first.

This tutorial will guide you through the process of setting up the 5G LAN feature on your testbed. This feature will allow your 5G network to work as a LAN network, meaning that all the devices connected to the 5G network will be able to communicate with each other.

## Prerequisites

- A working UPF & 5G Core Network running with the aether-in-a-box image
- A working RAN & UE with the UERANSIM simulator

## Setup

To setup the 5G LAN feature, you will first need to gather the IP of the UE that are running on your test bed.
To do so, just go on the machine that your UE are running on and to the following command :

```bash
ip a | grep uesim
```

Now go on the machine that your UPF is running on, clone this repository if it isn't already done and go to the *5glan-setup* folder.

```bash
git clone https://github.com/linhanphan/5glan
cd 5glan/5glan-setup
```

Then, you will need to install some python packages and a program to be able to run the setup script.

```bash
sudo apt install python3-pip
pip3 install grpcio
pip3 install ptf
sudo apt install scapy
```

You can now run the setup script. The setup script takes one argument and it is the IP adress of the UE that you want to add to the 5GLAN network. You can add as many UE as you want by running the script multiple times with different IP adress.

```bash
python3 setupLAN.py <UE IP>
```

Well done, you now have a working 5GLAN feature between the UEs of your testbed. You can now test it by pinging the UE from each other.