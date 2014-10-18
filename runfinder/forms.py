import colander


class SearchSchema(colander.MappingSchema):
    country = colander.SchemaNode(colander.String())
    city = colander.SchemaNode(colander.String())
    distance = colander.SchemaNode(
        colander.Integer(), validator=colander.Range(min=1))
    distance_unit = colander.SchemaNode(
        colander.String(), validator=colander.OneOf(['mi', 'km']))
