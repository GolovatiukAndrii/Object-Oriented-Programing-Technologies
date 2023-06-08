from PIL import Image


class ProductImage:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        if self.image is None:
            self.image = Image.open(self.image_path)
            print(f"Image loaded: {self.image_path}")

    def display_image(self):
        if self.image is None:
            self.load_image()
        self.image.show()


class LazyLoadingProxy:
    def __init__(self, subject):
        self.subject = subject

    def display_image(self):
        self.subject.load_image()
        self.subject.display_image()


# Створення об'єкту проксі
image_proxy = LazyLoadingProxy(ProductImage("product1.jpg"))

# При виклику методу display_image() проксі буде завантажувати зображення і відображати його
image_proxy.display_image()

# Якщо викликати метод display_image() знову, зображення буде відображено без повторного завантаження
image_proxy.display_image()
