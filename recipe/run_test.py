import libarchive
from os.path import join

with libarchive.file_reader(join('test', 'hello_world.xar')) as archive:
    for entry in archive:
        print(entry.name)

