import graphene
import links.schema
import inventory.schema


class Query(links.schema.Query, inventory.schema.Query, graphene.ObjectType):
    pass


class Mutation(links.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
