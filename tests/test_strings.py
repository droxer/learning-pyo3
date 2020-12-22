from learning_pyo3 import strings


def test_sum_as_string():
    assert strings.sum_as_string(100, 200) == "300"