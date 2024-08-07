import zipfile
import pytest
import os
import shutil
import pathes


@pytest.fixture(scope='function', autouse=True)
def given_zip_file():
    if not os.path.exists(pathes.ZIPPED_PATH):
        os.mkdir(pathes.ZIPPED_PATH)
    with zipfile.ZipFile(pathes.ZIPPED_PATH + '/zipped_files.zip', 'w') as zf:
        for file in os.listdir(pathes.RESOURCES_PATH):
            add_file = os.path.join(pathes.RESOURCES_PATH, file)
            zf.write(add_file, os.path.basename(add_file))

    yield

    shutil.rmtree(pathes.ZIPPED_PATH)
