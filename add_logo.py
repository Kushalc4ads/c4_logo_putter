import os
from PIL import Image, ImageEnhance, ImageOps
from PIL import EpsImagePlugin

EpsImagePlugin.gs_windows_binary = r'gswin64c'

def is_light_image(image, threshold=127):
    grayscale = image.convert('L')  # Convert to grayscale
    histogram = grayscale.histogram()
    pixels = sum(histogram)
    light_pixels = sum(histogram[threshold:])
    return light_pixels > pixels // 2

def add_logo(image, logo_path, position='bottom-right', size_ratio=0.1):
    logo = Image.open(logo_path)
    image_width, image_height = image.size
    logo.thumbnail((image_width * size_ratio, image_height * size_ratio), Image.Resampling.LANCZOS)  # Updated here
    logo_width, logo_height = logo.size

    if position == 'bottom-right':
        position = (image_width - logo_width - 10, image_height - logo_height - 10)

    image.paste(logo, position, logo.convert('RGBA'))
    return image


def process_images(directory, tagline=False):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            image_path = os.path.join(directory, filename)
            image = Image.open(image_path)

            if tagline:
                black_logo = 'C4ADSLOGOTYPE/PNG/C4ADS_Logotype-tagline_FINAL_Black.png'
                white_logo = 'C4ADSLOGOTYPE/PNG/C4ADS_Logotype-tagline_FINAL_White.png'
            else:
                black_logo = 'C4ADSLOGOTYPE/PNG/C4ADS_Logotype-NOtagline_FINAL_Black.png'
                white_logo = 'C4ADSLOGOTYPE/PNG/C4ADS_Logotype-NOtagline_FINAL_White.png'

            if is_light_image(image):
                logo_path = black_logo
            else:
                logo_path = white_logo

            image_with_logo = add_logo(image, os.path.join(directory, logo_path))
            image_with_logo.save(image_path)
            print(f'Processed {filename}')

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Add logos to images in a directory.")
    parser.add_argument("directory", help="Directory containing the images")
    parser.add_argument("--tagline", action="store_true", help="Use logos with tagline")

    args = parser.parse_args()
    process_images(args.directory, args.tagline)
