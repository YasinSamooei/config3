# Generated by Django 5.0.2 on 2024-03-04 02:11

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={
                "ordering": ["-published"],
                "verbose_name": "مقاله",
                "verbose_name_plural": "مقاله ها",
            },
        ),
        migrations.AddField(
            model_name="article",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="articles",
                to=settings.AUTH_USER_MODEL,
                verbose_name="نویسنده",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="descriptions",
            field=models.TextField(blank=True, null=True, verbose_name="محتوا"),
        ),
        migrations.AlterField(
            model_name="article",
            name="published",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="زمان انتشار"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(
                max_length=100, unique=True, verbose_name="آدرس مقاله"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="status",
            field=models.CharField(
                choices=[("d", "Draft"), ("p", "Published")],
                max_length=1,
                verbose_name="وضعیت",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="thumbnail",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/", verbose_name="تصویر مقاله"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=200, verbose_name="عنوان مقاله"),
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=200, verbose_name="عنوان دسته بندی"),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=100, unique=True, verbose_name="آدرس دسته بندی"
                    ),
                ),
                (
                    "status",
                    models.BooleanField(
                        default=True, verbose_name="آیا نمایش داده شود؟"
                    ),
                ),
                ("position", models.IntegerField(default=0, verbose_name="پوزیشن")),
                (
                    "parents",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="children",
                        to="blog.category",
                        verbose_name="زیر دست",
                    ),
                ),
            ],
            options={
                "verbose_name": "دسته بندی",
                "verbose_name_plural": "دسته بندی ها",
                "ordering": ["parents__id", "position"],
            },
        ),
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.ManyToManyField(
                related_name="articles", to="blog.category", verbose_name="دسته بندی"
            ),
        ),
    ]
