# Generated by Django 2.0.3 on 2018-04-08 10:14

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import dummy.models.basic_array_models
import dummy.models.basic_embedded_models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArrayEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('authors', djongo.models.fields.ArrayModelField(model_container=dummy.models.basic_array_models.ArrayAuthor, model_form_class=dummy.models.basic_array_models.AuthorForm)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmbeddedEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', djongo.models.fields.EmbeddedModelField(model_container=dummy.models.basic_embedded_models.EmbeddedBlog, null=True)),
                ('headline', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('authors', models.ManyToManyField(to='dummy.Author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dummy.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('i', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('authors', djongo.models.fields.ArrayReferenceField(on_delete=django.db.models.deletion.CASCADE, to='dummy.ReferenceAuthor')),
            ],
        ),
    ]
