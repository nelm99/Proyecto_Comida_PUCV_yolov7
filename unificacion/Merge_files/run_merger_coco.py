try:
    from datetime import datetime
    from source.merge_annotations import *
    import json
    import os
except ImportError as e:
    print('{} Mssg: cannot import library: {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), e))

if __name__ == '__main__':
    rootdir = os.path.dirname(os.path.abspath(__file__))+os.sep

    config = json.loads(open('{}config/config_merge.json'.format(rootdir)).read())
    config = {
        'rootdir': rootdir,
        'data': config['data']
    }
    print(rootdir)

    try:
        process =  merge(config)
        process.merge_folders()

    except KeyboardInterrupt:
        print('{} RUN MSSG: weight estimation process Interrupt by user...'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    # except Exception as e:
    #     print('{} RUN MSSG: weight estimation process Error {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), e))