from PIL import Image, ImageEnhance

# Function to apply color blindness simulation
def simulate_color_blindness(image_path, mode='deuteranopia'):
    """
    Simulate how an image looks to someone with color blindness.

    Parameters:
    - image_path: str, path to the input image.
    - mode: str, type of color blindness ('deuteranopia', 'protanopia', or 'tritanopia').

    Returns:
    - PIL.Image object of the modified image.
    """
    # Open the image
    img = Image.open(image_path).convert('RGB')
    
    # Get image data
    pixels = img.load()
    
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]

            if mode == 'deuteranopia':  # Green deficiency
                r, g, b = int(r * 0.625 + g * 0.375), int(r * 0.7 + g * 0.3), b
            elif mode == 'protanopia':  # Red deficiency
                r, g, b = int(r * 0.567 + g * 0.433), int(r * 0.558 + g * 0.442), b
            elif mode == 'tritanopia':  # Blue deficiency
                r, g, b = r, int(g * 0.95 + b * 0.05), int(g * 0.433 + b * 0.567)
            else:
                raise ValueError("Unsupported mode. Choose 'deuteranopia', 'protanopia', or 'tritanopia'.")

            # Set new pixel values
            pixels[i, j] = (r, g, b)
    
    return img

# Enhance contrast for better accessibility
def enhance_contrast(image, factor=1.5):
    """
    Enhance the contrast of the image.

    Parameters:
    - image: PIL.Image object
    - factor: float, factor to adjust contrast. Default is 1.5.

    Returns:
    - Enhanced PIL.Image object.
    """
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

# Example usage
if __name__ == '__main__':
    input_image = "example.jpg"  # Replace with your image path
    output_mode = 'deuteranopia'  # Choose between 'deuteranopia', 'protanopia', or 'tritanopia'

    # Simulate color blindness
    simulated_image = simulate_color_blindness(input_image, mode=output_mode)
    
    # Enhance contrast for accessibility
    enhanced_image = enhance_contrast(simulated_image)

    # Save the result
    enhanced_image.save(f"output_{output_mode}.jpg")
    print(f"Processed image saved as output_{output_mode}.jpg")
