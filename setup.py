from setuptools import setup, find_packages

print(find_packages(include=["manysteps", "manysteps.*"]))

setup(
    author="Jackson Markowski",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="A short description",
    # install_requires=requirements,
    license="MIT license",
    # long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords="manysteps",
    name="manysteps",
    packages=find_packages(include=["manysteps", "manysteps.*"]),
    package_data={"manysteps": ["py.typed"]},
    # test_suite='tests',
    # tests_require=test_requirements,
    url="https://github.com/JacksonMarkowski/manysteps",
    version="0.0.1",
    zip_safe=False,
)
