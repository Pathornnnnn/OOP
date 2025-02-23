class System:
    def __init__(self, acc_lst, product_lst):
        self.__acc_lst = acc_lst
        self.__product_lst = product_lst

    def search_acc_by_id(self,member_id):
        for acc in self.__acc_lst:
            if acc.get_acc_id() == member_id:
                return acc
        
    def search_product_by_name(self,name):
        for product in self.__product_lst:
            if name == product.get_name_product():
                return product
    def get_acc_lst(self):
        return self.__acc_lst
    
    def get_product_lst(self):
        return self.__product_lst

    def Add_to_cart(self, product_name , quantity, acc_id):
        product = self.search_product_by_name(product_name)
        acc = self.search_acc_by_id(acc_id)
        stock_product = product.get_stock_product()
        if stock_product >= quantity:
            itemm = Cartitem(product,quantity)
            acc.Add_to_cart_shopping(itemm)
            return True

        else:
            return False

class Account:
    def __init__(self,user_id , name , email):
        self.__id = user_id
        self.__name = name
        self.__email = email
        self.__myCart_shopping = Cart([])
    
    def get_acc_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def Add_to_cart_shopping(self,cartitemm):
        self.__myCart_shopping.Add_to_cartitem(cartitemm)

    def get_cart_shopping(self): 
        return self.__myCart_shopping
    
class Product:
    def __init__(self,product_id , name , stock):
        self.__id = product_id
        self.__name = name
        self.__stock = stock
    
    def get_name_product(self):
        return self.__name

    def get_stock_product(self):
        return self.__stock

class Cart:
    def __init__(self,Cartitem_lst=[]):
        self.__Cartitem_lst = Cartitem_lst

    def Add_to_cartitem(self,inp):
        self.__Cartitem_lst.append(inp)

    def __str__(self):
        return f'{[[i.get_product().get_name_product(), i.get__quantity() ] for i in self.__Cartitem_lst]}'

class Cartitem:
    def __init__(self, product , quantity):
        self.__product = product
        self.__quantity = quantity

    def get_product(self):
        return self.__product
    
    def get__quantity(self):
        return self.__quantity
    
    def __str__(self):
        return f'{self.__product} : {self.__quantity}'

#init usr
user_lst = []
maxkey = Account("1",'MAX','MAX@gmail.com')
jj = Account("2",'JJ','JJ@gmail.com')
user_lst.append(maxkey)
user_lst.append(jj)

#init product
product_lst = []
a = Product(1,'Monitor',10)
b = Product(2,'Keyboard',10)
product_lst.append(a)
product_lst.append(b)
bananaIT = System(user_lst,product_lst)


#test add cart
print('ID :',maxkey.get_acc_id(),'| Name :',  maxkey.get_name() ,'| Cart :', maxkey.get_cart_shopping())
print('ID :',jj.get_acc_id(),'| Name :',  jj.get_name() ,'| Cart :', jj.get_cart_shopping())

# test case
# เพิ่มสินค้า Monitor จำนวน 2 ชิ้น ลงตะกร้าของไอดี 1 (MAX)
bananaIT.Add_to_cart('Monitor',2,'1')
# เพิ่มสินค้า Keyboard จำนวน 3 ชิ้น ลงตะกร้าของไอดี 1 (MAX)
bananaIT.Add_to_cart('Keyboard',3,'1')


#test add cart
print('ID :',maxkey.get_acc_id(),'| Name :',  maxkey.get_name() ,'| Cart :', maxkey.get_cart_shopping())
print('ID :',jj.get_acc_id(),'| Name :',  jj.get_name() ,'| Cart :', jj.get_cart_shopping())