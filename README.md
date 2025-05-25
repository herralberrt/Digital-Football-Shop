# 🛒 Albert's Football Shop

This is a responsive shopping cart web application themed around football.
It allows users to browse football jerseys and boots, add items to the cart, modify quantities, and place an order. The app uses Flask, HTML/CSS with Bootstrap, JavaScript, and is containerized with Docker.

---

## 🚀 Features

* Browse football jerseys and boots
* Add items to cart dynamically (JavaScript `fetch()`)
* Live cart counter in navbar
* Modify quantity or remove items
* Checkout with form (name, email, address)
* Order saved to `data/orders.json`
* Toast notifications after adding to cart
* Responsive layout with Bootstrap
* Fully Dockerized for deployment

---

## 🧠 Technologies Used

* Python 3.10
* Flask
* Jinja2
* Bootstrap 5
* JavaScript (vanilla)
* Docker

---

## 📁 Project Structure

```
.
├── app.py                  # Flask main app
├── requirements.txt        # Dependencies
├── Dockerfile              # For Docker container
├── README.md               # Project documentation
├── /templates              # HTML templates (Jinja2)
│   ├── base.html
│   ├── index.html
│   ├── cart.html
│   ├── checkout.html
│   └── thank_you.html
├── /static
│   ├── css/style.css
│   ├── js/cart.js
│   └── images/
└── /data
    └── orders.json         # Saved orders
```

---

## 🐳 How to Run with Docker

```bash
# Step 1: Build Docker image
docker build -t football-shop .

# Step 2: Run container
docker run -p 5000:5000 football-shop

# Step 3: Open in browser
http://localhost:5000
```

---

## 📩 Contact Info (Demo Content)

* **Name:** Albert Iulian Romaniuc
* **Email:** [albertiulianromaniuc@gmail.com](mailto:albertiulianromaniuc@gmail.com)

---

## ⭐ Bonus Implemented

* JavaScript cart updates (no reload)
* Toast-style notifications
* Live cart count in navbar
* Responsive design with Bootstrap
* Styled "Thank you" page after checkout

---

## 📌 Notes

* Orders are saved locally in `data/orders.json`
* No login system was required or implemented
* Prices are in EUR (converted manually or set directly)
