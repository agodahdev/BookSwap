from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # Add any dependencies here if needed
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=255)),
                # Add other fields here
            ],
        ),
    ]
