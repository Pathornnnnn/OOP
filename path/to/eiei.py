from fasthtml.common import *

app, rt = fast_app()

class Product:
    def __init__(self, name, price: str, is_available=True):
        self.name = name
        self.price = price
        self.is_available = is_available

    # def __str__(self):
    #     status = "มี" if self.is_available else "ไม่มี"
    #     return f"สินค้า {self.name} {status}ครับ/ค่ะ"
    
class System:
    def __init__(self):
        self.lst_product = []
    
    def add_product(self, product):
        self.lst_product.append(product)

    def search(self, search):
        result = []
        for product in self.lst_product:
            if search.lower() in product.name.lower():
                result.append(product)
        return result
            
system = System()
phone1 = Product("Iphone", "15,000")
phone2 = Product("Samsung", "10,000")
phone3 = Product("OnePlus", "12,000", is_available=False)

system.add_product(phone1)
system.add_product(phone2)
system.add_product(phone3)


@rt('/')
def get():
    return Titled("Search Product",
                Form(Input(id="search", placeholder="Search products...",
                    hx_get="/search", target_id="results", hx_trigger="keyup delay:500ms")),
                Div(id="results", *[Card(
                    H3(product.name),
                    P(f"Price : {product.price} THB"),
                    P(f"Status : {'Available' if product.is_available else 'Unavailable'}")
                )for product in system.lst_product]))

@rt('/search')
def get(search: str):
    results = system.search(search)
    if results:
        return Div(*[Card(
            H3(product.name),
            P(f"Price : {product.price} THB"),
            P(f"Status : {'Available' if product.is_available else 'Unavailable'}")
        )for product in results])
    else:
        return Div(P("Products Not Found."))

serve()