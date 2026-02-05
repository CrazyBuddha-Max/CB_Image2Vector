import os

import vtracer


def convert_png_to_svg(input_filename: str, output_filename: str) -> None:
    print("--------Vector Graphics Conversion System Started--------")
    if not os.path.exists(input_filename):
        print(f"Error: File not found '{input_filename}'")
        return

    print(f"Starting the underlying conversion interface, processing '{input_filename}'...")

    try:
    
        vtracer.convert_image_to_svg_py(
            input_filename,
            output_filename,
            colormode="color",  # Keep color
            mode="spline",  # Smooth curve
            filter_speckle=4,  # Filter out noise
            color_precision=6,  # Color accuracy
        )

        if os.path.exists(output_filename):
            print("-" * 30)
            print("Conversion successful!")
            print(f"Generate file: {os.path.abspath(output_filename)}")
            print("-" * 30)

    except Exception as e:
        print(fConversion failed: {e}")
        print("\nTry a simpler way to call it...")
        try:
            vtracer.convert_image_to_svg_py(input_filename, output_filename)
            print("Simplified call conversion successful!")
        except Exception as e2:
            print(f"The ultimate attempt also failed: {e2}")
    print("--------Vector image conversion system is off--------")


if __name__ == "__main__":
    convert_png_to_svg("cpu.png", "cpu.svg")
