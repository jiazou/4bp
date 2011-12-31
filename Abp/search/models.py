from django.db import models

# something a Deal can be applied upon. all products and services are by convention, named product.
class Product(models.Model):
    # name of the product;
    name = models.CharField(max_length = 500)
    # description of the product
    description = models.CharField(max_length = 1000)
    # unique Id for this product.
    unique_id = models.CharField(max_length = 1000)
    # unique Id type. This Id can be of any type, e.g., IBSN for books, etc. An enum.
    unique_id_type = models.IntegerField();
    # the category of this product.
    category = models.CharField(max_length = 100)
    # link to image
    imageLink = models.URLField(max_length = 100)
    # specs related to this product
    specs = models.TextField(max_length = 1000)

# a money-saving deal that can be applied to a Product.
class Deal(models.Model):
    # the date, time, and time zone of the starting date at which this deal becomes valid.
    start_valid_date = models.DateTimeField('starting valid date')
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
    # the source of the deal, such as Amazon.com. This field may be null, in case of a manufacture
    # coupon.
    deal_source = models.URLField(max_length = 100)
    # the image or text needed to redeem a deal on that page.
    deal_redeembable_text = models.CharField(max_length = 50)
    # this may not be needed, if we can parse QR/bar codes in advance and simply convert these date
    # to text fields.
    deal_redeemable_image = models.ImageField()

# a mapping from product to deals. A separate database table is needed because there is a
# many-to-many mapping between products and deals.
class productToDealMapping(models.Model):
    # The product id for this mapping.
    product_id = models.IntegerField()
    # The deal id for this mapping.
    deal_id = models.IntegerField()
    
class productPriceHistory(models.Model):
    # the product associated with the history
    product_id = models.ImageField()
    # the date at which this price became active.
    date = models.DateTimeField('date at which this active is active')
    # the _smallest_ amount at which the product was priced at the previously defined date.
    amount_local_currency_value = models.IntegerField()
    amount_currency = models.CharField(max_length = 4)
    amount_exchange_rate_to_usd = models.DecimalField(max_digit = 20, decimal_places = 6)
