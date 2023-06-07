"""
RealClasses isolates the attribute of Base and Derived classes.

RealClasses is a collection of classes and functions that help
the creation of new classes with a behavior expected regarding
to class and instance variables also between base and derived
classes.
"""
from copy import deepcopy
from typing import Any, Type

__slots__ = ['Attribute', 'RealClasses', 'real_class']


def apply_deep_copy_annotation(cls, instance):
    """Copy fields according to the type annotations."""
    if not hasattr(cls, '__annotations__'):
        return

    for var_name, _ in cls.__annotations__.items():
        if not isinstance(getattr(instance, var_name), Attribute):
            val = deepcopy(getattr(instance, var_name))
            setattr(instance, var_name, val)
            return
        val = deepcopy(getattr(instance, var_name))
        setattr(instance, var_name, val.default)


# volture: skip
def realclass(cls):
    """Decorate a regular class and convert it into a RealClass."""
    for class_base in cls.__bases__:
        apply_deep_copy_annotation(class_base, cls)

    apply_deep_copy_annotation(cls, cls)
    cls.__new__ = realclass__new__(cls)
    return cls


class Attribute:
    """Attribute is a class used to create fields for RealClass."""

    type_obj: Type = object
    default: Any = None

    def __init__(self, type_obj: Type, default: Any = None):
        """Initialize Attribute instances."""
        self.type_obj = type_obj
        self.default = default


def realclass__new__(klass):
    """
    Wrap-up the class method `__new__`.

    It copies all the fields marked with type annotation.
    """
    klass__new__ = klass.__new__

    def _realclass__new__(cls, *args, **kwargs):
        instance = klass__new__(cls, *args, **kwargs)

        for class_base in cls.__bases__:
            apply_deep_copy_annotation(class_base, instance)

        apply_deep_copy_annotation(cls, instance)

        return instance

    return _realclass__new__
