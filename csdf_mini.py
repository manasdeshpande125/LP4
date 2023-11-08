'''from PIL import Image
import exifread


def analyze_image(image_path):
    try:
        # Open the image using Pillow
        with Image.open(image_path) as img:
            # Get basic image information
            image_info = {
                "Width": img.width,
                "Height": img.height,
                "Format": img.format,
                "Mode": img.mode
            }
            print("Basic Image Information:")
            print(image_info)

            # Extract EXIF metadata using exifread
            with open(image_path, "rb") as f:
                tags = exifread.process_file(f)
                print("\nEXIF Metadata:")
                for tag, value in tags.items():
                    print(f"{tag}: {value}")

    except Exception as e:
        print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    image_path = input("D:\Mobile\Camera\20201129_140004_01.jpg")
    analyze_image(image_path)




steganography detection, metadata analysis, error level analysis, histogram analysis,EXIF metadata
'''
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image, ImageChops,ImageEnhance 
import matplotlib.pyplot as plt
import numpy as np

def extract_exif_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data is not None:
                metadata = {}
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    metadata[tag_name] = value
                return metadata
            else:
                return None
    except Exception as e:
        print("Error:", e)
        return None
    



def error_level_analysis(image_path, save_path):
    original = Image.open(image_path)
    scale = 10
    ela_image = ImageChops.difference(original, original.resize((scale, scale), Image.LANCZOS))
    extrema = ela_image.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff
    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)
    ela_image.save(save_path)


def plot_histogram(image_path):
    image = Image.open(image_path)
    r, g, b = image.split()

    r_histogram = np.array(r.histogram(), dtype=float)
    g_histogram = np.array(g.histogram(), dtype=float)
    b_histogram = np.array(b.histogram(), dtype=float)

    plt.figure(figsize=(8, 6))
    plt.title('Histogram Analysis')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.plot(r_histogram, color='red', label='Red', alpha=0.7)
    plt.plot(g_histogram, color='green', label='Green', alpha=0.7)
    plt.plot(b_histogram, color='blue', label='Blue', alpha=0.7)
    plt.legend()
    plt.show()



def main():
    image_path = r"D:\ManasPICT2\7th Sem\Camera\20231018_170824.jpg"  # Replace this with the path to your image file
    metadata = extract_exif_metadata(image_path)
    
    if metadata is not None:
        print("EXIF and Metadata Information:")
        for tag, value in metadata.items():
            print(f"{tag}: {value}")
    else:
        print("No EXIF data found.")


    # Example usage
    #input_image_path = r"D:\ManasPICT2\7th Sem\Camera\20231018_170824.jpg"  # Replace with the path to your input image
    ela_output_path = "ela_output.jpg"  # Replace with the desired output path for ELA image
    error_level_analysis(image_path, ela_output_path)

    plot_histogram(image_path)

if __name__ == "__main__":
    main()
