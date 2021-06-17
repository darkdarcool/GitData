from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()
# delete the url info if error, also change version in an update
setup(
  name = "GitGrabber",
  version = "0.0.1",
  description = "Get the GitHub data you need!",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = "darkdarcool30",
  author_email = "darkdarcool@gmail.com",
#To find more licenses or classifiers go to: https://pypi.org/classifiers/
  license = "GNU General Public License v3 (GPLv3)",
  packages=['GitData', 'GitGrabber'],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
  "Operating System :: OS Independent",
],
  zip_safe=True,
  python_requires = ">=3.0",
) 
