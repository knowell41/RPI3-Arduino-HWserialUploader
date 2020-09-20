Installation

sudo apt-get install python3-pip
pip3 install RPi.GPIO
sudo apt-get install avrdude


Edit /boot/config.txt
dtoverlay=disable-bt

sudo raspi-config
-interfacing options
-serial
--would you like a login shell to be accessible over serial?
-No
--would you like the serial port hardware to be enabled?
-Yes

Exit raspi-config and reboot

Hardware Connection
ArduinoProMini			RPi

Rx				Tx (GPIO14)
Tx				Rx (GPIO15)
DTR				GPIO23
RAW				3v3
GND				GND

edit python script to match your directory.

chmod 755 upload.py

execute 

./upload.py YourHexFile.hex
  
  
  





