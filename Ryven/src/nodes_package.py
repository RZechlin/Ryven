from os.path import basename, dirname, splitext, normpath, join, abspath, splitdrive


class NodesPackage:
    """
    A small container to store meta data about imported node packages.
    """

    def __init__(self, directory: str):

        self.name = basename(normpath(directory))
        self.directory = directory

        self.file_path = normpath(join(directory, 'nodes.py'))

    def config_data(self):
        return {
            'name': self.name,
            'dir': self.directory,
        }

    def add_path(self):
        self.directory = join(splitdrive(__file__)[0], splitdrive(self.directory)[1])
        self.file_path = normpath((join(self.directory, 'nodes.py')))
