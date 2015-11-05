#!/bin/sh

#
# Script for registering Broadcom UART BT device
#
BT_UART_DEVICE=/dev/sttybt0
BT_CHIP_TYPE=sprd

BT_ADDR=/csa/bluetooth/.bd_addr

UART_SPEED=115200

/usr/sbin/rfkill unblock bluetooth

echo "Bluetooth device is DOWN"
echo "Registering Bluetooth device"

echo " Attaching device"
if (/usr/bin/hciattach -s $UART_SPEED $BT_UART_DEVICE $BT_CHIP_TYPE); then
	/bin/sleep 0.1
	echo "HCIATTACH success"
else
	echo "HCIATTACH failed"
	/usr/sbin/rfkill block bluetooth
	/bin/cp /var/log/messages /var/lib/bluetooth/
fi

#/usr/sbin/hciconfig hci0 down

