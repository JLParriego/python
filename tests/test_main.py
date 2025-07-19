from src.main import saludar

def test_saludo_basico(capsys):
    saludar("Juan", 25)
    captured = capsys.readouterr()
    assert "Juan" in captured.out and "25" in captured.out
