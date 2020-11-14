from convert_units.app import run_script
import io

def test_unit_convert(monkeypatch):
    test_input = "5 m in cm"
    monkeypatch.setattr('sys.stdin', io.StringIO(test_input))
    model_answer = "500.0cm"
    assert run_script(True) == model_answer
    
