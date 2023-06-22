from fastapi import FastAPI
from starlette.graphql import GraphQLApp
import graphene

app = FastAPI()

app.add_route("/graphql", GraphQLApp(schema=graphene.Schema()))