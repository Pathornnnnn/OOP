class System:
    def __init__(self, acc_lst, product_lst):
        self.__acc_lst = acc_lst
        self.__product_lst = product_lst

    def search_acc_by_id(self,id):
        for i in self.__acc_lst:
            if i.get_acc_id() == id:
                return i
        
    def search_produch_by_name(self,name):
        for i in self.__product_lst:
            if name == i.get_name_product():
                return i
    def get_acc_lst(self):
        return self.__acc_lst
    
    def get_product_lst(self):
        return self.__product_lst

    def add_cart(self, product_name , quantity, acc_id):
        product = self.search_produch_by_name(product_name)
        acc = self.search_acc_by_id(acc_id)
        print(acc)
        itemm = CartItem(product,quantity)
        acc.add_cart_shopping(itemm)

class Account:
    def __init__(self,user_id , name , email):
        self.__id = user_id
        self.__name = name
        self.__email = email
        self.__myCart_shopping = []
    
    def get_acc_id(self):
        return self.__id

    def add_cart_shopping(self,cartitemm):
        self.__myCart_shopping.append(cartitemm)


    def get_cart_shopping(self):
        return self.__myCart_shopping
class Product:
    def __init__(self,product_id , name):
        self.__id = product_id
        self.__name = name
    
    def get_name_product(self):
        return self.__name

class CartItem:
    def __init__(self, product , quantity):
        self.__product = product
        self.__quantity = quantity


#init 
user_lst = []
maxkey = Account("1",'MAX','MAX@gmail.com')
jj = Account("2",'JJ','JJ@gmail.com')
user_lst.append(maxkey)
user_lst.append(jj)
product_lst = []
a = Product(1,'A')
b = Product(2,'B')
product_lst.append(a)
product_lst.append(b)
bananaIT = System(user_lst,product_lst)

# test
# เพิ่มสินค้า A จำนวน 2 ชิ้น ลงตะกร้าของไอดี 1 (MAX)
bananaIT.add_cart('A',2,'1')

#test add cart
print(maxkey.get_cart_shopping())
