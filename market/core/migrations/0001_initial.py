# Generated by Django 2.2.15 on 2020-08-10 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=15)),
                ('content', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('like_count', models.IntegerField(default=0)),
                ('dislike_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.FloatField()),
                ('discount_amount', models.FloatField()),
                ('status', models.IntegerField(choices=[(1, 'processing'), (2, 'packing'), (3, 'delivered'), (4, 'received')], default=1)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=50)),
                ('national_ID', models.CharField(max_length=10)),
                ('user_info', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('cover_image', models.ImageField(null=True, upload_to='product/cover_image')),
                ('price', models.FloatField()),
                ('available', models.BooleanField()),
                ('inventory_count', models.IntegerField()),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='QA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questinon', models.CharField(max_length=15)),
                ('answer', models.CharField(max_length=100, null=True)),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product')),
            ],
        ),
        migrations.CreateModel(
            name='TicketThread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_content', models.TextField()),
                ('question_content', models.TextField()),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('ticked_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.QA')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Shipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_date', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Orders')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit_amount', models.FloatField()),
                ('rank', models.IntegerField()),
                ('seller_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Person')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Seller')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product')),
                ('description', models.TextField(default='')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=20)),
                ('feature_value', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('status', models.IntegerField(choices=[(1, 'paid'), (2, 'unpaid')])),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Orders')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Seller'),
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Orders')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_code', models.CharField(max_length=10)),
                ('amount', models.FloatField()),
                ('init_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('until_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='person_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Person'),
        ),
        migrations.CreateModel(
            name='CommentDisadvantages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disadvantage', models.CharField(max_length=50)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='CommentAdvantages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advantage', models.CharField(max_length=50)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='customer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Customer'),
        ),
        migrations.AddField(
            model_name='comment',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product'),
        ),
        migrations.AddField(
            model_name='comment',
            name='seller_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Seller'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product')),
            ],
        ),
    ]
