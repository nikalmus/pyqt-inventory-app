import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QListWidget

class InventoryApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.items = []

        self.setWindowTitle("Inventory Tracking App")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.name_label = QLabel("Item Name:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.quantity_label = QLabel("Quantity:")
        self.quantity_input = QLineEdit()
        layout.addWidget(self.quantity_label)
        layout.addWidget(self.quantity_input)

        self.add_button = QPushButton("Add Item")
        self.add_button.clicked.connect(self.add_item)
        layout.addWidget(self.add_button)

        self.item_list = QListWidget()
        layout.addWidget(self.item_list)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_item(self):
        name = self.name_input.text()
        quantity = self.quantity_input.text()

        if name and quantity:
            self.items.append((name, quantity))
            self.update_item_list()
            self.name_input.clear()
            self.quantity_input.clear()

    def update_item_list(self):
        self.item_list.clear()
        for item in self.items:
            self.item_list.addItem(f"{item[0]} - {item[1]}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec_())