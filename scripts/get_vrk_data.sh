#!/bin/sh

if [ ! -f data/raw/etunimitilasto-2019-08-07-vrk.xlsx ]; then
   mkdir -p data/raw && wget https://www.avoindata.fi/data/dataset/57282ad6-3ab1-48fb-983a-8aba5ff8d29a/resource/46f4f0b1-dc1f-4c28-a23b-2fba6cfa19b4/download/etunimitilasto-2019-08-07-vrk.xlsx -O data/raw/etunimitilasto-2019-08-07-vrk.xlsx
fi
if [ ! -f data/raw/Sukunimitilasto-2019-08-07-vrk.xlsx ]; then
   wget https://www.avoindata.fi/data/dataset/57282ad6-3ab1-48fb-983a-8aba5ff8d29a/resource/a32aa571-23aa-4bfc-ba72-106f74c5252e/download/sukunimitilasto-2019-08-07-vrk.xlsx -O data/raw/sukunimitilasto-2019-08-07-vrk.xlsx
fi

echo "Name,Count" > data/first-names-male.csv
in2csv --sheet "Miehet kaikki" data/raw/etunimitilasto-2019-08-07-vrk.xlsx | tail -n +2 >> data/first-names-male.csv

echo "Name,Count" > data/first-names-female.csv
in2csv --sheet "Naiset kaikki" data/raw/etunimitilasto-2019-08-07-vrk.xlsx | tail -n +2 >> data/first-names-female.csv

echo "Name,Count" > data/last-names.csv
in2csv --sheet "Sukunimet" data/raw/sukunimitilasto-2019-08-07-vrk.xlsx | tail -n +2 >> data/last-names.csv
