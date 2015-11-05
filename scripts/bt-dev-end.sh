#!/bin/sh

#
# Script for stopping Broadcom UART Bluetooth stack
#

PGREP="/usr/bin/pgrep"

# Device down
/usr/bin/hciconfig hci0 down

# Turn off Bluetooth Chip
/usr/sbin/rfkill block bluetooth

#/usr/bin/killall hciattach
# Do NOT use killall due to smack
hciattach_pid=`${PGREP} hciattach`
kill $hciattach_pid
