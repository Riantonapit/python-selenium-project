import subprocess

def test_run_demoQA_script():
    result = subprocess.run(["python", "demoQA.py"], capture_output=True, text=True)
    assert "Test berhasil dijalankan!" in result.stdout