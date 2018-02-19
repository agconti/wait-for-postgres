from setuptools import setup, find_packages

setup(
    name="wait-for-postgres",
    version="0.1.0",
    author="Andrew Conti",
    author_email="agc11d@gmail.com",
    url="https://github.com/agconti/wait-for-postgres",
    description="Wait for postgres to be ready.",
    long_description=open("README.md").read().strip(),
    packages=find_packages("wait_for_postgres"),
    install_requires=["psycopg2", ],
    test_suite="tests",
)
