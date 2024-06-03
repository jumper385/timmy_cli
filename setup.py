from setuptools import setup, find_packages

setup(
        name = "timmy-time",
        version = "0.1",
        description = "a basic timesheeting cli",
        author="jumper385 (Henry Chen)",
        install_package_data=True,
        install_requires = [
            "typer[all]"],
        packages = find_packages(),
        keywords = ["timesheeting"],
        entry_points = {
            'console_scripts': [
                'timmy-time=timmy.main:app']},
        classifiers = [
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            ])

