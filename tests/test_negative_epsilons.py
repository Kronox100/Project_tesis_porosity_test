import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
import Soyarslan_no_cubico as snc


def test_generates_files_with_negative_epsilons(tmp_path, monkeypatch):
    content = (
        "ITEM: TIMESTEP\n0\nITEM: NUMBER OF ATOMS\n1\n"\
        "ITEM: BOX BOUNDS ff ff ff\n0 1\n0 1\n0 1\n"\
        "ITEM: ATOMS id type x y z\n1 1 0 0 0\n"
    )
    dump = tmp_path / "in.dump"
    dump.write_text(content)
    monkeypatch.chdir(tmp_path)
    result = snc.funcion_app(
        str(dump), -0.1, -0.2, "<", "<", 1, 1,
        "out1.dump", "out2.dump", "vars1", "vars2",
        1, 1, 1, 1, 1, 1,
    )
    assert result[0] == "Complete"
    for folder, name in [
        ("process_files", "file1.dump"),
        ("process_files", "file2.dump"),
        ("process_files", "F_prime_result.dump"),
        ("results", "out1.dump"),
        ("results", "out2.dump"),
        ("results", "F_prime_result.dump"),
    ]:
        assert (tmp_path / folder / name).exists()

