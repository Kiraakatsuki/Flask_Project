from flask import Flask,render_template # importing various modules from flask
app=Flask(__name__) #creating an instance using variable
@app.route('/') # to call or hit the function when the mentioned symbol is called. @ is used for decoration
def index() :
    fruits=["apple","orange","mango"]
    return render_template('index.html',items=fruits)

@app.route('/product') # to call or hit the function when the mentioned symbol is called. @ is used for decoration
def product() :
    return render_template('index.html')


if __name__ == '__main__' : # confirming whether the page is main page or not
    app.run(debug=True) # to run the code