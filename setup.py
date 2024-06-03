from setuptools import setup, find_packages

setup(
        name = "timmy",
        version = "0.1",
        description = "a basic timesheeting cli",
        author="jumper385 (Henry Chen)",
        install_package_data=True,
        install_requires = [
            "typer[all]",
            ],
        packages = find_packages(),
        keywords = ["timesheeting"],
        entry_points = {
            'console_scripts': [
                'timmy=timmy.main:app',
                ]},
            )

