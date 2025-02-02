from flask import Flask


def create_app():
    app = Flask(__name__)
    def testing():
        print("hi testing...")
    @app.route('/')
    def home():
        print("hi hello")
        return 'GeeksForGeeks'

    return app
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
