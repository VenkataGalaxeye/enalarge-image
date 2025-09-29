import os
from PIL import Image
import argparse

def enlarge(image_path: str, output_dir: str = "output"):
    """
    Takes one image as input and saves two identical copies of it.

    Args:
        image_path (str): Path to the input image.
        output_dir (str): Directory where the copies will be saved.

    Returns:
        list: Paths of the two output images.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Load the input image
    try:
        img = Image.open(image_path)
    except Exception as e:
        raise ValueError(f"Error opening image: {e}")

    # Define output file names
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    copy1_path = os.path.join(output_dir, f"{base_name}_copy1.png")
    copy2_path = os.path.join(output_dir, f"{base_name}_copy2.png")

    # Save two copies
    img.save(copy1_path)
    img.save(copy2_path)

    print(f"✅ Two copies saved: {copy1_path}, {copy2_path}")
    return [copy1_path, copy2_path]


def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Duplicate an image into two identical copies."
    )
    parser.add_argument("image_path", help="Path to the input image")
    parser.add_argument("output_dir", help="Directory to save the copies")

    args = parser.parse_args()
    enlarge(args.image_path, args.output_dir)
