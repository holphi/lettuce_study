import sys
from os.path import join,abspath

print 'Terrain will be executed automatically before lettuce tests'

sys.path.append(join(abspath('.'), 'lib'))

print sys.path