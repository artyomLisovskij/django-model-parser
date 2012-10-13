import ast
from _ast import Call, Attribute, Name

from constants import *


class FieldVisitor(ast.NodeVisitor):
    """
    A visitor that inspects model fields.
    """
    def __init__(self):
        self.fields = []

    def add_field(self, field_name, field_type, relationship):
        field = {
            "name": field_name,
            "type": field_type
        }
        if relationship is not None:
            field["relationship"] = relationship
        self.fields.append(field)

    def visit_Assign(self, node):
        field_name = None
        field_type = None
        relationship = None

        if not isinstance(node.value, Call):
            return

        field_name = node.targets[0].id

        if isinstance(node.value.func, Attribute):
            field_type = FIELD_TYPE_MAP.get(node.value.func.attr,
                DEFAULT_FIELD_TYPE)

            if field_type in [MANY_TO_MANY_FIELD, FOREIGN_KEY_FIELD]:
                relationship = node.value.args[0].id

        if field_type is not None:
            self.add_field(field_name, field_type, relationship=relationship)



class ModelVisitor(ast.NodeVisitor):
    """
    A visitor that detects django models.
    """
    def __init__(self):
        self.models = {}

    def visit_ClassDef(self, node):
        base_class = None
        for base in node.bases:
            if isinstance(base, Attribute):
                base_class = base.attr
            if isinstance(base, Name):
                base_class = base.id

        if base_class == MODEL_BASE_CLASS:
            visitor = FieldVisitor()
            visitor.visit(node)
            self.models[node.name] = visitor.fields