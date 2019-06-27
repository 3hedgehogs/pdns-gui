from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Domain",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("master", models.CharField(blank=True, max_length=128, null=True)),
                ("last_check", models.IntegerField(blank=True, null=True)),
                ("domain_type", models.CharField(db_column="type", max_length=6)),
                ("notified_serial", models.PositiveIntegerField(blank=True, null=True)),
                ("account", models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={"db_table": "domains"},
        ),
        migrations.CreateModel(
            name="TsigKey",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("algorithm", models.CharField(blank=True, max_length=50, null=True)),
                ("secret", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "tsigkeys",
                "unique_together": {("name", "algorithm")},
            },
        ),
        migrations.CreateModel(
            name="Supermaster",
            fields=[
                (
                    "ip",
                    models.CharField(max_length=64, primary_key=True, serialize=False),
                ),
                ("nameserver", models.CharField(max_length=255)),
                ("account", models.CharField(max_length=40)),
            ],
            options={
                "db_table": "supermasters",
                "unique_together": {("ip", "nameserver")},
            },
        ),
        migrations.CreateModel(
            name="Record",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("type", models.CharField(blank=True, max_length=10, null=True)),
                ("content", models.TextField(blank=True, null=True)),
                ("ttl", models.IntegerField(blank=True, null=True)),
                ("prio", models.IntegerField(blank=True, null=True)),
                ("change_date", models.IntegerField(blank=True, null=True)),
                ("disabled", models.IntegerField(blank=True, null=True)),
                ("ordername", models.CharField(blank=True, max_length=255, null=True)),
                ("auth", models.IntegerField(blank=True, null=True)),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                (
                    "domain",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="pdns.Domain",
                    ),
                ),
            ],
            options={"db_table": "records"},
        ),
        migrations.CreateModel(
            name="DomainMetadata",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("kind", models.CharField(blank=True, max_length=32, null=True)),
                ("content", models.TextField(blank=True, null=True)),
                (
                    "domain",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="pdns.Domain"
                    ),
                ),
            ],
            options={"db_table": "domainmetadata"},
        ),
        migrations.CreateModel(
            name="CryptoKey",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("flags", models.IntegerField()),
                ("active", models.IntegerField(blank=True, null=True)),
                ("content", models.TextField(blank=True, null=True)),
                (
                    "domain",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="pdns.Domain"
                    ),
                ),
            ],
            options={"db_table": "cryptokeys"},
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=10)),
                ("modified_at", models.IntegerField()),
                ("account", models.CharField(blank=True, max_length=40, null=True)),
                ("comment", models.TextField()),
                (
                    "domain",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="pdns.Domain"
                    ),
                ),
            ],
            options={"db_table": "comments"},
        ),
    ]
