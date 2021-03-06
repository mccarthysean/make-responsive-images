from pathlib import Path

from PIL import Image


def resize_image(
    file: Path,
    widths: list,
    fmt: str,
    qual: int,
    lower: bool,
    dashes: bool,
) -> list:
    """Resize the image to the widths specified"""

    # Convert to RGB so we can save as .webp
    image = Image.open(file).convert("RGB")

    # filter out duplicates and larger than original
    sizes_set = set()
    for width in widths:
        width = min(width, image.width)
        # orig_aspect = image.width / float(image.height)
        ratio = width / float(image.width)
        width = int(image.width * ratio + 0.5)
        height = int(image.height * ratio + 0.5)
        sizes_set.add((width, height))
    sizes = sorted(sizes_set)

    # if sizes[0] == image.size:
    #     # smallest size is original image
    #     return [image]

    # create the resized images
    resized = []
    filenames = []
    for (width, height) in sizes:
        if (width, height) == (image.width, image.height):
            new_image = image
        else:
            # new_image = image.resize((width, height), Image.ANTIALIAS)
            new_image = image.resize((width, height), Image.NEAREST)

        resized.append(new_image)

        # Save the image
        fmt = fmt.lower()
        if fmt not in ("jpg", "webp"):
            raise TypeError('fmt must be either "jpg" or "webp"')

        filename_new = f"{file.stem}-{width}px.{fmt}"

        if lower:
            filename_new = filename_new.lower()

        if dashes:
            filename_new = filename_new.replace("_", "-")

        path_new = file.parent.joinpath(filename_new)
        fmt2 = "jpeg" if fmt == "jpg" else fmt
        # Set quality to max 100, min 0
        quality = max(0, min(100, qual))
        # The optimize flag will do an extra pass on the image to find a way
        # to reduce its size as much as possible
        new_image.save(path_new, fmt2, quality=quality, optimize=True)

        # filename_new = f"{file.stem}-{width}px.jpg"
        # path_new = file.parent.joinpath(filename_new)
        # new_image.save(path_new, "JPEG", quality=50, optimize=True)

        filenames.append((filename_new, width, height))

        # if crop:
        #     new_image = ImageOps.fit(
        #         orig_image,
        #         (width, height),
        #         method=Image.BICUBIC,
        #         centering=(crop[0] / 100.0, crop[1] / 100.0),
        #     )
        # else:
        #     new_image = orig_image.app(
        #         (width, height),
        #         resample=Image.BICUBIC
        #     )

    return filenames


def make_html(
    orig_img_file: Path,
    filenames: list,
    classes: str,
    img_sizes: str,
    lazy: bool,
    alt: str,
    dir: str,
    flask: bool,
) -> None:
    """Resize the image to the widths specified"""

    html_str = "<img "

    if classes:
        html_str += f'class="{classes}" '
    if lazy:
        html_str += 'loading="lazy" '

    html_str += f'\n  sizes="{img_sizes}" '
    html_str += f'\n  alt="{alt}" '

    def _get_filename(dir: str, filename: str, flask: bool) -> str:
        if dir:
            if flask:
                return (
                    r"{{ " + f"url_for('static', filename='{dir}/{filename}')" + r" }}"
                )
            return f"{dir}/{filename}"
        return filename

    srcset_str = '\n  srcset="'
    n_filenames = len(filenames)
    for num, (filename, width, height) in enumerate(filenames):
        is_last = num == (n_filenames - 1)
        filename2 = _get_filename(dir=dir, filename=filename, flask=flask)
        if not is_last:
            srcset_str += "\n    " + filename2 + f" {width}w,"
        else:
            srcset_str += "\n    " + filename2 + f' {width}w"'
            srcset_str += '\n  src="' + filename2 + '" '
            srcset_str += f'\n  width="{width}" height="{height}"'

    html_str += srcset_str
    html_str += ">"

    html_path = orig_img_file.parent.joinpath(f"img-tag-{filename}.html")
    with open(html_path, "w") as f:
        f.write(html_str)

    return None
