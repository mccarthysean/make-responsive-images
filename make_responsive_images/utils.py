from pathlib import Path

from PIL import Image


def resize_image(
    file: Path,
    widths: list,
) -> list:
    """Resize the image to the widths specified"""

    image = Image.open(file)

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

    if sizes[0] == image.size:
        # smallest size is original image
        return [image]

    # create the resized images
    resized = []
    filenames = []
    for (width, height) in sizes:
        if (width, height) == (image.width, image.height):
            resized.append(image)
            continue
        # new_image = image.resize((width, height), Image.ANTIALIAS)
        new_image = image.resize((width, height), Image.NEAREST)
        resized.append(new_image)

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

        # Save the image
        filename_new = f"{file.stem}-{width}px{file.suffix}"
        path_new = file.parent.joinpath(filename_new)
        new_image.save(path_new)

        filenames.append((filename_new, width))

    return filenames


def make_html(
    orig_img_file: Path,
    filenames: list,
    classes: str,
    img_sizes: str,
    lazy: bool,
    alt: str,
    dir: str,
) -> None:
    """Resize the image to the widths specified"""

    html_str = "<img "

    if classes:
        html_str += f'class="{classes}" '
    if lazy:
        html_str += 'loading="lazy" '

    html_str += f'\n  sizes="{img_sizes}" '
    html_str += f'\n  alt="{alt}" '

    def _get_filename(dir: str, filename: str) -> str:
        if dir:
            return f"{dir}/{filename}"
        return filename

    src_filename = _get_filename(dir, orig_img_file.name)
    html_str += f'\n  src="{src_filename}" '

    srcset_str = '\n  srcset="'
    n_filenames = len(filenames)
    for num, (filename, width) in enumerate(filenames):
        is_last = num == (n_filenames - 1)
        filename = _get_filename(dir, filename)
        if is_last:
            srcset_str += f'\n    {filename} {width}w"'
        else:
            srcset_str += f"\n    {filename} {width}w,"

    html_str += srcset_str
    html_str += ">"

    html_path = orig_img_file.parent.joinpath("img_tag.html")
    with open(html_path, "w") as f:
        f.write(html_str)

    return None
