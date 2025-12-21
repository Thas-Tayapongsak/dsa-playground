import pytest
import os
import shutil
from pathlib import Path

@pytest.fixture
def run_app():
    import subprocess
    
    def _run(app_name, args=None, input_path=None):
        if args is None: args = []

        default_build_dir = Path(__file__).parent.parent / "build" / "bin"
        exe_dir = os.environ.get('EXECUTABLE_DIR', default_build_dir)
        app_path = Path(exe_dir) / f"{app_name}.exe"

        if not app_path.exists():
            pytest.fail(f"Executable not found: {app_path}")

        cmd = [str(app_path)] + args

        if input_path is None:
            return subprocess.run(cmd, capture_output=True, text=True)
        else:
            with open(input_path, 'r') as f:
                return subprocess.run(cmd, stdin=f, capture_output=True, text=True)
    
    return _run

@pytest.fixture
def temp_path():
    """
    Clear the `temp` directory of the temporary files
    """
    root_dir = Path(__file__).parent
    temp_dir = root_dir / "temp"

    if temp_dir.exists():
        shutil.rmtree(temp_dir)

    temp_dir.mkdir()

    return temp_dir
