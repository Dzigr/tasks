from flask import Flask, request

app = Flask(__name__)


@app.route('/Datalore', methods=['POST'])
def handle_webhook():
    webhook_data = request.json()
    function_name = webhook_data.get('function')

    try:
        function = FunctionFactory.run(function_name)
        result = function(webhook_data)
    except ValueError:
        result = {'error': 'Invalid function name'}

    return result


def function_1(data):
    return {'result': 'Function №1 executed'}


def function_2(data):
    return {'result': 'Function №2 executed'}


class FunctionFactory:

    functions = {
        'function1': function_1,
        'function2': function_2,
    }

    @classmethod
    def run(cls, function_name):
        function = cls.functions.get(function_name, None)
        if function:
            return function

        raise ValueError('Invalid function name')
