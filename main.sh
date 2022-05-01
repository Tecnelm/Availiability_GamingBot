#!/bin/bash

cd /Availiability_GamingBot/
sed -i 's/$token/'$TOKEN'/' ./config.yml 
sed -i 's/$timeMinAFK/'$TIME_MIN_AFK'/' ./config.yml 
sed -i 's/$mac/'$MAC'/' ./config.yml 
sed -i 's/$port/'$PORT'/' ./config.yml
sed -i 's/$address/'$ADDRESS'/' ./config.yml

python3 main.py


