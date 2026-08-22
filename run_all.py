"""Execute every Cartopy projection script and regenerate the image gallery."""
from pathlib import Path
import subprocess, sys

root = Path(__file__).resolve().parent
for script in sorted((root / "scripts").glob("*.py")):
    print(f"Running {script.name} ...")
    subprocess.run([sys.executable, str(script)], cwd=root, check=True)
