import glob
import os

if not os.path.exists('build'):
    os.makedirs('build')

files = glob.glob('*.ipynb')

for f in files:
	os.system('ipython nbconvert "{0}" --output="build/{1}" --template=basic'.format(f, os.path.basename(f)))