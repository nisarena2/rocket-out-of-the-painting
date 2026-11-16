import os
import shutil

# Copy the entry image to the output directory (default /output).
src = os.path.join(os.path.dirname(__file__), "entry.png")
dst = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
os.makedirs(os.path.dirname(dst), exist_ok=True)
shutil.copyfile(src, dst)
