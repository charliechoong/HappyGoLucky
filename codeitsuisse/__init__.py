from flask import Flask
app = Flask(__name__)
import codeitsuisse.routes.square
import codeitsuisse.routes.inventory_management
import codeitsuisse.routes.fruitbasket



