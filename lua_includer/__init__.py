__version__ = '0.1.0'

def include(lines):
    rlines = []
    for line in lines:
        if line.startswith("--include- "):
            fp = line[11:]
            with open(fp, "r") as f:
                rlines += include(f.readlines())
        else:
            rlines += line
    return rlines