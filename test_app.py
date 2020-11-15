from convert_units.app import run_script, unit_convert
import io
import pytest
from _pytest.outcomes import Failed

def test_unit_convert(monkeypatch):
    test_input = "5 m in cm"
    monkeypatch.setattr('sys.stdin', io.StringIO(test_input))
    model_answer = "500.0cm"
    assert run_script(True) == model_answer
    
# def test_value_error(monkeypatch):
#     string_input = '5m in cm'
#     with pytest.raises(ValueError) as e:
#         monkeypatch.setattr('sys.stdin', io.StringIO(string_input))
#     assert str(e.value) == "ValueError: invalid literal for int() with base 10: '5m'"
