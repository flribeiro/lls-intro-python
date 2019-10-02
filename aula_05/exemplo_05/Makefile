# First of all
# alias m='make'

# Remover os caches que o PY gera
clean:
	find . -type d -name '__pycache__' -prune -exec rm -rf {} \;
	find . -name "*.pyc" -exec rm -rf {} \;

# Rodando em todos os pc's conectados na mesma rede
run:
	python manage.py runserver 0.0.0.0:8000

# Migração de banco de dados
te:
	python manage.py migrate
	# python manage.py <app_name>

tions:
	python manage.py makemigrations
	# python manage.py makemigrations <app_name>

# Remover os arquivos que o ORM nativo gera
off_tions:
	find . -type d -name 'migrations' -prune -exec rm -rf {} \;
	# cd /src/apps/<app_name> && rm -rf migrations

# Criando o super usuário
user:
	python manage.py createsuperuser

# Interagindo com o shell no django
shell:
	python manage.py shell

# Coletando os arquivos estáticos de todas apps para um único diretório
staticfiles:
	python manage.py collectstatic

# Remover registros da tabela
del:
	python manage.py sqlflush
	
# Exportando base de dados
dump:
	python manage.py dumpdata --format=json --indent=4 --database=default --all > db_dump.json
	
load:
	python manage.py loaddata db_dump.json  # database=production

comments_off:
	sed '/^[[:blank:]]*#/d;s/#.*//' **/*.py 
