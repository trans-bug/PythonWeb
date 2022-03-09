# Generated by Django 4.0.2 on 2022-03-06 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('logo', models.ImageField(upload_to='', verbose_name='Logo图片')),
                ('first_letter', models.CharField(max_length=1, verbose_name='品牌首字母')),
            ],
            options={
                'verbose_name': '品牌',
                'verbose_name_plural': '品牌',
                'db_table': 'tb_brand',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('sales', models.IntegerField(default=0, verbose_name='销量')),
                ('comments', models.IntegerField(default=0, verbose_name='评价数')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dj_store.brand', verbose_name='品牌')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'tb_goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=10, verbose_name='名称')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dj_store.goodscategory', verbose_name='父类别')),
            ],
            options={
                'verbose_name': '商品类别',
                'verbose_name_plural': '商品类别',
                'db_table': 'tb_goods_category',
            },
        ),
        migrations.CreateModel(
            name='GoodsSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=20, verbose_name='规格名称')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj_store.goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品规格',
                'verbose_name_plural': '商品规格',
                'db_table': 'tb_goods_specification',
            },
        ),
        migrations.CreateModel(
            name='SKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
                ('stock', models.IntegerField(default=0, verbose_name='库存')),
                ('sales', models.IntegerField(default=0, verbose_name='销量')),
                ('default_image_url', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='默认图片')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj_store.goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品SKU',
                'verbose_name_plural': '商品SKU',
                'db_table': 'tb_sku',
            },
        ),
        migrations.CreateModel(
            name='SpecificationOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('value', models.CharField(max_length=20, verbose_name='选项值')),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj_store.goodsspecification', verbose_name='规格')),
            ],
            options={
                'verbose_name': '规格选项',
                'verbose_name_plural': '规格选项',
                'db_table': 'tb_specification_option',
            },
        ),
        migrations.CreateModel(
            name='SKUImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('image', models.ImageField(upload_to='', verbose_name='图片')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj_store.sku', verbose_name='sku')),
            ],
            options={
                'verbose_name': 'SKU图片',
                'verbose_name_plural': 'SKU图片',
                'db_table': 'tb_sku_image',
            },
        ),
        migrations.CreateModel(
            name='GoodsChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('group_id', models.IntegerField(verbose_name='组号')),
                ('url', models.CharField(max_length=50, verbose_name='频道页面链接')),
                ('sequence', models.IntegerField(verbose_name='组内顺序')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj_store.goodscategory', verbose_name='顶级商品类别')),
            ],
            options={
                'verbose_name': '商品频道',
                'verbose_name_plural': '商品频道',
                'db_table': 'tb_goods_channel',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='category1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cat1_goods', to='dj_store.goodscategory', verbose_name='一级类别'),
        ),
        migrations.AddField(
            model_name='goods',
            name='category2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cat2_goods', to='dj_store.goodscategory', verbose_name='二级类别'),
        ),
        migrations.AddField(
            model_name='goods',
            name='category3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cat3_goods', to='dj_store.goodscategory', verbose_name='三级类别'),
        ),
    ]
