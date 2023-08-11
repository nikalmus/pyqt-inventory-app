import sys
import uuid
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QAction, QTabWidget, QFormLayout, QComboBox, QHBoxLayout

class InventoryApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.products = []
        self.inventory = []

        self.setWindowTitle("Inventory Tracking App")
        self.setGeometry(100, 100, 600, 400)

        self.init_ui()

    def init_ui(self):
        self.tab_widget = QTabWidget()

        self.products_tab = QWidget()
        self.init_products_tab()
        self.tab_widget.addTab(self.products_tab, "Products")

        self.inventory_tab = QWidget()
        self.init_inventory_tab()
        self.tab_widget.addTab(self.inventory_tab, "Inventory")

        self.setCentralWidget(self.tab_widget)

    def init_products_tab(self):
        layout = QVBoxLayout()

        self.product_name_label = QLabel("Product Name:")
        self.product_name_input = QLineEdit()
        layout.addWidget(self.product_name_label)
        layout.addWidget(self.product_name_input)

        self.add_product_button = QPushButton("Add Product")
        self.add_product_button.clicked.connect(self.add_product)
        layout.addWidget(self.add_product_button)

        self.product_list = QListWidget()
        layout.addWidget(self.product_list)

        self.delete_product_button = QPushButton("Delete Product")
        self.delete_product_button.clicked.connect(self.delete_product)
        layout.addWidget(self.delete_product_button)

        self.products_tab.setLayout(layout)

    def init_inventory_tab(self):
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

        self.inventory_tab.setLayout(layout)

    def generate_uuid(self):
        generated_uuid = str(uuid.uuid4())
        self.serial_number_input.setText(generated_uuid)

    def add_product(self):
        product_name = self.product_name_input.text()
        if product_name:
            self.products.append(product_name)
            self.product_name_input.clear()
            self.update_product_list()
            self.product_dropdown.addItem(product_name)

    def delete_product(self):
        selected_items = self.product_list.selectedItems()
        for item in selected_items:
            product_name = item.text()
            self.products.remove(product_name)
            self.product_dropdown.removeItem(self.product_dropdown.findText(product_name))
        self.update_product_list()

    def add_inventory(self):
        product = self.product_dropdown.currentText()
        quantity = self.quantity_input.text()

        if product and quantity:
            for _ in range(int(quantity)):
                serial_number = str(uuid.uuid4())
                self.inventory.append((product, serial_number))
            self.update_inventory_list()

    def clear_quantity_input(self):
        self.quantity_input.clear()

    def update_product_list(self):
        self.product_list.clear()
        self.product_list.addItems(self.products)

    def update_inventory_list(self):
        self.inventory_list.clear()
        for item in self.inventory:
            self.inventory_list.addItem(f"Product: {item[0]} - Serial Number: {item[1]}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec_())
