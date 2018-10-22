from setuptools import setup

setup(name='ccmsproteosafepythonapi',
      version='0.1',
      description='ccmsproteosafepythonapi',
      url='http://proteomics.ucsd.edu',
      author='Mingxun Wang',
      author_email='miw023@ucsd.edu',
      license='LICENSE',
      packages=['ccmsproteosafepythonapi'],
      install_requires=[
          'pyteomics',
          'joblib',
          'lxml',
          'xmltodict',
          'numpy',
          'matplotlib',
          'requests',
          'csv'
      ],
      zip_safe=False)
