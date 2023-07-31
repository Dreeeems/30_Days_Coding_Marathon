import tkinter as tk
from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageTk

class ProductScraperApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Product Search Results")

        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        self.search_button = tk.Button(self.root, text="Search", command=self.search_products)
        self.search_button.pack()

        self.selected_product_info = tk.StringVar()
        self.product_info_label = tk.Label(self.root, textvariable=self.selected_product_info)
        self.product_info_label.pack()

        self.image_label = tk.Label(self.root)
        self.image_label.pack()

    def scrape_product_data(self, url):
        page = requests.get(url)

        if page.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {page.status_code}")
            return None

        doc = BeautifulSoup(page.content, "html.parser")

        products = []
        product_elements = doc.find_all("li", class_="pdt-item")

        if not product_elements:
            print("No product elements found.")
            return None

        for product_element in product_elements:
            name = product_element.find("h3").text.strip()
            price = product_element.find("div", class_="price").text.strip()
            image_url = product_element.find("img")['src']
            products.append({"name": name, "price": price, "image_url": image_url})

        return products

    def search_products(self):
        item = "gpu"  
        url = f"https://www.ldlc.com/en/search/{item}"

        product_data = self.scrape_product_data(url)

        self.listbox.delete(0, tk.END)  # Clear previous results

        if product_data:
            for product in product_data:
                product_info = f"Product: {product['name']}, Price: {product['price']}"
                self.listbox.insert(tk.END, product_info)
        else:
            self.listbox.insert(tk.END, "No product data found.")

    def on_select(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_product = self.listbox.get(selected_index)
            self.selected_product_info.set(selected_product)

         
            product_data = self.scrape_product_data(f"https://www.ldlc.com/en/search/laptop")
            image_url = product_data[selected_index[0]]['image_url']

          
            image = Image.open(requests.get(image_url, stream=True).raw)
            image = image.resize((200, 200))  
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(image=photo)
            self.image_label.image = photo

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ProductScraperApp()
    app.run()
