"""Tests for `realclasses` package."""

from realclasses import Attribute as attr
from realclasses import realclass


@realclass
class MyClassBase:
    my_list: list = attr(list, default=[])


@realclass
class MyClassDerived1(MyClassBase):
    my_int: int = attr(int, default=0)


@realclass
class MyClassDerived2(MyClassBase):
    my_int: int = attr(int, default=0)


def test_class_instance():
    obj1: MyClassDerived1 = MyClassDerived1()
    obj2: MyClassDerived2 = MyClassDerived2()

    obj1.my_list.append(1)
    obj2.my_list.append(2)

    assert obj1.my_list
    assert obj1.my_list == [1]
    assert obj1.my_list != obj2.my_list

    assert obj2.my_list == [2]

    MyClassDerived1.my_list.append(3)
    MyClassDerived2.my_list.append(4)

    assert MyClassDerived1.my_list == [3]
    assert MyClassDerived2.my_list == [4]

    assert MyClassBase.my_list == []
