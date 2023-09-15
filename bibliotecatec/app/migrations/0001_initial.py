# Generated by Django 4.2.5 on 2023-09-15 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_autor', models.CharField(max_length=100)),
                ('site_autor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cidade', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_editora', models.CharField(max_length=100)),
                ('site_editora', models.CharField(max_length=100)),
                ('cidade_editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_genero', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Leitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_leitor', models.CharField(max_length=100)),
                ('email_leitor', models.CharField(max_length=100)),
                ('cpf_leitor', models.CharField(max_length=11, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_livro', models.CharField(max_length=100)),
                ('preco', models.IntegerField()),
                ('data_plub', models.DateField()),
                ('status', models.BooleanField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.autor')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.editora')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genero')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateField()),
                ('data_devolucao', models.DateField()),
                ('leitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.leitor')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.livro')),
            ],
        ),
        migrations.AddField(
            model_name='autor',
            name='cidade_autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade'),
        ),
    ]
