

#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': 'Kenneth T. Moore',
 'author_email': 'kenneth.t.moore-1@nasa.gov',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': 'OpenMDAO component wrapper for FLOPS',
 'download_url': '',
 'entry_points': '[openmdao.component]\nflops_wrapper.flops_wrapper.FlopsWrapper=flops_wrapper.flops_wrapper:FlopsWrapper',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license': 'Apache License, Version 2.0',
 'maintainer': 'Kenneth T. Moore',
 'maintainer_email': 'kenneth.t.moore-1@nasa.gov',
 'name': 'flops_wrapper',
 'package_data': {'flops_wrapper': ['sphinx_build/html/usage.html',
                                    'sphinx_build/html/py-modindex.html',
                                    'sphinx_build/html/genindex.html',
                                    'sphinx_build/html/search.html',
                                    'sphinx_build/html/srcdocs.html',
                                    'sphinx_build/html/index.html',
                                    'sphinx_build/html/objects.inv',
                                    'sphinx_build/html/searchindex.js',
                                    'sphinx_build/html/.buildinfo',
                                    'sphinx_build/html/pkgdocs.html',
                                    'sphinx_build/html/_sources/pkgdocs.txt',
                                    'sphinx_build/html/_sources/srcdocs.txt',
                                    'sphinx_build/html/_sources/index.txt',
                                    'sphinx_build/html/_sources/usage.txt',
                                    'sphinx_build/html/_modules/index.html',
                                    'sphinx_build/html/_modules/flops_wrapper/flops_wrapper.html',
                                    'sphinx_build/html/_static/underscore.js',
                                    'sphinx_build/html/_static/pygments.css',
                                    'sphinx_build/html/_static/basic.css',
                                    'sphinx_build/html/_static/file.png',
                                    'sphinx_build/html/_static/sidebar.js',
                                    'sphinx_build/html/_static/jquery.js',
                                    'sphinx_build/html/_static/default.css',
                                    'sphinx_build/html/_static/minus.png',
                                    'sphinx_build/html/_static/doctools.js',
                                    'sphinx_build/html/_static/searchtools.js',
                                    'sphinx_build/html/_static/plus.png',
                                    'test/TURPRP',
                                    'test/xflp2_openmdao.in',
                                    'test/xflp2.in',
                                    'test/TBYPAS',
                                    'test/xflp1.in',
                                    'test/xflp5_openmdao.out',
                                    'test/xflp3_openmdao.in',
                                    'test/xflp5.in',
                                    'test/ENDRAG',
                                    'test/xflp5_openmdao.in',
                                    'test/TFNMX3',
                                    'test/xflp6_openmdao.out',
                                    'test/TURJET',
                                    'test/test_flops_wrapper.py',
                                    'test/TURJT2',
                                    'test/xflp2_openmdao.dump',
                                    'test/xflp3.out',
                                    'test/xflp1_openmdao.in',
                                    'test/xflp1_openmdao.out',
                                    'test/xflp3.in',
                                    'test/xflp6.out',
                                    'test/xflp4.in',
                                    'test/TFN3SH',
                                    'test/openmdao_log.txt',
                                    'test/xflp6_openmdao.dump',
                                    'test/xflp4_openmdao.out',
                                    'test/xflp3_openmdao.out',
                                    'test/xflp1.out',
                                    'test/ENGTAB',
                                    'test/TFNMIX',
                                    'test/TFNSP3',
                                    'test/TFNSEP',
                                    'test/xflp3_openmdao.dump',
                                    'test/xflp2_openmdao.out',
                                    'test/xflp4_openmdao.dump',
                                    'test/xflp1_openmdao.dump',
                                    'test/xflp4.out',
                                    'test/xflp5.out',
                                    'test/xflp2.out',
                                    'test/xflp6_openmdao.in',
                                    'test/xflp5_openmdao.dump',
                                    'test/xflp6.in',
                                    'test/xflp4_openmdao.in']},
 'package_dir': {'': 'src'},
 'packages': ['flops_wrapper'],
 'url': 'https://github.com/OpenMDAO-Plugins/flops_wrapper',
 'version': '0.8',
 'zip_safe': False}


setup(**kwargs)

