"""Tests for `realclasses` package."""

from dataclasses import dataclass, field

import pytest


@dataclass
class MyClassBase:
    my_list: list = field(default_factory=list)


@dataclass
class MyClassDerived1(MyClassBase):
    my_int: int = 0


@dataclass
class MyClassDerived2(MyClassBase):
    my_int: int = 1


def test_class_instance():
    obj1: MyClassDerived1 = MyClassDerived1()
    obj2: MyClassDerived2 = MyClassDerived2()

    obj1.my_list.append(1)
    obj2.my_list.append(2)

    assert obj1.my_list
    assert obj1.my_list == [1]
    assert obj1.my_list != obj2.my_list

    assert obj2.my_list == [2]

    with pytest.raises(AttributeError):
        MyClassDerived1.my_list.append(3)
        assert MyClassDerived1.my_list == [3]

    with pytest.raises(AttributeError):
        MyClassDerived2.my_list.append(4)
        assert MyClassDerived2.my_list == [4]
