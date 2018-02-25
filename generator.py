from dump_reader import load_dump
import json
from ontop import getOntop
from tabs import getTabs
import sys

if __name__ == '__main__':

    if len(sys.argv) == 1:
        dump_path = 'example.dump'
        result_path = 'result_config'
    elif len(sys.argv) == 2:
        raise BaseException("Script accepts exactly 2 arguments!")
    else:
        dump_path = sys.argv[1]
        result_path = sys.argv[2]

    cpe_dump = load_dump(dump_path)


    ontop = getOntop(cpe_dump)
    tabs = getTabs(cpe_dump)
    config = {
        'ontop': ontop,
        'tabs': tabs
    }

    with open(result_path, 'w') as fp:
        json.dump(config, fp, indent=4)
    print('Success')
