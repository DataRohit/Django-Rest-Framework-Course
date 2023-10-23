import requests
import random

# Define the API endpoint and authorization tokens for two users.
api_url = "http://localhost:8000/restapi/products/create/"
user_tokens = [
    "97ba95d99d5f6f0f49d2c039341b6969d28fc15e",
    "9125a09adaf0376519853e179a673597afb55d50",
]

data = [
    {
        "title": "Mechanical Keyboard 1",
        "category": "Keyboards",
        "description": "High-quality mechanical keyboard with RGB lighting",
        "price": 99.99,
    },
    {
        "title": "Wireless Keyboard 1",
        "category": "Keyboards",
        "description": "Sleek wireless keyboard for convenience",
        "price": 49.99,
    },
    {
        "title": "Ergonomic Keyboard",
        "category": "Keyboards",
        "description": "An ergonomic keyboard for comfortable typing",
        "price": 79.99,
    },
    {
        "title": "Compact Bluetooth Keyboard",
        "category": "Keyboards",
        "description": "Compact and portable Bluetooth keyboard",
        "price": 39.99,
    },
    {
        "title": "Gaming Keyboard",
        "category": "Keyboards",
        "description": "Gaming keyboard with customizable backlighting",
        "price": 69.99,
    },
    {
        "title": "Gaming Mouse 1",
        "category": "Mice",
        "description": "Precision gaming mouse with customizable buttons",
        "price": 79.99,
    },
    {
        "title": "Wireless Mouse 1",
        "category": "Mice",
        "description": "Wireless optical mouse for everyday use",
        "price": 29.99,
    },
    {
        "title": "Ergonomic Mouse",
        "category": "Mice",
        "description": "Ergonomically designed mouse for comfort",
        "price": 39.99,
    },
    {
        "title": "Trackball Mouse",
        "category": "Mice",
        "description": "Trackball mouse for precise cursor control",
        "price": 49.99,
    },
    {
        "title": "RGB Gaming Mouse",
        "category": "Mice",
        "description": "Gaming mouse with customizable RGB lighting",
        "price": 59.99,
    },
    {
        "title": "Ultra-thin Laptop 1",
        "category": "Laptops",
        "description": "Thin and lightweight laptop with a powerful processor",
        "price": 999.99,
    },
    {
        "title": "Business Laptop 1",
        "category": "Laptops",
        "description": "Laptop designed for professional use with long battery life",
        "price": 799.99,
    },
    {
        "title": "Convertible Laptop",
        "category": "Laptops",
        "description": "2-in-1 convertible laptop with touchscreen",
        "price": 849.99,
    },
    {
        "title": "Gaming Laptop",
        "category": "Laptops",
        "description": "High-performance gaming laptop with dedicated GPU",
        "price": 1199.99,
    },
    {
        "title": "Budget Laptop",
        "category": "Laptops",
        "description": "Affordable laptop for everyday tasks",
        "price": 499.99,
    },
    {
        "title": "27-Inch 4K Monitor 1",
        "category": "Monitors",
        "description": "High-resolution 4K monitor for stunning visuals",
        "price": 349.99,
    },
    {
        "title": "Curved Gaming Monitor 1",
        "category": "Monitors",
        "description": "Curved monitor with fast refresh rate for gaming",
        "price": 499.99,
    },
    {
        "title": "Ultrawide Monitor",
        "category": "Monitors",
        "description": "Immersive ultrawide monitor for multitasking",
        "price": 599.99,
    },
    {
        "title": "Professional Monitor",
        "category": "Monitors",
        "description": "Color-accurate monitor for professional graphics work",
        "price": 799.99,
    },
    {
        "title": "Budget Monitor",
        "category": "Monitors",
        "description": "Affordable monitor with decent image quality",
        "price": 199.99,
    },
    {
        "title": "Intel Core i7 Processor 1",
        "category": "CPUs",
        "description": "High-performance Intel Core i7 processor",
        "price": 299.99,
    },
    {
        "title": "AMD Ryzen 5 Processor 1",
        "category": "CPUs",
        "description": "AMD Ryzen 5 processor for multitasking",
        "price": 249.99,
    },
    {
        "title": "Intel Core i9 Processor",
        "category": "CPUs",
        "description": "Top-of-the-line Intel Core i9 processor",
        "price": 499.99,
    },
    {
        "title": "AMD Ryzen 7 Processor",
        "category": "CPUs",
        "description": "AMD Ryzen 7 processor for gaming and content creation",
        "price": 349.99,
    },
    {
        "title": "Budget CPU",
        "category": "CPUs",
        "description": "Affordable CPU for everyday computing",
        "price": 99.99,
    },
]

# Split the data randomly into two sets.
random.shuffle(data)
data_for_user_1 = data[: len(data) // 2]
data_for_user_2 = data[len(data) // 2 :]

# Iterate through the data for each user and send a POST request.
for user_id, user_data in enumerate([data_for_user_1, data_for_user_2], start=1):
    headers = {"Authorization": f"Bearer {user_tokens[user_id - 1]}"}
    for product_data in user_data:
        response = requests.post(api_url, json=product_data, headers=headers)
