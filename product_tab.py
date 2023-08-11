from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget

class ProductTab(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parentApp = parent

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.product_name_label = QLabel("Product Name:")
        self.product_name_input = QLineEdit()
        layout.addWidget(self.product_name_label)
        layout.addWidget(self.product_name_input)

        self.add_product_button = QPushButton("Add Product")
        self.add_product_button.clicked.connect(self.add_product)  # Connect the button click to add_product method
        layout.addWidget(self.add_product_button)

        self.product_list = QListWidget()
        layout.addWidget(self.product_list)

        self.delete_product_button = QPushButton("Delete Product")
        self.delete_product_button.clicked.connect(self.delete_product)
        layout.addWidget(self.delete_product_button)

        self.setLayout(layout)

    def add_product(self):
        product_name = self.product_name_input.text()
        if product_name:
            self.parentApp.products.append(product_name)
            self.product_name_input.clear()
            print(f"self.parentApp.products: {self.parentApp.products}")
            self.update_product_list()
            self.parentApp.update_inventory_tab_product_dropdown()

    def delete_product(self):
        selected_items = self.product_list.selectedItems()
        for item in selected_items:
            product_name = item.text()
            self.parentApp.products.remove(product_name)
        self.update_product_list()

    def update_product_list(self):
        self.product_list.clear()
        self.product_list.addItems(self.parentApp.products)
