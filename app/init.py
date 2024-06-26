from flask import Flask
from app.config import Config

print("Creating Flask app...")
app = Flask(__name__)

print("Configuring Flask app...")
app.config.from_object(Config)

from app import views
print("Flask app setup complete.")