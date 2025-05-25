from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

products = [
    {
        "name": "USA Jersey",
        "image": "usa-shirt.jpg",
        "price": 50,
        "description": "Official 2024 home jersey of the USA national team."
    },
    {
        "name": "Barcelona Jersey",
        "image": "barcelona-shirt.png",
        "price": 70,
        "description": "Classic design inspired by Barça's iconic colors."
    },
    {
        "name": "Roma Jersey",
        "image": "asroma-shirt.jpg",
        "price": 40,
        "description": "Authentic AS Roma home jersey with sponsor print."
    },
    {
        "name": "PSG Jersey",
        "image": "psg-shirt.jpg",
        "price": 60,
        "description": "Paris Saint-Germain home shirt, modern and elegant."
    },
    {
        "name": "Nike Mercurial",
        "image": "nike-mercurial.jpg",
        "price": 130,
        "description": "Built for explosive speed and agility on the pitch."
    },
    {
        "name": "Nike Phantom",
        "image": "nike-phantom.jpg",
        "price": 150,
        "description": "Precision-driven design for playmakers and finishers."
    },
    {
        "name": "Nike Tiempo",
        "image": "nike-tiempo.jpg",
        "price": 100,
        "description": "Classic comfort and elite-level touch control."
    },
    {
        "name": "Nike Superfly",
        "image": "nike-superfly.jpg",
        "price": 120,
        "description": "Dynamic fit collar for locked-in speed and traction."
    }
]

@app.route('/')
def index():
    return render_template("index.html", products=products)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_name = request.form.get('product_name')
    product = next((p for p in products if p['name'] == product_name), None)
    if not product:
        return jsonify({"success": False, "message": "Product not found."}), 404
    if 'cart' not in session:
        session['cart'] = {}
    cart = session['cart']
    if product_name in cart:
        cart[product_name]['quantity'] += 1
    else:
        cart[product_name] = {
            'price': product['price'],
            'image': product['image'],
            'quantity': 1
        }
    session.modified = True
    total_items = sum(item['quantity'] for item in cart.values())
    return jsonify({
        "success": True,
        "message": f"{product_name} has been added to your cart!",
        "cart_count": total_items
    })

@app.context_processor
def inject_cart_count():
    cart = session.get('cart', {})
    total_items = sum(item['quantity'] for item in cart.values())
    return {'cart_count': total_items}

@app.route('/update_cart', methods=['POST'])
def update_cart():
    product_name = request.form.get('product_name')
    action = request.form.get('action')

    if 'cart' in session and product_name in session['cart']:
        if action == 'increase':
            session['cart'][product_name]['quantity'] += 1
        elif action == 'decrease':
            session['cart'][product_name]['quantity'] -= 1
            if session['cart'][product_name]['quantity'] <= 0:
                session['cart'].pop(product_name)
        session.modified = True
    return redirect(url_for('cart'))

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    product_name = request.form.get('product_name')
    if 'cart' in session and product_name in session['cart']:
        session['cart'].pop(product_name)
        session.modified = True
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render_template("cart.html", cart=cart, total=total)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        order = {
            'name': name,
            'email': email,
            'address': address,
            'items': cart,
            'total': total
        }
        os.makedirs('data', exist_ok=True)
        filepath = os.path.join('data', 'orders.json')
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                orders = json.load(f)
        else:
            orders = []
        orders.append(order)
        with open(filepath, 'w') as f:
            json.dump(orders, f, indent=2)
        session['cart'] = {}
        session.modified = True
        return render_template("ty.html")
    return render_template("checkout.html", cart=cart, total=total)

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
