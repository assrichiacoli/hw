import os


class FileSystemError(Exception):
    ''' Class for errors in filesystem module '''
    pass


class FSItem(object):
    ''' Common class for OS items OS: Files and Directories '''

    def existnt(self, path):
        if not os.path.exists(path):
            raise FileSystemError('{0} does not exist'.format(path))

    def exist(self, path):
        if os.path.exists(path):
            raise FileSystemError('{0} already exists'.format(path))

    def isdir(self, path):
        if os.path.isdir(path):
            raise FileSystemError('{0} is directory'.format(path))
            
    def isfil(self, path):
        if os.path.isfile(path):
            raise FileSystemError('{0} is file'.format(path))

    def __init__(self, path):
        ''' Creates new FSItem instance by given path to file '''
        self.path = path

    def rename(self, newname):
        ''' Renames current item
                raise FileSystemError if item does not exist
                raise FileSystemError if item "newname" already exists '''
        os.rename(self.path, newname)
        self.path = os.path.join(os.path.split(self.path)[0], newname)
        print("Renamed successfully!")

    def create(self):
        pass

    def getname(self):
        ''' Returns name of current item '''
        return os.path.split(self.path)[1]

    def isfile(self):
        ''' Returns True if current item exists and current item is file, False otherwise '''
        return os.path.isfile(self.path)

    def isdirectory(self):
        ''' Returns True if current item exists and current item is directory, False otherwise '''
        return os.path.isdir(self.path)


class File(FSItem):
    ''' Class for working with files '''

    def __init__(self, path):
        ''' Creates new File instance by given path to file
                raise FileSystemError if there exists directory with the same path '''
        super().__init__(path)
        self.isdir(self.path)

    def create(self):
        ''' Creates new item in OS
                raise FileSystemError if item with such path already exists '''
        self.exist(self.path)
        open(self.path, 'w+').close()

    def __len__(self):
        ''' Returns size of file in bytes
                raise FileSystemError if file does not exist '''
        self.existnt(self.path)
        return os.path.getsize(self.path)

    def getcontent(self):
        ''' Returns list of lines in file (without trailing end-of-line)
                raise FileSystemError if file does not exist '''
        self.existnt(self.path)
        return open(self.path, 'r').read().splitlines()

    def __iter__(self):
        ''' Returns iterator for lines of this file
                raise FileSystemError if file does not exist '''
        return iter(self.getcontent())


class Directory(FSItem):
    ''' Class for working with directories '''

    def __init__(self, path):
        ''' Creates new Directory instance by given path
                raise FileSystemError if there exists file with the same path '''
        super().__init__(path)
        self.isfil(self.path)

    def create(self):
        ''' Creates new item in OS
                raise FileSystemError if item with such path already exists '''
        self.exist(self.path)
        os.mkdir(self.path)

    def items(self):
        ''' Yields FSItem instances of items inside of current directory
                raise FileSystemError if current directory does not exists '''
        self.existnt(self.path)
        return self.files()
        return self.subdirectories()

    def files(self):
        ''' Yields File instances of files inside of current directory
                raise FileSystemError if current directory does not exists '''
        self.existnt(self.path)
        for x in os.listdir(self.path):
            new = os.path.join(self.path, x)
            if os.path.isfile(new):
                yield new

    def subdirectories(self):
        ''' Yields Directory instances of directories inside of current directory
                raise FileSystemError if current directory does not exists '''
        self.existnt(self.path)
        for x in os.listdir(self.path):
            new = os.path.join(self.path, x)
            if os.path.isdir(new):
                yield new

    def filesrecursive(self):
        ''' Yields File instances of files inside of this directory,
                inside of subdirectories of this directory and so on...
                raise FileSystemError if directory does not exist '''
        self.existnt(self.path)
        for root, directories, file in os.walk(self.path):
            for x in file:
                yield x

    def getsubdirectory(self, name):
        ''' Returns Directory instance with subdirectory of current directory with name "name"
                raise FileSystemError if item "name" already exists and item "name" is not directory '''
        self.exist(os.path.join(self.path,name))
        return Directory(os.path.join(self.path,name))
