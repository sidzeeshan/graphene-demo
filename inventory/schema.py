import graphene
from graphene_django import DjangoObjectType
from inventory.models import Family, Location, Product, Transaction


class FamilyType(DjangoObjectType):
    class Meta:
        model = Family


class LocationType(DjangoObjectType):
    class Meta:
        model = Location


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction


class Query(graphene.ObjectType):
    all_families = graphene.List(FamilyType)
    all_locations = graphene.List(LocationType)
    all_products = graphene.List(ProductType)
    all_transactions = graphene.List(TransactionType)

    def resolve_all_families(self, info, **kwargs):
        return Family.objects.all()

    def resolve_all_locations(self, info, **kwargs):
        return Location.objects.all()

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_all_transactions(self, info, **kwargs):
        return Transaction.objects.all()
