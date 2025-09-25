#!/usr/bin/env python3
"""
Script to batch update remaining first frame placeholders
"""

def batch_update():
    """Update remaining placeholders"""
    with open('Desktop/Study/STANCE/STANCE_page/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace remaining placeholders
    replacements = [
        # STANCE Showcase - Composite Scenes continued (16-24)
        ('tmp_59cab502_4_142b6527.mp4', './assets/first_frame/stance_showcase/16.png'),
        ('tmp_65cb3c85_4_5291d291.mp4', './assets/first_frame/stance_showcase/17.png'),
        ('tmp_65cb3c85_0_6b8a4043.mp4', './assets/first_frame/stance_showcase/18.png'),
        ('tmp_6cbdc52e_5_00761c16.mp4', './assets/first_frame/stance_showcase/19.png'),
        ('tmp_6cbdc52e_3_d223f6a6.mp4', './assets/first_frame/stance_showcase/20.png'),
        ('tmp_4c34f81c_4_2686137b.mp4', './assets/first_frame/stance_showcase/21.png'),
        ('tmp_4c34f81c_3_e96c6d9b.mp4', './assets/first_frame/stance_showcase/22.png'),
        ('tmp_35797f71_3_92230724.mp4', './assets/first_frame/stance_showcase/23.png'),
        ('tmp_35797f71_1_c6707bc1.mp4', './assets/first_frame/stance_showcase/24.png'),
        
        # Real World Captures (real_1 to real_4)
        ('validation-55400-0-0_bottom_right.mp4', './assets/first_frame/real_capture/real_1.png'),
        ('validation-55400-1-1_bottom_right.mp4', './assets/first_frame/real_capture/real_2.png'),
        ('validation-55400-2-2_bottom_right.mp4', './assets/first_frame/real_capture/real_3.png'),
        ('validation-55400-3-3_bottom_right.mp4', './assets/first_frame/real_capture/real_4.png'),
        
        # Comparison (1.png to 3.png)
        ('case_1/our_1.mp4', './assets/first_frame/comparison/1.png'),
        ('case_2/our_2.mp4', './assets/first_frame/comparison/2.png'),
        ('case_3/our_3.mp4', './assets/first_frame/comparison/3.png'),
    ]
    
    for video_file, image_path in replacements:
        # Find the placeholder before this video
        pattern = f'<div class="first-frame-placeholder">\\s*<!-- First frame image will be added here -->\\s*<div class="placeholder-text">First Frame</div>\\s*</div>\\s*<div class="video-container-small">\\s*<video[^>]*>\\s*<source src="[^"]*{video_file}"'
        import re
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        if match:
            old_placeholder = re.search(r'<div class="first-frame-placeholder">.*?</div>', match.group(0), re.DOTALL).group(0)
            new_placeholder = f'<div class="first-frame-placeholder">\n                                    <img src="{image_path}" alt="First Frame" />\n                                </div>'
            content = content.replace(old_placeholder, new_placeholder)
            print(f"Updated placeholder for {video_file} -> {image_path}")
        else:
            print(f"Could not find placeholder for {video_file}")
    
    # Write back
    with open('Desktop/Study/STANCE/STANCE_page/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Batch update completed!")

if __name__ == "__main__":
    batch_update() 