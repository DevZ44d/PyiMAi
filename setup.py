import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    lng_description = fh.read()

setuptools.setup(
    name="PyiMAi",
    version="1.0.0",
    author="AhMed",
    author_email="asyncpy@proton.me",
    license="MIT",
    description="PyiMAi is a lightweight AI-powered CLI tool that allows you to interact with an AI model directly from your terminal, with optional image support.",
    long_description=lng_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "PyiMAi=PyiMAi.cil:console",
        ],
    },
    python_requires=">=3.6",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
