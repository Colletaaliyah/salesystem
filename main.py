from flask import Flask,render_template,request,redirect
from mytestpostgres import fetch_data, salesperday
from mytestpostgres import insert_product,insert_sales
import pygal
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


@app.route("/inventories")
def inventories():
            # import pandas as pd
            from datetime import datetime
            # from dateutil import parser
            daily_sales=salesperday()
            dates=[]
            sales=[]
            for i in (daily_sales):
                    dates.append(((i[0])))
                                #  '%Y-%m-%d %H:%M:%S.%f')
                    # dates.append(i[0])
                    sales.append(i[1])
            print(dates)
            print(sales) 
            chart = pygal.Line()
            chart.title = 'sales Per Day'
            chart.x_labels = ["dates"]
            chart.y_labels = ["sales"]
            chart.add('dates', dates)
            chart.add('sales', sales)
            inventories=chart.render_data_uri()
            return render_template("inventories.html",inventories=inventories)
     
    #  except Exception:
    #     bar_chart = pygal.Bar()
    #     bar_chart.title = 'Total Sales'
    #     bar_chart.add('created_at', 100)
    #     bar_chart.add('Sales', 200)
    #     bar_chart.render()
    #     inventories=bar_chart.render_data_uri()
    #     return render_template("inventories.html",inventories=inventories)

@app.route("/sales")
def sale():
    sales=fetch_data('sales')
    prods=fetch_data('products')
    return render_template("sales.html",sales=sales,prods=prods)

@app.route("/addproducts",methods=['POST','GET'])
def addproducts():
    if request.method=='POST':
        name=request.form["name"]
        buying_price=request.form["buying_price"]
        selling_price=request.form["selling_price"]
        quantity=request.form["quantity"]
        Sales_amount=quantity*selling_price
        print(name)
        print(buying_price)
        print(selling_price)
        print(quantity)
        product=(name,buying_price,selling_price,quantity)
        insert_product(product)
        return redirect("/products")



@app.route("/addsales",methods=['POST','GET'])
def addsales():
    if request.method=='POST':
        pid=request.form["pid"]
        quantity=request.form["quantity"]
        print(pid)
        print(quantity)
        sale=(pid,quantity,"now()")
        insert_sales(sale)
        return redirect("/sales")
    
# @app.route("/addinventories",methods=['POST','GET'])
# def addinventories():
#     if request.method=='POST':
#         inventories=request.form["inventories"]
#         print(inventories)
#         insert_inventories(inventories)
#         return redirect("/inventories")
app.run(debug=True)