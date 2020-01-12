from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moves', models.CharField(max_length=40)),
                ('cpu_code', models.CharField(max_length=100)),
                ('cpu_first_player', models.BooleanField()),
                ('cpu2_code', models.CharField(max_length=100)),
            ],
        ),
    ]
