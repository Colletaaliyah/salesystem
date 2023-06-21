import psycopg2
try:
# Connect to your postgres DB
    conn = psycopg2.connect("dbname=postgres user=postgres password=Candidcoco@20")

    # Open a cursor to perform database operations
    cur = conn.cursor()
except Exception as e:
    print(e)

def fetch_data(tbln):
    try:
        q="SELECT * FROM " + tbln + ';'
        cur.execute(q)
        records = cur.fetchall()
        return records
    except Exception as e:
        return e
    
def insert_product(v):
        vs=str(v)
        q= "INSERT INTO products(name, buying_price, selling_price, quantity)"\
            "VALUES" + vs
        cur.execute(q)
        conn.commit()
        return "product added successfully"

# p1=insert_product(('popcorn',50,50,30))
# print(p1)
# p1=insert_product(('broccoli',40,60,10))
# print(p1)

# data = fetch_data("products")
# print(data)
# Execute a query
# cur.execute("SELECT * FROM products")

# Retrieve query results
# records = cur.fetchall()

# print(records)
#store all product names in alist and only print that list. do not filter in the query.
# newlist=[i[1] for i in records]
# print(newlist)
