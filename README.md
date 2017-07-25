# Silly name generator

This program generates silly Finnish person names.

The program uses a Markov chain to generate random letter sequences that locally resemble person names. Real names (used by at least 10 persons according to Väestörekisterikeskus) are filtered out leaving only hopefully funny name-like results.

Some examples of the generated names:
* Kaara Keiskanen
* Velix Minkkonen
* Annelena Maariannikki Nesterlund
* Pekka-Pekka Thor Elovirtanen
* Gunneli Pirkko-Liisabeth Puuma
* Katrica Järvi-Latva-Kiikert

## Usage

Requires Python 3.6.

### 1. Setup a Python virtual environment with the required libraries

```
virtualenv -p python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Fetch the Finnish name data set from avoindata.fi

```
scripts/get_vrk_data.sh
```

This downloads [an open Finnish name data set](https://www.avoindata.fi/data/fi/dataset/none), preprocesses it, and stores it in the subdirectory data.

### 3. Start the web server

```
FLASK_APP=namegenserver.py flask run
```

### 4. Run the application

Open [http://localhost:5000](http://localhost:5000) on a web browser.

Alternatively, run the command line script that prints a bunch of random names:
```
python namegenerator.py
```
