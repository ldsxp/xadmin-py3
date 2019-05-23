#!/usr/bin/env python
from setuptools import setup

# version_tuple = __import__('xadmin').VERSION
# version = ".".join([str(v) for v in version_tuple])
version = '2.0.2'

setup(
    name='xadmin-py3',
    version=version,
    description='直接替换Django管理员带来了许多好东西，完全可扩展的插件支持，基于Twitter Bootstrap的漂亮用户界面。',
    long_description=open('README.md', encoding='utf-8').read(),
    author='sshwsfc',
    author_email='sshwsfc@gmail.com',
    maintainer="lds",
    maintainer_email="85176878@qq.com",
    license='BSD',
    url='https://github.com/ldsxp/xadmin-py3',
    download_url='https://github.com/ldsxp/xadmin-py3/archive/master.zip',
    packages=['xadmin', 'xadmin.migrations', 'xadmin.plugins', 'xadmin.templatetags', 'xadmin.views'],
    include_package_data=True,
    long_description_content_type='text/markdown',
    install_requires=[
        'setuptools',
        'django>=2.2',
        'django-crispy-forms>=1.7.2',
        'django-reversion>=3.0.0',
        'django-formtools>=2.1',
        'django-import-export>=1.2.0',
        'httplib2==0.12.3',
        'future',
        'six'
    ],
    extras_require={
        'Excel': ['xlwt', 'xlsxwriter'],
        'Reversion': ['django-reversion>=3.0.0'],
    },
    zip_safe=False,
    keywords=['admin', 'django', 'xadmin', 'xadmin-py3', 'bootstrap'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        "Programming Language :: JavaScript",
        'Programming Language :: Python',
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
