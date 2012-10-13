Django Model Parser
===================

The parser that detects django models from the provided python script.
It's uses Python's AST (Abstract Syntax Trees) module.

Usage
=====

Example usage:

    from modelparser.parser import parse

    parse("""

    class Group(models.Model):
        name = models.CharField(max_length=255)

    class User(models.Model):
        first_name = models.CharField(max_length=255)
        last_name = models.CharField(max_length=255)
        is_active = models.BooleanField()
        groups = models.ManyToManyField(Group)

    """)

The result:

    {
        'Group': [{
            'type': 'string',
            'name': 'name'
        }],
        'User': [{
            'type': 'string',
            'name': 'first_name'
        }, {
            'type': 'string',
            'name': 'last_name'
        }, {
            'type': 'boolean',
            'name': 'is_active'
        }, {
            'type': 'many-to-many',
            'name': 'groups',
            'relationship': 'Group'
        }]
    }




