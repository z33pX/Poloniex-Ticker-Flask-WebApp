from gevent import monkey
monkey.patch_all()

from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from time import sleep
from threading import Thread, Event
from p_ticker import PWSTicker


__author__ = 'z33p'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'db54uztbebm4p5gb9w4p955bgvm459vhdlfjhhweheeh'
app.config['DEBUG'] = True

# Turn the flask app into a socketio app
socketio = SocketIO(app)

# Create ticker object
ticker = PWSTicker()
ticker_label = [
    'USDT_BTC', 'USDT_ETH', 
    'USDT_XMR', 'USDT_LTC',
    'USDT_DASH', 'USDT_ETC',
]

thread = Thread()
thread_stop_event = Event()

class Ticker(Thread):
    def __init__(self):
        self.delay = 1
        super(Ticker, self).__init__()
        self.last_ticker_data = dict()

    def ticker_thread(self):
        while not thread_stop_event.isSet():
            global ticker
            ticker_data = dict()
            for label in ticker_label:
                ticker_data[label] = ticker(str(label))

            if self.last_ticker_data != ticker_data:
                self.last_ticker_data = ticker_data
                print(ticker_data)
                socketio.emit('tickerData', {
                    'ticker_data': ticker_data, 
                    'ticker_label': ticker_label
                }, namespace='/tiDa')
            sleep(self.delay)

    def run(self):
        self.ticker_thread()


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/tiDa')
def test_connect():
    global thread
    print('Client connected')

    if not thread.isAlive():
        print("Starting Thread")
        thread = Ticker()
        thread.start()

@socketio.on('disconnect', namespace='/tiDa')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    ticker.start()
    socketio.run(app)
    ticker.stop()