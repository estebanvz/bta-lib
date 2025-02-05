import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="etalib",
    version="0.0.1",
    author="Esteban Vilca",
    author_email="esteban.wilfredo.g@gmail.com",
    description="eta-lib technical analysis library for trading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/estebanvz/eta-lib",
    project_urls={
        "Bug Tracker": "https://github.com/estebanvz/eta-lib/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7.9",
    install_requires=[
       "numpy>=1.21.5",
       "pandas>=1.3.4",
       "scipy>=1.7.3"
   ],
)