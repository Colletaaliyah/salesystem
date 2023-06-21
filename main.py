from flask import Flask,render_template
from mytestpostgres import fetch_data

#create an object called app
#__name__ is used to tell flask where to access html files
#all html files are put inside "template" folders
#all css ,js ,images are put inside "static" folder 


app=Flask(__name__)
# print(__name__)

#a route is an extension of a url which loads you a html page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def about():
    prods=fetch_data('products')
    return render_template("products.html",prods=prods)

@app.route("/sales")
def sale():
    sales=fetch_data('sales')
    return render_template("sales.html",sales=sales)

app.run()