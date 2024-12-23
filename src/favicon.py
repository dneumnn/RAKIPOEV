import os
import sys
import argparse
import urllib.request
import urllib

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
    parser.add_argument("--url", help="url to be parsed", required=True)
    args = parser.parse_args()

    with urllib.request.urlopen(url=args.url) as f:
        data = f.read().decode('utf-8')
    
    x = data.find('href="/favicon')
    if x > -1:
        data = data[x:]
        print(data[0:100])
        y = data.find("/>")
        image_link = data[6:y-1]

        imgURL = f"{args.url}{image_link}"
        print(imgURL)
        urllib.request.urlretrieve(imgURL, f"{file_path}favicon.png")




