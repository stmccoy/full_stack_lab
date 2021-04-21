from flask import Flask, render_template

from controllers.tasks_controller import tasks_blueprint

app = Flask(__name__)

# Register the blueprint with the flask app

app.register_blueprint(tasks_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)