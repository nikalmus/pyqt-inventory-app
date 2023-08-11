from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QListWidget

class ProductTab(QWidget):
    def __init__(self, products, update_product_list, add_product, delete_product):
        super().__init__()

        self.products = products
        self.update_product_list = update_product_list
        self.add_product = add_product
        self.delete_product = delete_product

        self.init_ui()

    def init_ui(self):
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

        self.setLayout(layout)
