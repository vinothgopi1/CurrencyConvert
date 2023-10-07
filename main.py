from flask import Flask
from flask import render_template, request, redirect, url_for
import json
import requests
import math

app = Flask(__name__)

@app.route('/', methods = ['get', 'post'])
def toConverter():
    return redirect(url_for('home'))
    

@app.route('/home', methods = ['get', 'post'])
def home():
    def conversion(initial, conversion_rate):
        if initial == None or initial == ' ':
            initial = 0
        output = int(initial) * conversion_rate
        return output


    print('outside')
    print(request.method)
    if request.method == "POST":
        print('inside')
        initial_currency = request.form['start_currency']
        print(initial_currency)
        amount = request.form['amount']
        print(amount)
        convert_currency = request.form['convert_currency']
        print(convert_currency)

        new = str(convert_currency)
        original = str(initial_currency)

        url = (f"http://apilayer.net/api/live?access_key=ab5d299e6fd0c8963287ef7c03a970af&currencies={new}&source={original}")
        print(url)

        response = requests.get(url)
    
        print(response)
        response_dict = response.json()
        temp = response_dict['quotes']
        for key in temp:
            conversion_rate = (temp[key])
        x = (conversion(amount, conversion_rate))
        x = round(x, 2)
        print(x)

        return render_template('home.html', convert_value = x)
      
    return render_template('home.html')













