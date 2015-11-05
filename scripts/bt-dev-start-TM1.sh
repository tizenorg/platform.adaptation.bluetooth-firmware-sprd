#!/bin/sh

BT_UART_DEVICE=/dev/ttyS0
BT_CHIP_TYPE=sprd

HCI_CONFIG=/usr/bin/hciconfig
HCI_ATTACH=/usr/bin/hciattach

UART_SPEED=3000000

echo "Check for Bluetooth device status"
if (${HCI_CONFIG} | grep hci); then
	echo "Bluetooth device is UP"
	${HCI_CONFIG} hci0 up
	exit 1
fi

/usr/sbin/rfkill unblock bluetooth

echo "Bluetooth device is DOWN"
echo "Registering Bluetooth device"

echo " Attaching device"
if (${HCI_ATTACH} -s $UART_SPEED $BT_UART_DEVICE $BT_CHIP_TYPE $UART_SPEED flow); then
	/bin/sleep 0.1
	echo "HCIATTACH success"
else
	echo "HCIATTACH failed"
	/usr/sbin/rfkill block bluetooth
	/bin/cp /var/log/messages /var/lib/bluetooth/
fi

#/usr/sbin/hciconfig hci0 down

