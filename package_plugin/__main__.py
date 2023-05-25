import os
import shutil
from zipfile import ZipFile

PACKAGE_PATH: str = os.path.dirname(os.path.realpath(__file__))

PLUGIN_FILES: list[str] = ["__init__.py", "elegoo_neptune_3_thumbnails.py", "LICENSE", "plugin.json", "README.md"]

BUILD_NAME = os.path.join(PACKAGE_PATH, "ElegooNeptune3Thumbnails.curapackage")

if __name__ == "__main__":
    """
    Package the plugin
    """

    # Clear old builds
    if os.path.exists(BUILD_NAME):
        os.remove(BUILD_NAME)

    # Clone base build
    shutil.copyfile(os.path.join(PACKAGE_PATH, "base.curapackage"), BUILD_NAME)

    # Add plugin files
    with ZipFile(BUILD_NAME, 'a') as file:
        for plugin_file in PLUGIN_FILES:
            file.write(os.path.join(PACKAGE_PATH, "..", plugin_file),
                       f"/files/plugins/ElegooNeptune3Thumbnails/{plugin_file}")