# Poloniex-Ticker-Flask-WebApp
This is a basic WebApp build with Flask and JS. 
It shows a table of the latest ticker data from Poloniex. Everything is based on Websockets.

# Setup
- Download this project:

```
git clone https://github.com/z33pX/Poloniex-Ticker-Flask-WebApp.git
```

- Create Virtual Environment:

```
cd Poloniex-Ticker-Flask-WebApp 
python3 -m venv venv
```

- Install important stuff:

```
source venv/bin/activate
pip install -r requirements.txt
```

- You have to install poloniex manually because pip references an older poloniex version.

```
pip3 install https://github.com/s4w3d0ff/python-poloniex/archive/v0.4.7.zip
```

- Start the app
```
python application.py
```

Now open `http://localhost:5000/` in your browser.

# Example

![](https://github.com/z33pX/Poloniex-Ticker-Flask-WebApp/blob/master/01.png)