#!/usr/bin/env python3

from setuptools import setup
import reportbug

# i18n = []
# for lang in glob.glob('*.po'):
#     lang = lang[:-3]
#     if lang == 'messages':
#         continue
#     i18n.append( ('share/locale/%s/LC_MESSAGES' % lang,
#                   ['i18n/%s/LC_MESSAGES/foomatic-gui.mo' % lang]) )

setup(name='reportbug', version=reportbug.VERSION_NUMBER,
      description='bug reporting tool',
      author='reportbug maintenance team',
      author_email='debian-reportbug@lists.debian.org',
      url='https://salsa.debian.org/reportbug-team/reportbug',
      data_files=[('share/reportbug', ['share/handle_bugscript',
                                       'share/reportbug.el',]),
                  ('share/bug/reportbug', ['share/presubj', 'share/script',
                                           'share/control'])],
      license='MIT',
      packages=['reportbug', 'reportbug.ui'],
      scripts=['bin/reportbug', 'bin/querybts'])
