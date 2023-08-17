import factory


class ContextFactory(factory.Factory):
    class Meta:
        model = dict

    example_key = factory.Sequence(lambda n: f"key{n}")
    example_value = factory.Sequence(lambda n: f"value{n}")
