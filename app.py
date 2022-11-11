from flask import Flask, render_template
from controller.van_controller import vans_blueprint
from controller.customer_controller import customers_blueprint


app = Flask(__name__)

app.register_blueprint(vans_blueprint)
app.register_blueprint(customers_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

