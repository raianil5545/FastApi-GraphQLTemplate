# FastApi-GraphQLTemplate
### Initilizate migration using alembic
alembic init alembic

### Create the migration file
docker-compose run app alembic revision --autogenerate -m "migration description"

### Apply migration
docker-compose run app alembic upgrade head

### Packages used 
fastapi uvicorn sqlalchemy graphene graphene-sqlalchemy alembic psycopg2 black python-dotenv
