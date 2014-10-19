import colander


class SearchSchema(colander.MappingSchema):
    country = colander.SchemaNode(colander.String(), missing=colander.drop)
    city = colander.SchemaNode(colander.String(), missing=colander.drop)
    distance = colander.SchemaNode(
        colander.Integer(), validator=colander.Range(min=1),
        missing=colander.drop)
    distance_unit = colander.SchemaNode(
        colander.String(), validator=colander.OneOf(['mi', 'km']),
        missing=colander.drop)


def search_at_least_one_validator(form, value):
    if not any([value.get('country'), value.get('city')]):
        raise colander.Invalid(form, 'Country and City can\'t be both empty')

