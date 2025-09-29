import os
from PIL import Image
import argparse


def enlarge(image_path: str, output_dir: str = "output"):
    """
    Enlarges the input image (2x scale) and saves it in the output directory.

    Args:
        image_path (str): Path to the input image.
        output_dir (str): Directory where the enlarged image will be saved.

    Returns:
        str: Path of the enlarged output image.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Load the input image
    try:
        img = Image.open(image_path)
    except Exception as e:
        raise ValueError(f"Error opening image: {e}")

    # Get original size
    width, height = img.size

    # Double the size (2x enlargement)
    enlarged_img = img.resize((width * 2, height * 2), Image.NEAREST)

    # Define output file name
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_path = os.path.join(output_dir, f"{base_name}_enlarged.png")

    # Save enlarged image
    enlarged_img.save(output_path)

    print(f"✅ Enlarged image saved: {output_path}")
    return output_path


def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(description="Enlarge an image by 2x.")
    parser.add_argument("image_path", help="Path to the input image")
    parser.add_argument("output_dir", help="Directory to save the enlarged image")

    args = parser.parse_args()
    enlarge(args.image_path, args.output_dir)


if __name__ == "__main__":
    main()
