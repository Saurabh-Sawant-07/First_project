from setuptools import find_packages,setup

setup(
    name = "ML Project",
    version="0.0.1",
    author="Saurabh",
    author_email = "saurabhsawanteducation@gmail.com",
    packages = find_packages(),
    install_requirement = ["pandas", "numpy","seaborn"],
)