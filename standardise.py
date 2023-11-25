import os, sys
from PIL import Image
HELP_MESSAGE = """You must provide an input directory and an output directory with image size
For example python standardise.py textures/ export/ 128 128
"""
def resize_images(input_directory, output_directory, output_size=(128, 128)):
    if not (os.path.exists(input_directory) or os.path.exists(output_directory)):
        print(f"Directory '{input_directory}' does not exist.")
        return False

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            try:
                # Open the image
                with Image.open(os.path.join(input_directory, filename)) as img:
                    # Resize the image
                    img = img.resize(output_size)

                    # Construct the output filename
                    output_filename = os.path.splitext(filename)[0] + "_resized.png"

                    # Save the resized image
                    img.save(os.path.join(output_directory, output_filename), 'PNG')

                    print(f"Resized and saved {output_filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return True


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(HELP_MESSAGE)
        exit(1)

    if not all([x.isdigit() for x in sys.argv[3:4]]):
        print(HELP_MESSAGE)
        exit(1)
    
    if not resize_images(sys.argv[1], sys.argv[2],(int(sys.argv[3]), int(sys.argv[4]))):
        exit(1)