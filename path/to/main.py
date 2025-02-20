from fasthtml.common import *

app , rt = fast_app()

@rt('/')
def cart_modal():
    return Html(
        Div(
            {"id": "cart-modal", "class": "fixed inset-0 bg-gray-900 bg-opacity-50 flex justify-center items-center hidden"},
            Div(
                {"class": "bg-white p-6 rounded-lg w-96 shadow-lg"},
                Div({"class": "text-lg font-semibold mb-4"}, "Your Cart"),
                Ul({"class": "space-y-4"},
                   Li({"class": "flex justify-between items-center"}, Span("Product 1"), Span("$99.99")),
                   Li({"class": "flex justify-between items-center"}, Span("Product 2"), Span("$149.99")),
                   Li({"class": "flex justify-between items-center"}, Span("Product 3"), Span("$249.99"))
                ),
                Div(
                    {"class": "mt-6 flex justify-between"},
                    Button({"class": "bg-red-500 text-white py-2 px-4 rounded-lg w-fUll hover:bg-red-600", "onclick": "closeCartModal()"}, "Close"),
                    Button({"class": "bg-blue-500 text-white py-2 px-4 rounded-lg w-fUll hover:bg-blue-600"}, "Proceed to Checkout")
                )
            )
        )
    )

def top_navigation():
    return Html(
        Header({"class": "bg-gray-800 text-white p-4"},
            Div({"class": "container mx-auto flex justify-between items-center"},
                Div({"class": "text-2xl font-bold"}, "MyShop"),
                Nav({"class": "hidden md:flex space-x-6"},
                    A({"href": "#", "class": "hover:text-orange-500"}, "Home"),
                    A({"href": "#", "class": "hover:text-orange-500"}, "Shop"),
                    A({"href": "#", "class": "hover:text-orange-500"}, "About"),
                    A({"href": "#", "class": "hover:text-orange-500"}, "Contact")
                ),
                Div({"class": "relative w-1/4"},
                    input({"type": "text", "placeholder": "Search products...", "class": "w-fUll p-2 rounded-lg text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500"})
                ),
                Div({"class": "flex space-x-4 items-center"},
                    A({"href": "#", "class": "hover:text-orange-500"}, "Account"),
                    A({"href": "#", "class": "relative hover:text-orange-500", "id": "cart-icon"},
                        Svg({"xmlns": "http://www.w3.org/2000/svg", "fill": "none", "viewBox": "0 0 24 24", "stroke": "currentColor", "class": "w-6 h-6"}
                        ),
                        Span({"class": "absolute top-0 right-0 bg-red-500 text-white text-xs rounded-full w-4 h-4 flex items-center justify-center"}, "3")
                    )
                )
            )
        )
    )

def select_item_page():
    return Html(
        top_navigation(),
        Div({"class": "container mx-auto p-8"},
            Div({"class": "bg-white shadow-md rounded-lg p-6 grid grid-cols-1 md:grid-cols-2 gap-6"},
                Div({"class": "text-xl font-semibold mb-4"}, "Product Name: Lenovo ThinkVision S22i-30"),
                Div({"class": "text-lg text-orange-500 font-bold mb-6"}, "$249.99"),
                Div({"class": "mb-6"}, "The Lenovo ThinkVision S22i-30 is a high-quality, versatile monitor perfect for your home or office workspace. With a 21.5-inch display, it provides excellent picture quality and ergonomics for long hours of use."),
                Div(
                    Img({"src": "https://www.2beshop.com/images/products/Lenovo%20ThinkVision%20S22i-30.jpg", "alt": "Lenovo ThinkVision S22i-30", "class": "w-full h-full object-cover rounded-lg mb-4"})
                )
            ),
            Div({"class": "flex justify-between mt-6"},
                Form({"action": "/add-to-cart", "method": "post", "class": "flex-1"},
                    Input({"type": "hidden", "name": "product_id", "value": "123"}),
                    Button({"type": "submit", "class": "bg-green-500 text-white py-2 px-4 rounded-lg w-full hover:bg-green-600"}, "Add to Cart")
                ),
                Form({"action": "/purchase", "method": "post", "class": "flex-1"},
                    Input({"type": "hidden", "name": "product_id", "value": "123"}),
                    Button({"type": "submit", "class": "bg-blue-500 text-white py-2 px-4 rounded-lg w-full hover:bg-blue-600"}, "Purchase")
                )
            )
        ),
        cart_modal()
    )

# To render the Html, you would call select_item_page() and render it to a file or a web page
serve()