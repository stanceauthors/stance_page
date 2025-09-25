#!/usr/bin/env python3
"""
Script to add "Initial condition" labels to all first frame placeholders
"""

import re

def add_frame_labels():
    """Add frame labels to all first frame placeholders"""
    
    # Read the HTML file
    with open('Desktop/Study/STANCE/STANCE_page/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match first-frame-placeholder divs with images (but no frame-label yet)
    pattern = r'(<div class="first-frame-placeholder">\s*<img src="[^"]*" alt="First Frame" />\s*</div>)\s*(<div class="video-container-small">)'
    
    # Replace with the same content plus frame label
    def replacement(match):
        placeholder_div = match.group(1)
        video_container = match.group(2)
        frame_label = '\n                                <div class="frame-label">Initial condition</div>\n                                '
        return placeholder_div + frame_label + video_container
    
    # Apply replacements
    new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE | re.DOTALL)
    
    # Also handle comparison cases where the structure is slightly different
    comparison_pattern = r'(<div class="first-frame-placeholder">\s*<img src="[^"]*" alt="First Frame" />\s*</div>)\s*(<div class="video-label">First Frame</div>)'
    
    def comparison_replacement(match):
        placeholder_div = match.group(1)
        video_label = match.group(2)
        frame_label = '\n                            <div class="frame-label">Initial condition</div>\n                            '
        return placeholder_div + frame_label + video_label
    
    new_content = re.sub(comparison_pattern, comparison_replacement, new_content, flags=re.MULTILINE | re.DOTALL)
    
    # Write back to file
    with open('Desktop/Study/STANCE/STANCE_page/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Added frame labels to all first frame placeholders!")

if __name__ == "__main__":
    add_frame_labels() 