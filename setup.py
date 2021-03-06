from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Full_data_alchemy", # the name that you will install via pip
    version="1.1",
    author="Full Data Alchemist",
    author_email="imani.beasley.72@gmail.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/Full-Data-Alchemist/Lambdata-full-data-alchemist",
    #keywords="",
    packages=find_packages() # ["Full_data_alchemy"]
)