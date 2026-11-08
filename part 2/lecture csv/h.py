import csv 
# optional parameters 
def getProducts(category = ""):
    products = []
    with open("stock.csv","r") as file:
        columns = ["ID","Name","Category","Price"]
        reader = csv.DictReader(file,fieldnames=columns)
        for product in reader:
            if category in product["Category"]:
                products.append(product)
    return products

def getProductByID(id):
    with open("stock.csv","r") as file:
        columns = ["ID","Name","Category","Price"]
        reader = csv.DictReader(file,fieldnames=columns)
        for product in reader:
            if product["ID"] == str(id):
                return product 
    return None 

def displayProducts(products=None):
    if products == None:
        products = getProducts()
    print("######## Products #######")
    for product in products:
        print(f"ID: {product["ID"]}\nName: {product["Name"]}\nCategory: {product["Category"]}\nPrice: {product["Price"]}")
        print("-----")
    print("######################")

def searchByCategory():
    category = input("Enter the category: ")
    products = getProducts(category)
    return products 

def addToCart(products):
    with open("cart.csv","a",newline="") as file:
        columns = ["ID","Name","Category","Quantity","Price"]
        writer = csv.DictWriter(file,fieldnames=columns)
        writer.writerows(products)

def cart():
    flag = True 
    bag = [] 
    while True:
        break