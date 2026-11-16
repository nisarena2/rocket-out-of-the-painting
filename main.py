import os
import shutil

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
here = os.path.dirname(os.path.abspath(__file__))
shutil.copyfile(os.path.join(here, "entry.png"),
                os.path.join(out, "entry.png"))
