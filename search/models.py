from django.db import models
# Create your models here.
class Account(models.Model):
    username = models.CharField(("Tên đăng nhập"), max_length=50)
    password = models.CharField("Mật khẩu", max_length=50)
    fullname = models.CharField("Họ tên", max_length=100)
    email = models.EmailField(("Email"), max_length=254)
    def __str__(self):
        print(f"{self.username} {self.email}")
class Item(models.Model):
    title = models.CharField("Tiêu đề", max_length = 200)
    typeInfo = models.CharField("Loại tin",max_length = 50) # tin : tìm kiếm / thất lạc
    typeItem = models.CharField("Phân loại đồ", max_length = 50)
    adrLost = models.CharField("Địa điểm mất",max_length=200)
    image = models.CharField("Hình ảnh vật", max_length=50) # link file 
    content = models.CharField("Nội dung", max_length=500)
    fullname = models.CharField("Họ tên", max_length = 100)
    address = models.CharField("Địa chỉ", max_length = 200)
    phoneNum = models.CharField("Số điện thoại", max_length = 10)
    email = models.EmailField(("Email"), max_length=254)
    def __str__(self):
        print(f"{self.title}")
class Message(models.Model):
    fullname = models.CharField(("Họ tên"), max_length=100)
    content = models.CharField(("Nội dung"), max_length=50)
    time = models.CharField(("Thời gian"), max_length=50)
    status = models.CharField("Trạng thái tin nhắn",max_length=50) #Success/Fail
class menuItem(models.Model):
    nameItem = models.CharField("Tên kiểu đồ",max_length=50)
    amountLost = models.IntegerField(("Số lượng mất"))
    amountPick = models.IntegerField("Số lượng nhặt được")



