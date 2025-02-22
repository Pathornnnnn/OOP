from fasthtml.common import *

app , rt = fast_app()

@rt('/p/Monitor')
def get():
    return Titled(
        "Banana : Select Item Page",
        Div(
            Container(
                P("DELL P2425H 23.8 INCH IPS FHD 100HZ 5MS *จอคอมพิวเตอร์"),
                Grid(
                    Img(src="https://storage.googleapis.com/file-computeandmore/large_images/3627867c-c3b1-4db0-b9eb-27b9a4b15ffe.png",style="width: 300px; height: 300px;", alt="ตัวอย่างภาพ"),
                    style="text-align: center; background-color:rgb(182, 255, 253);"
                ),
                Container(
                    Grid(
                        
                        Div(P("ทำงานได้อย่างมีประสิทธิภาพ รับความสบายตาที่เพิ่มมากขึ้นและการเชื่อมต่อที่ราบรื่นด้วยจอภาพ FHD ที่ได้รับการรับรองจาก TÜV ว่าสบายตาในระดับ 4 ดาวจุดเด่นสินค้าลดการปล่อยแสงสีฟ้าอันเป็นอันตรายเหลือ ≤35% เพื่อความสบายตลอดทั้งวันโดยไม่ต้องเสียสละสีสันอัตราการรีเฟรช 100Hz ช่วยลดการสั่นไหว เลื่อนภาพได้ลื่นไหลยิ่งขึ้น และเคลื่อนไหวได้ราบรื่นยิ่งขึ้นครอบคลุมสีที่กว้างโดยมีสีที่แสดงได้สูงสุดถึง 16.7 ล้านสีที่ 99% sRGBสีสันสดใสในมุมมองที่กว้างด้วยเทคโนโลยี In-Plane Switching (IPS)"), cls="box")
                    ),
                    Button("Add Cart",style="margin-right: 20px; text-align: center;"),Button("Purchase",style="text-align: center;"),
                    style="text-align: center; background-color:rgb(94, 93, 93);"
                )     
            )
        )

    )

@rt('/p/Keyboard')
def get():
    return Titled(
        "Banana : Select Item Page",
        Div(
            Container(
                P("คีย์บอร์ดเกมมิ่ง Signo Gaming Keyboard Nuzzon KB-751 Wireless Mechanical Black (Blue Switch)"),
                Grid(
                    Img(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp7b8xCcf89FHFziDHJ8Asl1k3dHk49AlMgA&s",style="width: 300px; height: 300px;", alt="ตัวอย่างภาพ"),
                    style="text-align: center; background-color:rgb(182, 255, 253);"
                ),
                Container(
                    Grid(
                        
                        Div(P("KB 751 NUZZON PUDDING WIRELESS OPTICAL SWITCH KEYBOARD การส่งคำสั่งและการตอบสนองที่เร็วกว่าเพียง 2 MS ทำงานด้วยระบบ INFARED ตอบสนองได้เร็วกว่า มีความทนทานและแก้ปัญหาปุ่มเบิ้ล รองรับการกดได้มากถึง 100 ล้านครั้ง  ใช้งานได้นานสูงสุด 20 ชม. ( แบบปิดไฟ ) 10 ชม. (แบบเปิดไฟ) วัสดุเป็นพลาสติก ABS แข็งแรง ทนทาน  มีฟังค์ชั่นล็อควินโดว์ ปุ่มคีย์บอร์ดแบบจมเพิ่มความเรียบหรู พร้อมอะแดปเตอร์ขยายตัวรับสัญญาน"), cls="box")
                    ),
                    Button("Add Cart",style="margin-right: 20px; text-align: center;"),Button("Purchase",style="text-align: center;"),
                    style="text-align: center; background-color:rgb(94, 93, 93);"
                )     
            )
        )

    )


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
        itemm = Cartitem(product,quantity)
        acc.add_cart_shopping(itemm)

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
    
    def add_cart_shopping(self,cartitemm):
        self.__myCart_shopping.add_Cartitem(cartitemm)

    def get_cart_shopping(self): 
        return self.__myCart_shopping
    
class Product:
    def __init__(self,product_id , name):
        self.__id = product_id
        self.__name = name
    
    def get_name_product(self):
        return self.__name


class Cart:
    def __init__(self,Cartitem_lst=[]):
        self.__Cartitem_lst = Cartitem_lst

    def add_Cartitem(self,inp):
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
a = Product(1,'Monitor')
b = Product(2,'Keyboard')
product_lst.append(a)
product_lst.append(b)

#init System
bananaIT = System(user_lst,product_lst)

# TEST API
# เพิ่มสินค้า Monitor จำนวน 2 ชิ้น ลงตะกร้าของไอดี 1 (MAX)
bananaIT.add_cart('Monitor',2,'1')
# เพิ่มสินค้า Monitor จำนวน 2 ชิ้น ลงตะกร้าของไอดี 1 (MAX)
bananaIT.add_cart('Keyboard',5,'1')


#test add cart
print('ID :',maxkey.get_acc_id(),'| Name :',  maxkey.get_name() ,'| Cart :', maxkey.get_cart_shopping())
print('ID :',jj.get_acc_id(),'| Name :',  jj.get_name() ,'| Cart :', jj.get_cart_shopping())




serve()