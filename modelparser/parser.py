import ast

from modelparser.visitors import ModelVisitor

def load(file):
    return loads(file.read())

def loads(script):
    node = ast.parse(script)
    visitor = ModelVisitor()
    visitor.visit(node)
    return visitor.models
