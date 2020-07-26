from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    gender = models.CharField(max_length=60)
    date_of_birth = models.DateField()

    email = models.EmailField()
    password = models.CharField(max_length=60)

    def get_pass(self):
        return self.password


class Item(models.Model):
    CHOICES = [              # men/women uniqe product
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('General', 'General'),
    ]
    ProductCategory = [
        ('Fruits', 'Fruits'), #
        ('Meats on fire', 'Meat on fire'), #
        ('Cheese', 'Cheese'), #
        ('Salads', 'Salads'), #
        ('Eggs', 'Eggs'), #
        ('Vegetables', 'Vegetables'), #
        ('Fish', 'Fish'), #
        ('Milk', 'Milk'), #
        ('DriedFruit', 'DriedFruit'), #
        ('Nuts', 'Nuts'), #
        ('Organic', 'Organic'), #
        ('Milk Delicacies & Yogurt', 'Milk Delicacies & Yogurt'), #
        ('Creamy Margarine Butter', 'Creamy Margarine Butter'), #
        ('Frozen meat', 'Frozen meat'), #
        ('Hot dogs and Sausages', 'Hot dogs and Sausages'), #
        ('Frozen chicken', 'Frozen chicken'), #
        ('Fresh chicken', 'Fresh chicken'), #
        ('Fresh meat', 'Fresh meat'),  #
        ('Free and reduced in sugar', 'Free and reduced in sugar'), #
        ('Soy and Lactose free', 'Soy and Lactose free'), #
        ('Gluten free', 'Gluten free'), #
        ('Ice cream and Popsicle', 'Ice cream and Popsicle'), #
        ('Fast food', 'Fast food'), #
        ('Pizzas, Pastries and Dough', 'Pizzas, Pastries and Dough'), #
        ('Vegetarian-ready food', 'Vegetarian-ready food'), #
        ('Frozen vegetables and Fries', 'Frozen vegetables and Fries'), #
        ('Canning', 'Canning'), #
        ('Sauces', 'Sauces'), #
        ('Soups and Stews', 'Soups and Stews'), #
        ('Oil, Vinegar and Lemon juice', 'Oil, Vinegar and Lemon juice'), #
        ('Honey, Jam and Spreads', 'Honey, Jam and Spreads'), #
        ('Spices', 'Spices'), #
        ('Baking products', 'Baking products'), #
        ('Asian cuisine', 'Asian cuisine'), #
        ('Flour and Breadcrumbs', 'Flour and Breadcrumbs'), #
        ('Pasta, Flakes, Couscous', 'Pasta, Flakes, Couscous'), #
        ('Cereals', 'Cereals'), #
        ('Rice and Legumes', 'Rice and Legumes'), #
        ('Sweets', 'Sweets'), #
        ('Salty snacks', 'Salty snacks'), #
        ('Waffles and Biscuits', 'Waffles and Biscuits'), #
        ('Cakes and Cookies', 'Cakes and Cookies'), #
        ('Candy and Gum', 'Candy and Gum'), #
        ('Sweet snacks', 'Sweet snacks'), #
        ('Soft drinks', 'Soft drinks'), #
        ('Hot beverages', 'Hot beverages'), #
        ('Wines', 'Wines'), #
        ('Alcohol and Energy', 'Alcohol and Energy'), #
        ('Concentrations', 'Concentrations'), #
        ('Paper products and Disposable', 'Paper products and Disposable'), #
        ('Covers, Bags and Molds', 'Covers, Bags and Molds'), #
        ('One-time', 'One-time'), #
        ('Picnic', 'Picnic'), #
        ('Candles and Matches', 'Candles and Matches'), #
        ('Housewares', 'Housewares'), #
        ('Home cleaning products', 'Home cleaning products'), #
        ('Dish soaps', 'Dish soaps'), #
        ('Laundry products', 'Laundry products'), #
        ('Cleaning accessories', 'Cleaning accessories'), #
        ('Insecticides and Aerosols', 'Insecticides and Aerosols'), #
        ('Animals products', 'Animals products'), #
        ('Hygiene products', 'Hygiene products'), #
        ('Pharm products', 'Pharm products'), #
        ('Diapers and Wipes', 'Diapers and Wipes'), #
        ('Babies food', 'Babies food'), #
        ('Baby care and Baby accessories', 'Baby care and Baby accessories'), #
        ('Soaps', 'Soaps'), #
        ('Shampoo and Conditioner', 'Shampoo and Conditioner'), #
        ('Deodorant', 'Deodorant'), #
        ('Shaving and Hair removal', 'Shaving and Hair removal'), #
        ('Oral hygiene', 'Oral hygiene'), #
        ('Bread, Pita, Bun', 'Bread, Pita, Bun'), #
        ('Salty pastry', 'Salty pastry'), #
    ]
    Item_Code = models.CharField(max_length=60)
    Item_Name = models.CharField(max_length=60)
    Manufacturer_Name = models.CharField(max_length=60)
    Manufacturer_Item_Description = models.CharField(max_length=60)
    Quantity = models.CharField(max_length=60)
    Unit_Qty = models.CharField(max_length=60)
    Item_Price = models.FloatField()                            # we actually don't need that line
    Audience = models.CharField(max_length=60, choices=CHOICES)
    Image = models.CharField(max_length=600)
    Category = models.CharField(max_length=60, choices=ProductCategory)

    def __str__(self):
        return self.Item_Name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(Item)
    #bool


class CartLine(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


class SubStores(models.Model):
    chain_id = models.CharField(max_length=60)
    sub_chain_id = models.CharField(max_length=60)
    store_id = models.CharField(max_length=60)
    store_name = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=60, null=True)


class Stores(models.Model):
    chain_id = models.CharField(max_length=60)
    name = models.CharField(max_length=60)



