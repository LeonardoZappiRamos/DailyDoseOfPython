from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def measure_converter():
    context = {}
    if request.method == 'POST':
        print(request.form)
        conversion_type = request.form.get('conversion-type', 0)
        amount = float(request.form.get('amount', 0))
        if conversion_type == '1':
            converted_amount = amount * 0.6214
            context["product_text"] = f"{amount} kilometers is {round(converted_amount, 2)} miles"
        elif conversion_type == '2':
            converted_amount = amount * 1.6093
            context["product_text"] = f"{amount} miles is {round(converted_amount, 2)} kilometers"
        else:
            context["product_text"] = "Choose de amount and click the button"
        context["amount"] = amount
        context["conversion_type"] = conversion_type
        print(context)
    return render_template('index.html', **context)