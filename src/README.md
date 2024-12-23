# Some Helper Functions

## SVG to PNG

1. install cairo with brew install cairo

2. insall python wrapper:

    - pip install svglib
    - pip install rlPyCairo

3. Then export path:

```bash
export PKG_CONFIG_PATH="/usr/local/lib/pkgconfig:/opt/homebrew/lib/pkgconfig:$PKG_CONFIG_PATH"
export DYLD_LIBRARY_PATH="/usr/local/lib:/opt/homebrew/lib:$DYLD_LIBRARY_PATH"
```

see: <https://stackoverflow.com/questions/73637315/oserror-no-library-called-cairo-2-was-found-from-custom-widgets-import-proje>

```bash
python src/svg_to_png.py --name logo
```

## Download Favicon Icon

```bash
python src/favicon.py --url "https://design.landbw.de"
```
