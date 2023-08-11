import sys
import uuid
from PyQt5.QtWidgets import QApplication
from product_tab import ProductTab
from inventory_tab import InventoryTab
from PyQt5.QtWidgets import QMainWindow, QTabWidget

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

        self.products_tab = ProductTab(self.products, self.update_product_list, self.add_product, self.delete_product)
        self.tab_widget.addTab(self.products_tab, "Products")

        self.inventory_tab = InventoryTab(self.products, 
                                          self.update_inventory_list, 
                                          self.add_inventory, 
                                          self.clear_quantity_input, 
                                          self.delete_selected_inventory)
        self.tab_widget.addTab(self.inventory_tab, "Inventory")

        self.setCentralWidget(self.tab_widget)

    def add_product(self):
        product_name = self.products_tab.product_name_input.text()
        if product_name:
            self.products.append(product_name)
            self.products_tab.product_name_input.clear()
            self.update_product_list()
            self.inventory_tab.product_dropdown.addItem(product_name)  # Line changed here

    def delete_product(self):
        selected_items = self.products_tab.product_list.selectedItems()
        for item in selected_items:
            product_name = item.text()
            self.products.remove(product_name)
            self.inventory_tab.product_dropdown.removeItem(self.inventory_tab.product_dropdown.findText(product_name))  
        self.update_product_list()

    def update_product_list(self):
        self.products_tab.product_list.clear()
        self.products_tab.product_list.addItems(self.products)

    def add_inventory(self):
        product = self.inventory_tab.product_dropdown.currentText()
        quantity = self.inventory_tab.quantity_input.text()

        if product and quantity:
            for _ in range(int(quantity)):
                serial_number = str(uuid.uuid4())
                self.inventory.append((product, serial_number))
            self.update_inventory_list()

    def clear_quantity_input(self):
        self.inventory_tab.quantity_input.clear()

    def update_inventory_list(self):
        self.inventory_tab.inventory_list.clear()
        for item in self.inventory:
            self.inventory_tab.inventory_list.addItem(f"Product: {item[0]} - Serial Number: {item[1]}")

    def delete_selected_inventory(self):
        selected_items = self.inventory_tab.inventory_list.selectedItems()
        for item in selected_items:
            inventory_item_text = item.text()
            serial_number = inventory_item_text.split(" - Serial Number: ")[1]
            for inv_item in self.inventory:
                if inv_item[1] == serial_number:
                    self.inventory.remove(inv_item)
                    break
        self.update_inventory_list()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec_())
