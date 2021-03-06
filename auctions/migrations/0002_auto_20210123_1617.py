# Generated by Django 3.1.1 on 2021-01-23 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='prices',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='bid',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_bided', to='auctions.item'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_commented', to='auctions.item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='items',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auctions.item'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_list_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_comment', to='auctions.comment')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
