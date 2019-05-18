import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="wrds2pg",
    version="0.1.2",
    author="Ian Gow",
    author_email="iandgow@gmail.com",
    description="Download wrds tables and upload to PostgreSQL, upload SAS file to PG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iangow-public/wrds_pg/",
    packages=setuptools.find_packages(),
    install_requires=['pandas', 'sqlalchemy', 'paramiko'],
    python_requires=">=3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
