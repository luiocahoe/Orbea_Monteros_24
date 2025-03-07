from setuptools import setup, find_packages

setup(
    name="pec4",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas==2.2.3",
        "matplotlib==3.10.0",
        "Faker==33.3.1",
        "regex",
        "pylint==3.3.3",
        "coverage==7.6.10",
    ],
    python_requires='>=3.12.7',
)
