from flask import Flask


def create_app():
    app = Flask(__name__)
    x=10
    y=20
    @app.route('/')
    def home():
        return 'GeeksForGeeks'

    return app

def a():
    print("test")
    a()
def a():
    print("test")
    a()
a()
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
