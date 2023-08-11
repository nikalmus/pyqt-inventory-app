import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from product_tab import ProductTab
from inventory_tab import InventoryTab

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

        self.products_tab = ProductTab(self)  # Pass the main app instance to ProductTab
        self.tab_widget.addTab(self.products_tab, "Products")

        self.inventory_tab = InventoryTab(self)  # Pass the main app instance to InventoryTab
        self.tab_widget.addTab(self.inventory_tab, "Inventory")

        self.setCentralWidget(self.tab_widget)

    def update_inventory_tab_product_dropdown(self):
        self.inventory_tab.populate_product_dropdown()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec_())