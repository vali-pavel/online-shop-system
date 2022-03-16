from dataclasses import dataclass
from typing import List
from wand.image import Image
import magic, os

import constants
import helpers


@dataclass
class IFile:
    file_name: str
    file_path: str


class Product:
    @staticmethod
    def validate_file_type(file_buffer: bytes) -> bool:
        file_format = magic.from_buffer(file_buffer, mime=True)
        return file_format in constants.VALID_IMAGE_FORMATS

    def resize_and_save_img(
        self,
        file_buffer: bytes,
        filename: str,
        product_id: int,
    ):
        with Image(blob=file_buffer) as img:
            img.sample(constants.IMAGE_WIDTH, constants.IMAGE_HEIGHT)
            folder_path = self._get_folder_path(product_id)
            helpers.create_folder(folder_path)
            img_path = f"{folder_path}/{filename}"
            img.save(filename=img_path)

    def get_images(self, product_id: int) -> List[IFile]:
        file_names = os.listdir(self._get_folder_path(product_id))
        files: List[IFile] = []
        for file_name in file_names:
            file_path = os.path.join(self._get_folder_path(product_id), file_name)
            file = IFile(file_name, file_path)
            files.append(file)
        return files

    @staticmethod
    def _get_folder_path(product_id: int):
        return f"./assets/{str(product_id)}"
