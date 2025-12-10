import pytest
import os
import sys
from pathlib import Path

@pytest.fixture
def run_app():
    import subprocess
    
    def _run(app_name, args=None):
        if args is None: args = []

        exe_dir = os.environ.get('EXECUTABLE_DIR', Path(__file__).parent.parent / "build" / "bin")
        app_path = Path(exe_dir) / f"{app_name}.exe"

        return subprocess.run([str(app_path)] + args, capture_output=True, text=True)
    
    return _run