# weatherpi
Repository for scripts used for my basic weather station Raspberry Pi project

Project build can be found here https://core-electronics.com.au/projects/basic-weather-station

Pi requires I2C bus to be enabled

    sudo apt-get install -y python-smbus
    
    sudo apt-get install -y i2c-tools
   
    sudo raspi-config
    
    Interfacing options > Enable I2C
    
Requires Adafruit DHT Python Libraries - https://github.com/adafruit/Adafruit_Python_DHT.git

Requires Adafruit LED Backpack Libraries - https://github.com/adafruit/Adafruit_Python_LED_Backpack.git
