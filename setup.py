from distutils.core import setup
from setuptools import find_packages

setup(
    name='django_formrenderer',
    version=__import__('formrenderer').__version__,
    description='A reusable django app for customising form rendering from your template.',
    author='Humphrey Murray (Datalive Software)',
    author_email='hmurray@datalive.com.au',
    url='https://github.com/humphrey/django_formrenderer',
    # py_modules=[
    #     'formrenderer',
    #     # 'formrenderer.templatetags',
    # ],
    install_requires = [
        "django",
    ],
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    long_description=open('README.md').read(),
)