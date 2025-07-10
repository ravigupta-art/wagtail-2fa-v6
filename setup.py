import re

from setuptools import find_packages, setup


install_requires = [
    "Django>=5.2",
    "Wagtail>=6.3",
    "django-otp>=0.8.1",
    "six>=1.14.0",
    "qrcode>=6.1",
]

tests_require = [
    "coverage==5.5",
    "pytest",
    "pytest-cov==2.12.1",
    "pytest-django==4.4.0",
    # Linting
    "flake8==3.9.2",  # 3.7.9
    "isort==5.9.3",
    "flake8-blind-except==0.2.0",
    "flake8-debugger==4.0.0",
]



setup(
    name="wagtail-2fa-v6",
    version="1.0.4",
    description="Wagtail two-factor auth, updated for Wagtail 6+",
    # long_description and long_description_content_type are now handled by pyproject.toml
    author="ravigupta-art",
    author_email="ravi.opensource@protonmail.com",
    url="https://github.com/ravigupta-art/wagtail-2fa-v6",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Framework :: Django :: 5.2",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 6",
        "Framework :: Wagtail :: 7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "Django>=5.2",
        "wagtail>=6.3",
        "django-otp>=0.8.1",
        "qrcode>=6.1",
        "six>=1.14.0",
    ],
    extras_require={
        "test": ["pytest", "pytest-django", "coverage"],
    },
    python_requires=">=3.10",
)
