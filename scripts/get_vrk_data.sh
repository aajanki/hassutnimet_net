#!/bin/sh

if [ ! -f data/raw/Etunimitilasto-2017-04-06-VRK.xls ]; then
   wget https://www.avoindata.fi/dataset/57282ad6-3ab1-48fb-983a-8aba5ff8d29a/resource/1db08a34-8948-48bc-89a6-0a95fdfa4a76/download/Etunimitilasto-2017-04-06-VRK.xls -O data/raw/Etunimitilasto-2017-04-06-VRK.xls
fi
if [ ! -f data/raw/Sukunimitilasto-2017-04-06-VRK.xls ]; then
   wget https://www.avoindata.fi/dataset/57282ad6-3ab1-48fb-983a-8aba5ff8d29a/resource/af5b50bf-094e-41a5-bdde-80f5c4e11620/download/Sukunimitilasto-2017-04-06-VRK.xls -O data/raw/Sukunimitilasto-2017-04-06-VRK.xls
fi

echo "Name,Count" > data/first-names-male.csv
in2csv --sheet "Miehet kaikki" data/raw/Etunimitilasto-2017-04-06-VRK.xls | tail -n +2 >> data/first-names-male.csv

echo "Name,Count" > data/first-names-female.csv
in2csv --sheet "Naiset kaikki" data/raw/Etunimitilasto-2017-04-06-VRK.xls | tail -n +2 >> data/first-names-female.csv

echo "Name,Count" > data/last-names.csv
in2csv --sheet "Nimet" data/raw/Sukunimitilasto-2017-04-06-VRK.xls | tail -n +2 >> data/last-names.csv
