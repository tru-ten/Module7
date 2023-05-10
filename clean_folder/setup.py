from setuptools import setup

setup(name='clean_folder',
      version='1',
      description='Will clean your dirty folder :)',
      url='https://github.com/tru-ten/Module7',
      author='Bohdan Zhemelko',
      author_email='bogdan.zhemelko@gmail.com',
      license='lol',
      packages=['clean_folder'],
      entry_points={'console_scripts':['clean-folder=clean_folder.clean:main']})