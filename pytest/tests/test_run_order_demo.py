# http://pytest.ordering.readthedocs.io/en/develop

import pytest

@pytest.mark.run(order=2)
def test_order_order_methodS():
    print("MethodS")

@pytest.mark.run(order=3)
def test_order_order_methodA():
    print("MethodA")
@pytest.mark.run(order=6)
def test_order_order_methodK():
    print("MethodK")

@pytest.mark.run(order=4)
def test_order_order_methodD():
    print("MethodD")
@pytest.mark.run(order=5)
def test_order_order_methodJ():
    print("MethodJ")
@pytest.mark.run(order=1)
def test_order_order_methodKS():
    print("MethodKS")

