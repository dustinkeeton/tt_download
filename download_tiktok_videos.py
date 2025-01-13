import json
import subprocess
from pathlib import Path
import time
import sys
import argparse

def download_tiktok_video(url, output_dir, video_id, list_type):
    try:
        output_template = f"{output_dir}/{list_type}_tiktok_{video_id}.%(ext)s"
        command = [
            "yt-dlp",
            "--no-warnings",
            "-o", output_template,
            url
        ]
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"Failed to download: {url}")
        return False

def process_video_list(videos, output_dir, list_type, start_index=0, total_videos=None):
    if not videos:
        print(f"No videos found in {list_type}")
        return start_index

    current_index = start_index
    list_total = len(videos)
    
    for video in videos:
        current_index += 1
        url = video["Link"]
        video_id = url.rstrip('/').split('/')[-1]
        
        print(f"[{current_index}/{total_videos}] Downloading {list_type} video {video_id}")
        
        # Check if video already exists
        existing_files = list(output_dir.glob(f"{list_type}_tiktok_{video_id}.*"))
        if existing_files:
            print(f"Video {video_id} already exists, skipping...")
            continue

        success = download_tiktok_video(url, output_dir, video_id, list_type)
        
        # Add a small delay between downloads to avoid rate limiting
        if success:
            time.sleep(1)
    
    return current_index

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Download TikTok videos from data export')
    parser.add_argument('json_file', type=str, help='Path to the TikTok data export JSON file')
    parser.add_argument('output_dir', type=str, help='Path to save the downloaded videos')
    
    args = parser.parse_args()

    # Convert paths to Path objects
    json_path = Path(args.json_file)
    output_dir = Path(args.output_dir)

    # Validate input file exists
    if not json_path.exists():
        print(f"Error: JSON file not found at {json_path}")
        sys.exit(1)

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Read the JSON file
    with open(json_path, 'r') as f:
        data = json.load(f)

    # Get both Favorite and Like lists
    favorite_videos = data["Activity"]["Favorite Videos"].get("FavoriteVideoList", [])
    liked_videos = data["Activity"]["Like List"].get("ItemFavoriteList", [])
    
    total_videos = len(favorite_videos) + len(liked_videos)
    print(f"Found {len(favorite_videos)} favorite videos and {len(liked_videos)} liked videos")
    print(f"Total videos to download: {total_videos}")
    print(f"Saving to: {output_dir}")

    # Process favorite videos first
    current_index = process_video_list(
        favorite_videos, 
        output_dir, 
        "favorite",
        start_index=0,
        total_videos=total_videos
    )

    # Then process liked videos
    process_video_list(
        liked_videos, 
        output_dir, 
        "liked",
        start_index=current_index,
        total_videos=total_videos
    )

    print("Download complete!")

if __name__ == "__main__":
    main()