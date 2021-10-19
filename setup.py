from setuptools import setup, find_packages

setup(
        name="convex",
        version="0.0.1",
        url="",
        package_dir={"":"src"},
        packages=find_packages(where="src"),
        python_requires=">=3.8"
    )
