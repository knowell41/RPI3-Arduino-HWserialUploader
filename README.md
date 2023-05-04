# Hardware setup
`Raspberry pi` with `Arduino` attached to hardware serial pins `GPIO14` and `GPIO15`.
Its purpose is to seamlessly update the `arduino` firmware with `*.bin` file by running a `upload.py` script. This setup is useful for updating firmware of an `arduino` attached in rasberry pi without having to disassembel it and manually reprogram it using `official arduino software`.

#Installation
## Install dependencies
```
> sudo apt-get install python3-pip
> pip3 install RPi.GPIO
> sudo apt-get install avrdude
```
## Edit `/boot/config.txt`
```
dtoverlay=disable-bt
```
## Enable Hardware Serial in Raspi Config and do a reboot
```
> sudo raspi-config
-interfacing options
-serial
--would you like a login shell to be accessible over serial?
-No
--would you like the serial port hardware to be enabled?
-Yes
```

Hardware Connection

| Arduino Pro Mini | Rpi |
| ---------------- | --- |
| RX | TX `GPIO14` |
| TX | RX `GPIO15` |
| DTR | `GPIO23` |
| RAW | `3v3` |
| GND | `GND` |

## Update `upload.py` to match the your directory
```
######################################
yourDirectory = "/path/to/your/bin/file"

######################################

```

## Update permissions
```
> chmod 755 upload.py
```

# How to use

1. Upload your arduino hexfile to the RPI specified path. Make sure that `upload.py` and your hex file is in the same directory.
2. Run the script
```
./upload.py YourHexFile.hex
```
  
  





