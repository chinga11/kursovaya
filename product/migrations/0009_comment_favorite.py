from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0008_alter_product_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.TextField(max_length=1000)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("product", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="comments", to="product.product")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="product_comments", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["created_at"]},
        ),
        migrations.CreateModel(
            name="Favorite",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("product", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="favorited_by", to="product.product")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="favorites", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddConstraint(
            model_name="favorite",
            constraint=models.UniqueConstraint(fields=("user", "product"), name="unique_user_favorite_product"),
        ),
    ]
