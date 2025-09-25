#!/usr/bin/env python3
"""
Script to update all first frame placeholders in index.html with actual images
"""

import re

def update_first_frames():
    """Update all first frame placeholders with actual image paths"""
    
    # Read the HTML file
    with open('Desktop/Study/STANCE/STANCE_page/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Define the mapping of placeholders to images
    # STANCE Showcase: 24 images (1.png to 24.png)
    # Real World Captures: 4 images (real_1.png to real_4.png)  
    # Comparison: 3 images (1.png to 3.png)
    
    stance_showcase_images = [f"./assets/first_frame/stance_showcase/{i}.png" for i in range(1, 25)]
    real_capture_images = [f"./assets/first_frame/real_capture/real_{i}.png" for i in range(1, 5)]
    comparison_images = [f"./assets/first_frame/comparison/{i}.png" for i in range(1, 4)]
    
    # All images in order
    all_images = stance_showcase_images + real_capture_images + comparison_images
    
    # Pattern to match first-frame-placeholder divs
    placeholder_pattern = r'<div class="first-frame-placeholder">\s*<!-- First frame image will be added here -->\s*<div class="placeholder-text">First Frame</div>\s*</div>'
    
    # Find all placeholders
    placeholders = list(re.finditer(placeholder_pattern, html_content, re.MULTILINE | re.DOTALL))
    
    print(f"Found {len(placeholders)} placeholders")
    print(f"Have {len(all_images)} images")
    
    if len(placeholders) != len(all_images):
        print("Warning: Number of placeholders doesn't match number of images!")
        return False
    
    # Replace placeholders from end to start (to maintain correct positions)
    for i in range(len(placeholders) - 1, -1, -1):
        match = placeholders[i]
        image_path = all_images[i]
        
        # Create new div with image
        new_placeholder = f'<div class="first-frame-placeholder">\n                                    <img src="{image_path}" alt="First Frame" />\n                                </div>'
        
        # Replace in content
        html_content = html_content[:match.start()] + new_placeholder + html_content[match.end():]
        
        print(f"Updated placeholder {i+1}: {image_path}")
    
    # Write back to file
    with open('Desktop/Study/STANCE/STANCE_page/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("All first frame placeholders updated successfully!")
    return True

if __name__ == "__main__":
    update_first_frames() 