import setuptools

with open("README.md", "r", encoding="UTF-8") as f:
    long_description = f.read()

setuptools.setup(
    name="use-proper-hosting",
    version="1.0.0",
    author="eunwoo1104",
    author_email="sions04@naver.com",
    description="No more support server flooding with questions about unsupported hosting.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/playground1104/use-proper-hosting",
    packages=setuptools.find_packages()
)