from setuptools import setup, find_packages

setup(
    name="mini-language",  # Package name (used for installation)
    version="1.0.0",       # Package version
    author="Ramin&Atefe",
    author_email="Ramin&Atefe.email@example.com",
    description="Mini language interpreter",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Ramin&Atefe/mini-language",  # GitHub repo
    packages=find_packages(include=["mini", "mini.*"]),  # Use 'mini' as the base package
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "mini=mini.shell.repl:start_repl",  # Command to start REPL
        ],
    },
    install_requires=[],  # List of dependencies
    python_requires=">=3.7",  # Minimum Python version
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
