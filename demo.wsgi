from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Makes a great meal.'

if __name__ == '__main__':
    app.run()

#hamburgers
