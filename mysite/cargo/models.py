from django.db import models
class Car(models.Model):
    model_name = models.CharField(max_length=100)
    release_year = models.IntegerField()
    body_style = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    mileage = models.IntegerField()
    seating_capacity = models.IntegerField()
    cargo_capacity = models.IntegerField()
    car_dimension = models.CharField(max_length=100)
    tyre_strength = models.CharField(max_length=100)  # Assuming this field was meant to be "tyre_strength"
    color = models.CharField(max_length=150)
    price = models.IntegerField()
    quantity=models.IntegerField()

    def __str__(self):
        return self.model_name
    
class Supplier(models.Model):
    #suppid
    supp_name=models.CharField(max_length=100)
    supp_email=models.CharField(max_length=100)
    supp_address=models.CharField(max_length=100)
    supp_phoneno=models.CharField(max_length=100)

    
class Profit(models.Model):
    #modelno(fk)
    model_name=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    profit=models.CharField(max_length=100)
    


class CustForm(models.Model):
    f_name=models.CharField(max_length=100)
    l_name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    NIC=models.IntegerField()


class Deal(models.Model):
    car_id = models.IntegerField(blank=True, null=True)
    supplier_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"deal of Car {self.car_id} to supplier {self.supp_id}"


class sales(models.Model):
 
    car_id = models.IntegerField()
    supplier_id = models.IntegerField()
    cust_id=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return f"Sale of Car {self.car_id} to Customer {self.cust_id}"


# class sales(models.Model):
#     car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
#     supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
#     cust_id = models.ForeignKey(CustForm, on_delete=models.CASCADE)
#     price = models.IntegerField()

#     def __str__(self):
#         return f"Sale of Car {self.car_id} to Customer {self.cust_id}"

# Create your models here.



class Record(models.Model):
    NIC=models.CharField(max_length=13)
    f_name=models.CharField(max_length=10)
    l_name=models.CharField(max_length=10)
    NewCustomer_name=models.CharField(max_length=20)
    NewCustomer_NIC=models.CharField(max_length=13)
    model_name=models.CharField(max_length=10)
    release_year=models.IntegerField()
    cust_id=models.ForeignKey(CustForm, on_delete=models.CASCADE)



