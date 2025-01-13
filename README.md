# TikTok Data Export Video Downloader

A Python script to download videos from your TikTok data export, including both favorite and liked videos.

## Description

This tool helps you download videos from your TikTok data export JSON file. It automatically handles both favorite and liked videos, saves them with organized filenames, and includes features like:

- Duplicate video detection
- Progress tracking
- Rate limiting protection
- Organized output directory structure

## Prerequisites

- Python 3.6+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (will need to be installed separately)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/tiktok-data-export-downloader.git
cd tiktok-data-export-downloader
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
``` 

3. Install yt-dlp:

```bash
pip install yt-dlp
```

## Usage

1. Request your TikTok data export from TikTok settings
2. Wait for TikTok to email you the data export or find it on your settings page (can take several days)
3. Extract the received ZIP file
4. Run the script:

```bash
python download_tiktok_videos.py json_file output_dir
```

### Positional Arguments

- `json_file`: Path to your TikTok JSON file
- `output_dir`: Directory where videos will be saved

### Command Line Arguments

- `--help`: Show help for command line arguments

## File Organization

Downloaded videos are organized in the following structure:
```
output_dir/
├── favorite_tiktok_{video_id}.*
└── liked_tiktok_{video_id}.*
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for video downloading capabilities
- TikTok for providing data export functionality

## Disclaimer

This tool is for personal use only. Please respect TikTok's terms of service and only download content you have proper access to.

