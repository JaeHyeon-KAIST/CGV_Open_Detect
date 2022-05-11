from setuptools import setup

setup(name="test_py2xxx",
      description="py2app test application",
      version="0.0.1",
      setup_requires=["py2app"],
      app=["main.py"],
      options={
          "py2app": {
              "includes": ["PySide.QtCore",
                           "PySide.QtGui",
                           "PySide.QtWebKit",
                           "PySide.QtNetwork",
                           "PySide.QtXml"]
          }
      })