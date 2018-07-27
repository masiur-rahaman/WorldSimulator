from flask import Flask
from Engine import Engine
from ResultAccumulator import ResultAccumulator

app = Flask(__name__)

result_accumulator = ResultAccumulator()


@app.route('/')
def hello_name():
    return result_accumulator.get()


if __name__ == '__main__':
    engine = Engine(result_accumulator)
    engine.start()
    app.run(debug=True)
