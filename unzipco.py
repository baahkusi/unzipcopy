import os
from zipfile import ZipFile


def unzipco(zipz, *fnames):
    """
    :zipz: Directory containing zipped files.
    :fnames: Names of files to copy.
    """
    # Get list of all zip files
    print('Getting zips ...\n')
    zips = list(os.listdir(zipz))
    # Create Folder names based on fnames
    print('Creating dirs for ', [f.split('.')[0] for f in fnames], '\n')
    mkdirs(zipz,*fnames)
    # Unzip each file and copy fnames to related folder, number each.
    count = 0
    print('Begin Extraction ...\n')
    for zpf in zips:
        with ZipFile(zipz+'/'+zpf) as zp:
            for fn in fnames:
                try:
                    zp.extract(fn,zipz)
                    f = ndes(fn, count)
                    print('Extracting '+ fn + ' to ' + f + '...\n')
                    os.rename(zipz+'/'+fn, zipz+'/'+f)
                except:
                    pass
        count += 1


def mkdirs(zipz,*fnames):
    for fname in fnames:
        try:
            os.mkdir(zipz+'/'+fname.split('.')[0])
        except:
            pass


def ndes(fn, n):
    old_dir, ext = fn.split('.')
    new_dir = old_dir+str(n)
    new_file = new_dir+'.'+ext
    new_dest = old_dir+'/'+new_file
    return new_dest


if __name__ == '__main__':
    import sys
    zipz = sys.argv[1]
    fnames = sys.argv[2:]
    unzipco(zipz, *fnames)