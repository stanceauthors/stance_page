#!/usr/bin/env python3
"""
Extract first frames from videos in the qualitative_video directory
"""

import cv2
import os
from pathlib import Path


def extract_first_frame(video_path, output_path):
    """Extract the first frame from a video and save as image."""
    cap = cv2.VideoCapture(str(video_path))
    
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return False
    
    # Read the first frame
    ret, frame = cap.read()
    
    if not ret:
        print(f"Error: Could not read frame from {video_path}")
        cap.release()
        return False
    
    # Save the frame
    success = cv2.imwrite(str(output_path), frame)
    cap.release()
    
    if success:
        print(f"Extracted first frame: {output_path}")
        return True
    else:
        print(f"Error: Could not save frame to {output_path}")
        return False


def process_directory():
    """Process all video directories and extract first frames."""
    base_dir = Path("./assets/qualitative_video")
    
    if not base_dir.exists():
        print(f"Error: Directory {base_dir} does not exist")
        return
    
    # Process vary directory
    vary_dir = base_dir / "vary"
    if vary_dir.exists():
        for subdir in sorted(vary_dir.iterdir()):
            if subdir.is_dir():
                # Find first video file in the subdirectory
                video_files = list(subdir.glob("*.mp4"))
                if video_files:
                    video_file = video_files[0]  # Take the first video
                    output_path = subdir / "first_frame.jpg"
                    extract_first_frame(video_file, output_path)
    
    # Process multi_obj directory
    multi_obj_dir = base_dir / "multi_obj"
    if multi_obj_dir.exists():
        video_files = list(multi_obj_dir.glob("*.mp4"))
        for i, video_file in enumerate(sorted(video_files)):
            output_path = multi_obj_dir / f"first_frame_{i+1}.jpg"
            extract_first_frame(video_file, output_path)
    
    # Process realistic_case directory
    realistic_case_dir = base_dir / "realistic_case"
    if realistic_case_dir.exists():
        for subdir in sorted(realistic_case_dir.iterdir()):
            if subdir.is_dir():
                # Find first video file in the subdirectory
                video_files = list(subdir.glob("*.mp4"))
                if video_files:
                    video_file = video_files[0]  # Take the first video
                    output_path = subdir / "first_frame.jpg"
                    extract_first_frame(video_file, output_path)


if __name__ == "__main__":
    process_directory()
    print("First frame extraction complete!") 