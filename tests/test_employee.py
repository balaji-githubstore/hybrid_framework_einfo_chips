import pytest


class TestAddEmployee:

    @pytest.mark.smoke
    def test_add_valid_employee(self):
        print("add valid employee")


class TestEditEmployee:
    def test_edit_employee1(self):
        print("edit employee")

    @pytest.mark.smoke
    @pytest.mark.bala
    def test_edit_employee2(self):
        print("edit employee")
