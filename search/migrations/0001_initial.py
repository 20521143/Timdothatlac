# Generated by Django 4.1.1 on 2022-10-12 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Tên đăng nhập')),
                ('password', models.CharField(max_length=50, verbose_name='Mật khẩu')),
                ('fullname', models.CharField(max_length=100, verbose_name='Họ tên')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Tiêu đề')),
                ('typeInfo', models.CharField(max_length=50, verbose_name='Loại tin')),
                ('typeItem', models.CharField(max_length=50, verbose_name='Phân loại đồ')),
                ('adrLost', models.CharField(max_length=200, verbose_name='Địa điểm mất')),
                ('image', models.CharField(max_length=50, verbose_name='Hình ảnh vật')),
                ('content', models.CharField(max_length=500, verbose_name='Nội dung')),
                ('fullname', models.CharField(max_length=100, verbose_name='Họ tên')),
                ('address', models.CharField(max_length=200, verbose_name='Địa chỉ')),
                ('phoneNum', models.CharField(max_length=10, verbose_name='Số điện thoại')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='menuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameItem', models.CharField(max_length=50, verbose_name='Tên kiểu đồ')),
                ('amountLost', models.IntegerField(verbose_name='Số lượng mất')),
                ('amountPick', models.IntegerField(verbose_name='Số lượng nhặt được')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, verbose_name='Họ tên')),
                ('content', models.CharField(max_length=50, verbose_name='Nội dung')),
                ('time', models.CharField(max_length=50, verbose_name='Thời gian')),
                ('status', models.CharField(max_length=50, verbose_name='Trạng thái tin nhắn')),
            ],
        ),
    ]
