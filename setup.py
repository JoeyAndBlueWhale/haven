from setuptools import setup

setup(name='haven',
      version='0.4.1',
      description='Manage large-scale experiments',
      url='https://github.com/ElementAI/haven',
      author='Issam Laradji',
      author_email='issam.laradji@elementai.com',
      license='MIT',
      packages=['haven'],
      zip_safe=False,
      install_requires=[
        'imageio>=2.6.1',
        'matplotlib>=3.1.2',
        'numpy>=1.17.4',
        'opencv-python-headless>=4.1.2.30',
        'pandas>=0.25.3',
        'Pillow>=6.1',
        'pyparsing>=2.4.5',
        'python-dateutil>=2.8.1',
        'pytz>=2019.3',
        'scikit-image>=0.16.2',
        'scikit-learn>=0.22',
        'scipy>=1.3.1',
        'sklearn>=0.0',
        'torch>=0.0',
        'torchvision>=0.0',
        'notebook >= 4.0'
      ]),
