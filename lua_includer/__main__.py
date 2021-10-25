import sys
import lua_includer

with open(sys.argv[1], "r") as f:
    with open(sys.argv[2], "w+") as of:
        of.writelines(lua_includer.include(f.readlines()))