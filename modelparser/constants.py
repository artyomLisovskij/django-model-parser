MODEL_BASE_CLASS = "Model"

MANY_TO_MANY_FIELD = "many-to-many"
FOREIGN_KEY_FIELD = "foreign-key"

FIELD_TYPE_MAP = {
    "CharField": "string",
    "EmailField": "string",
    "BooleanField": "boolean",
    "DateTimeField": "datetime",
    "DateField": "date",
    "TimeField": "time",
    "FileField": "string",
    "ForeignKey": FOREIGN_KEY_FIELD,
    "ManyToManyField": MANY_TO_MANY_FIELD,
    "OneToOneField": FOREIGN_KEY_FIELD
}

DEFAULT_FIELD_TYPE = "string"