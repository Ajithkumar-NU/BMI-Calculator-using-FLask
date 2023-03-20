from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    bmi = ()
    if request.method == 'POST' and 'weight' in request.form :
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi  = calc_bmi(weight, height)
  
    return render_template('bmi_calc.html', bmi = bmi)

def calc_bmi(weight, height):
    return round((weight/((height/100)**2)), 2)



if __name__ == '__main__':
    app.debug = True
    app.run()