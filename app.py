from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return '''
            <form method="post">
                <label>Enter your name here</label>
                <input type='text' name='name'>
                <h2>ADDITION</h2>
                <div><label>Enter first number</label>
                <input type='text' name="num1"></div>
                <div><label>Enter second number</label>
                <input type='text' name="num2"></div>
                <div>
                <input type='submit' value='Add'></div>
            </form>
        '''
    elif request.method == 'POST':
            Name = request.form.get('name')   
            num1 = request.form.get('num1')
            num2 = request.form.get('num2')
            sum = float(num1) + float(num2)
            return '<h2>Your sum is: %f</h2>' %sum

if __name__ == '__main__':
    app.run(debug=True)