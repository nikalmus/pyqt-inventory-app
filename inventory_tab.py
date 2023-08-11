from PyQt5.QtWidgets import QLineEdit, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QComboBox
import uuid

class InventoryTab(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parentApp = parent

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.product_dropdown = QComboBox()
        self.populate_product_dropdown()  # Populate the product dropdown
        self.product_dropdown.currentIndexChanged.connect(self.clear_quantity_input)  
        
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
        self.delete_inventory_button.clicked.connect(self.delete_selected_inventory)
        layout.addWidget(self.delete_inventory_button)

        self.setLayout(layout)

    def populate_product_dropdown(self):
        self.product_dropdown.clear() # fixes items being duplicated when dropdown is clicked
        self.product_dropdown.addItems(self.parentApp.products)

    def clear_quantity_input(self):
        self.quantity_input.clear()

    def add_inventory(self):
        product = self.product_dropdown.currentText()
        quantity = self.quantity_input.text()

        if product and quantity:
            for _ in range(int(quantity)):
                serial_number = str(uuid.uuid4())
                self.parentApp.inventory.append((product, serial_number))
            self.update_inventory_list()

    def delete_selected_inventory(self):
        selected_items = self.inventory_list.selectedItems()
        for item in selected_items:
            inventory_item_text = item.text()
            serial_number = inventory_item_text.split(" - Serial Number: ")[1]
            for inv_item in self.parentApp.inventory:
                if inv_item[1] == serial_number:
                    self.parentApp.inventory.remove(inv_item)
                    break
        self.update_inventory_list()


    def update_inventory_list(self):
        self.inventory_list.clear()
        for item in self.parentApp.inventory:
            self.inventory_list.addItem(f"Product: {item[0]} - Serial Number: {item[1]}")
