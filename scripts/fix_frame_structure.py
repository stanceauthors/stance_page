#!/usr/bin/env python3
"""
Script to fix all first frame structures to have consistent "image above, label below" format
"""

import re

def fix_frame_structures():
    """Fix all first frame structures"""
    
    # Read the HTML file
    with open('Desktop/Study/STANCE/STANCE_page/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern 1: Fix structures where first-frame-placeholder is followed by frame-label (not wrapped in video-container-small)
    pattern1 = r'(<div class="video-container-with-frame">\s*)<div class="first-frame-placeholder">\s*<img src="([^"]*)" alt="First Frame" />\s*</div>\s*<div class="frame-label">Initial condition</div>\s*(<div class="video-container-small">)'
    
    def replacement1(match):
        prefix = match.group(1)
        img_src = match.group(2)
        video_container = match.group(3)
        
        new_structure = f"""{prefix}<div class="video-container-small">
                                    <div class="first-frame-placeholder">
                                        <img src="{img_src}" alt="First Frame" />
                                    </div>
                                    <div class="video-label">Initial condition</div>
                                </div>
                                {video_container}"""
        return new_structure
    
    # Apply first pattern
    content = re.sub(pattern1, replacement1, content, flags=re.MULTILINE | re.DOTALL)
    
    # Pattern 2: Fix Real World Captures structure (slightly different)
    pattern2 = r'(<div class="video-container-with-frame">\s*)<div class="first-frame-placeholder">\s*<img src="([^"]*)" alt="First Frame" />\s*</div>\s*<div class="frame-label">Initial condition</div>\s*(<div class="video-container-small">\s*<video)'
    
    def replacement2(match):
        prefix = match.group(1)
        img_src = match.group(2)
        video_part = match.group(3)
        
        new_structure = f"""{prefix}<div class="video-container-small">
                            <div class="first-frame-placeholder">
                                <img src="{img_src}" alt="First Frame" />
                            </div>
                            <div class="video-label">Initial condition</div>
                        </div>
                        {video_part}"""
        return new_structure
    
    # Apply second pattern
    content = re.sub(pattern2, replacement2, content, flags=re.MULTILINE | re.DOTALL)
    
    # Pattern 3: Fix Comparison section structure (different layout)
    pattern3 = r'(<div class="video-container-small">\s*)<div class="first-frame-placeholder">\s*<img src="([^"]*)" alt="First Frame" />\s*</div>\s*<div class="frame-label">Initial condition</div>\s*(<div class="video-label">First Frame</div>)'
    
    def replacement3(match):
        prefix = match.group(1)
        img_src = match.group(2)
        video_label = match.group(3)
        
        new_structure = f"""{prefix}<div class="first-frame-placeholder">
                                <img src="{img_src}" alt="First Frame" />
                            </div>
                            <div class="video-label">Initial condition</div>
                        </div>
                        <div class="video-container-small">
                            <video controls loop muted>
                                <source src="./assets/comparison_video/case_1/our_1.mp4" type="video/mp4">
                            </video>
                            {video_label}"""
        return new_structure
    
    # Don't apply pattern3 as it's too risky, handle comparison manually
    
    # Write back to file
    with open('Desktop/Study/STANCE/STANCE_page/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed first frame structures!")

if __name__ == "__main__":
    fix_frame_structures() 