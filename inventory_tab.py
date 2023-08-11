import uuid
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QFormLayout, QComboBox

class InventoryTab(QWidget):
    def __init__(self, products, update_inventory_list, add_inventory, clear_quantity_input, delete_inventory):
        super().__init__()

        self.products = products
        self.update_inventory_list = update_inventory_list
        self.add_inventory = add_inventory
        self.clear_quantity_input = clear_quantity_input
        self.delete_inventory = delete_inventory

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.product_dropdown = QComboBox()
        self.product_dropdown.currentIndexChanged.connect(self.clear_quantity_input)
        for product in self.products:
            self.product_dropdown.addItem(product)
        layout.addWidget(QLabel("Product:"))
        layout.addWidget(self.product_dropdown)

        self.quantity_input = QLineEdit()
        layout.addWidget(QLabel("Quantity:"))
        layout.addWidget(self.quantity_input)

        self.add_inventory_button = QPushButton("Add Inventory")
        self.add_inventory_button.clicked.connect(self.add_inventory)
        layout.addWidget(self.add_inventory_button)

        self.inventory_list = QListWidget()
        layout.addWidget(self.inventory_list)

        self.delete_inventory_button = QPushButton("Delete Inventory")
        self.delete_inventory_button.clicked.connect(self.delete_inventory) 
        layout.addWidget(self.delete_inventory_button)

        self.setLayout(layout)

    def generate_uuid(self):
        return str(uuid.uuid4())
