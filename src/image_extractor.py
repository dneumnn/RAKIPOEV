import os
import sys
import argparse

import urllib
import urllib.request
#import request



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="url to be parsed", required=True)
    parser.add_argument("--domain", required=True)
    args = parser.parse_args()

    with urllib.request.urlopen(url=args.url) as f:
        orig_data = f.read().decode('utf-8')
    
    urls = []
    image_suffixes = ["png", "jpeg", "svg", "jpg"]
    patterns = ['href="', 'src="', 'data-image="']
    #import pdb; pdb.set_trace()
    for pattern in patterns:
        data = orig_data
        running = True
        while running:
            x = data.find(pattern)
        
            if x > -1:
                #import pdb; pdb.set_trace()
                data = data[x+len(pattern):]
                y = data.find('"')
                url = data[0:y]

                splitted = url.split(".")
                suffix = ""
                if len(splitted) > 1:
                    suffix = splitted[1].lower()

                if suffix in image_suffixes:
                    
                    urls.append(url)
                    data = data[y:]

            else:
                running = False

    id = 0
    for url in urls:
        name = url.split("/")[-1]
        id += 1
        url = f"{args.domain}{url}"
        print(url)
        urllib.request.urlretrieve(url, f"./{id}_{name}")





