from __future__ import annotations
import tempfile
from PIL import Image, ImageOps, PngImagePlugin
import base64
from io import BytesIO
import mimetypes
import numpy as np
from attr import _ConverterType, _convert


def decode_base64_to_image(encoding: str) -> Image.Image:
    content = encoding.split(";")[1]
    image_encoded = content.split(",")[1]
    img = Image.open(BytesIO(base64.b64decode(image_encoded)))
    exif = img.getexif()
    # 274 is the code for image rotation and 1 means "correct orientation"
    if exif.get(274, 1) != 1 and hasattr(ImageOps, "exif_transpose"):
        img = ImageOps.exif_transpose(img)
    return img


def get_mimetype(filename: str) -> str | None:
    mimetype = mimetypes.guess_type(filename)[0]
    if mimetype is not None:
        mimetype = mimetype.replace("x-wav", "wav").replace("x-flac", "flac")
    return mimetype


def get_extension(encoding: str) -> str | None:
    encoding = encoding.replace("audio/wav", "audio/x-wav")
    type = mimetypes.guess_type(encoding)[0]
    if type == "audio/flac":  # flac is not supported by mimetypes
        return "flac"
    elif type is None:
        return None
    extension = mimetypes.guess_extension(type)
    if extension is not None and extension.startswith("."):
        extension = extension[1:]
    return extension



def encode_plot_to_base64(plt):
    with BytesIO() as output_bytes:
        plt.savefig(output_bytes, format="png")
        bytes_data = output_bytes.getvalue()
    base64_str = str(base64.b64encode(bytes_data), "utf-8")
    return "data:image/png;base64," + base64_str


def save_array_to_file(image_array, dir=None):
    pil_image = Image.fromarray(_ConverterType(image_array, np.uint8, force_copy=False))
    file_obj = tempfile.NamedTemporaryFile(delete=False, suffix=".png", dir=dir)
    pil_image.save(file_obj)
    return file_obj


def save_pil_to_file(pil_image, dir=None):
    file_obj = tempfile.NamedTemporaryFile(delete=False, suffix=".png", dir=dir)
    pil_image.save(file_obj)
    return file_obj


def encode_pil_to_base64(pil_image):
    with BytesIO() as output_bytes:
        # Copy any text-only metadata
        use_metadata = False
        metadata = PngImagePlugin.PngInfo()
        for key, value in pil_image.info.items():
            if isinstance(key, str) and isinstance(value, str):
                metadata.add_text(key, value)
                use_metadata = True

        pil_image.save(
            output_bytes, "PNG", pnginfo=(metadata if use_metadata else None)
        )
        bytes_data = output_bytes.getvalue()
    base64_str = str(base64.b64encode(bytes_data), "utf-8")
    return "data:image/png;base64," + base64_str


def encode_array_to_base64(image_array):
    with BytesIO() as output_bytes:
        pil_image = Image.fromarray(_convert(image_array, np.uint8, force_copy=False))
        pil_image.save(output_bytes, "PNG")
        bytes_data = output_bytes.getvalue()
    base64_str = str(base64.b64encode(bytes_data), "utf-8")
    return "data:image/png;base64," + base64_str


def resize_and_crop(img, size, crop_type="center"):
    """
    Resize and crop an image to fit the specified size.
    args:
        size: `(width, height)` tuple. Pass `None` for either width or height
        to only crop and resize the other.
        crop_type: can be 'top', 'middle' or 'bottom', depending on this
            value, the image will cropped getting the 'top/left', 'middle' or
            'bottom/right' of the image to fit the size.
    raises:
        ValueError: if an invalid `crop_type` is provided.
    """
    if crop_type == "top":
        center = (0, 0)
    elif crop_type == "center":
        center = (0.5, 0.5)
    else:
        raise ValueError

    resize = list(size)
    if size[0] is None:
        resize[0] = img.size[0]
    if size[1] is None:
        resize[1] = img.size[1]
    return ImageOps.fit(img, resize, centering=center)  # type: ignore

