import os
from PIL import Image
import sys
sys.stdout.reconfigure(encoding="utf-8")


# Folder paths (relative to this script's directory)
base_dir = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(base_dir, "input_images")
output_folder = os.path.join(base_dir, "output_images")

# Resize dimensions
new_width = 800
new_height = 600

# Create output folder if not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Supported formats
valid_extensions = (".jpg", ".jpeg", ".png", ".jfif")

# Ensure input folder exists
if not os.path.isdir(input_folder):
    raise FileNotFoundError(
        f"Input folder not found: {input_folder}. "
        "Create it and add images, or run the script from the image_resizer folder."
    )

# Process images
for filename in os.listdir(input_folder):
    if filename.lower().endswith(valid_extensions):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path) as img:
                # Resize image
                resized_img = img.resize((new_width, new_height))

                # Save resized image
                resized_img.save(output_path)
                print(f"Resized: {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

print(" All images processed!")
