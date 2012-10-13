import ast

from modelparser.visitors import ModelVisitor

def parse(script):
    node = ast.parse(script)
    visitor = ModelVisitor()
    visitor.visit(node)
    return visitor.models
