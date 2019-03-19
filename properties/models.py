from django.db import models

PROPERTY_CHOICES = (('SINGLE', 'Single Property'), ('CONDO', 'Condo/Townhouse'), ('INCOMEPROP', 'Income Property'), ('OTHER', 'Other'))

class Status(models.Model):
    #status will be active, pending, and past
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Property(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='properties/', default=None)
    description = models.TextField(max_length=4000)
    price = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    type = models.CharField(max_length=100)
    year_built = models.CharField('year built', max_length=100)
    sq_ft = models.IntegerField('square footage')
    beds = models.IntegerField('beds')
    full_baths = models.IntegerField('full baths')
    half_baths = models.IntegerField('half baths')
    mls_link = models.CharField('MLS Link', max_length=100, default=None, null=True)

    def src(self):
        #back = 4 would give us an output of /static/properties/uploads/image.jpg
        path = '/'.join(self.image.path.split('\\')[-1])
        img = self.image.path.split('\\')[-1]
        return path

    def bathrooms(self):
        return self.full_baths + 1/2*self.half_baths

    def formatted_price(self):
        value = self.price
        price = f"{value:,d}"
        return price

    def __str__(self):
        return self.address

class NewLead(models.Model):
    name = models.CharField('Your name', max_length=100, default=None)
    sq_ft = models.CharField('How much square footage?',max_length=100)
    move_in_date = models.CharField('What was the date of move in?',max_length=100)
    beds = models.CharField('How many beds?',max_length=100)
    baths = models.CharField('How many baths?',max_length=100)
    email = models.EmailField("What's your email?",max_length=100)
    phone = models.CharField("What's your phone number?",max_length=100)
    property_type = models.CharField("What's the property type?",max_length=20,choices=PROPERTY_CHOICES)
    address = models.CharField("Address",max_length=100)
    move_in_date = models.CharField("What's the approximate move in date?",max_length=100)
    preffered_method_of_contact = models.CharField("What's your preffered method of contact?",max_length=100)
    description = models.TextField('Description of the property', max_length=1000)

    def __str__(self):
        return self.name
