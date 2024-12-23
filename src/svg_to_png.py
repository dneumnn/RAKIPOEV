import os
import sys
import argparse

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

working_dir = os.getcwd()
working_name = "RAKIPOEV"
file_path = ""
x = working_dir.find(working_name)
if x > -1:
    file_path = f"{working_dir[0:x]}{working_name}{os.sep}{working_name}-docs{os.sep}docs{os.sep}assets{os.sep}"

print(file_path)
if len(file_path) == 0:
    print(f"program aborted, started in wrong directory. Please goto {working_name}")
    sys.exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="file name without suffix", required=True)
    args = parser.parse_args()
    drawing = svg2rlg(f"{file_path}{args.name}.svg")
    renderPM.drawToFile(drawing, f"{file_path}{args.name}.png", fmt="PNG")
