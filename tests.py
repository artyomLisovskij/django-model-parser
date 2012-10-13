import unittest
import operator

from modelparser import loads

EMPTY_MODELS = """
class Foo(models.Model):
    pass

class Bar(Model):
    pass
"""

NON_MODEL_CLASS = """
class FooBar(object):
    pass
"""

MODEL_WITH_FIELDS = """
class Foo(models.Model):
    foo = models.CharField(max_length=255)
    bar = models.CharField(max_length=255)
"""


class ModelParserTestCase(unittest.TestCase):

    def test_models(self):
        models = loads(EMPTY_MODELS)
        self.assertIn("Foo", models)
        self.assertIn("Bar", models)

    def test_non_model_classes(self):
        models = loads(NON_MODEL_CLASS)
        self.assertNotIn("FooBar", models)

    def test_model_fields(self):
        model = loads(MODEL_WITH_FIELDS).get("Foo")
        self.assertEqual(len(model), 2)
        field_names = map(operator.itemgetter("name"), model)
        self.assertIn("foo", field_names)
        self.assertIn("bar", field_names)

if __name__ == '__main__':
    unittest.main()
