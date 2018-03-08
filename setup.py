try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("pdist",
              ["pdist.pyx", 'cdist.c'],
			  runtime_library_dirs=[])
]
setup(
    name="Demos",
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules
)