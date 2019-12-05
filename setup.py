from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

name = 'external'

setup(
    name=name,
    version='0.0.0',
    description=long_description.splitlines()[0],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ravindra Marella',
    url='https://github.com/marella/{}'.format(name),
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='{} multiprocessing'.format(name),
)
