from setuptools import setup, find_packages

setup(
    name='django-cookie-sessions',
    version=__import__('cookiesessions').__version__,
    description='A secure cookie-based session engine for Django.',
    long_description=open('README.txt').read(),
    author='Eric Florenzano',
    author_email='floguy@gmail.com',
    url='https://github.com/ericflo/django-cookie-sessions',
    packages=['cookiesessions'],
    zip_safe=False,
    classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Web Environment',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Framework :: Django',
    ]
)