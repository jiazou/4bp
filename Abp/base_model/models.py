from django.db import models
import model_fields

# our database is designed to allow the following operations:
# 1. save a deal specific to a product/source
# 2. find deals specific to a product/source
# 3. given a product, find all deals associated with that product
# 4. given a source, find all deals associated with that source
# 5. given a product/source, find the price history associated with that product/source
# 6. given a product, find the price history associated with that product

# a money-saving deal that can be applied to a Product.
class Deal(models.Model):
    # the date, time, and time zone of the starting date at which this deal becomes valid.
    start_valid_date = models.DateTimeField('start valid date')
    # the date, time, and time zone of the ending date at which this deal becomes valid.
    end_valid_date = models.DateTimeField('end valid date')
    # the title description of this deal.
    title = models.CharField(max_length = 1000)
#   This deal should be able to capture the following attributes:
#        it should tell us how much we are saving, thus it needs:
#            1. a base price we are saving from. This may be null, e.g., manufacture coupon. In
#            2. the amount we are saving, either a percentage or a value amount.
#        a deal or a coupon can take many forms. To reduce our problem space, currently we are only
#        focusing on deals with the following format:
#            1. this deal must have a web url link.
#            2. a coupon, either in the form of bar code, or a coupon code:
#                after going to the web url, the deal can either be executed directly, or a coupon
#                code can be applied to execute the deal.
    # the image or text needed to redeem a deal on that page.
    coupon_code = models.CharField(max_length = 50)
    # this may not be needed, if we can parse QR/bar codes in advance and simply convert these date
    # to text fields.
    coupon_image = models.ImageField()

# something a Deal can be applied upon. all products and services are by convention, named product.
class Product(models.Model):
    # many to many association with a deal
    deal = models.ManyToManyField(Deal);

    # Product specific details:
    # name of the product;
    name = models.CharField(max_length = 500)
    # description of the product
    description = models.CharField(max_length = 1000)
    # unique Id for this product.
    unique_id = models.CharField(max_length = 1000)
    # unique Id type. This Id can be of any type, e.g., IBSN for books, etc. An enum.
    unique_id_type = models.IntegerField()
    # the category of this product.
    category = models.CharField(max_length = 100)
    # link to image
    image_link = models.URLField(max_length = 500)
    # specs related to this product
    specs = models.TextField(max_length = 1000)
    
class Source(models.Model):
    # many to many association with a deal
    deal = models.ManyToManyField(Deal);

    # source URL, we limit our selves to online sources/deals at this point.
    source_url = models.URLField(max_length = 500)
    # description of this source website.
    description = models.CharField(max_length = 500)
    
class ProductPriceHistory(models.Model):
    # the product for which we are storing the history.
    product_id = models.IntegerField()
    # the source for which we are storing the history.
    source_id = models.IntegerField()
    # a tuple of time and price for a particular product from a particular source.
    time_price = model_fields.TimePriceField()