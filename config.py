from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
database = os.environ['MYSQL_DATABASE']


if password:
    DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'
else:
    DATABASE_CONNECTION_URI = f'mysql://{user}@{host}/{database}'


for var in ['MYSQL_USER', 'MYSQL_HOST', 'MYSQL_DATABASE']:
    if not os.environ.get(var):
        raise ValueError(f"La variable {var} no está definida en el archivo .env")
