from distutils.core import setup
import py2exe
import os

assets = []
for files in os.listdir("assets/"):
    f1 = "assets/" + files
    if os.path.isfile(f1):  # skip directories
        f2 = "assets", [f1]
        assets.append(f2)

setup(
    windows=[
        {
            "script": "main.pyw",
            "icon_resources": [(1, "assets/favicon.ico")],
            "dest_base": "lofi",
        }
    ],
    data_files=assets,
    options={
        "py2exe": {"includes": ["vlc", "PIL"]},
    },
)
