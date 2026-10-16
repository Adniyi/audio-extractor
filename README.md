# Audio Extractor

A simple Python script to extract audio from video files using [MoviePy](https://zulko.github.io/moviepy/).

## Features

- Extract audio from video files and save as MP3
- Supports both positional arguments and flags for input/output paths
- Lightweight CLI tool with minimal dependencies

## Installation

### Prerequisites

- Python 3.10+
- [MoviePy](https://zulko.github.io/moviepy/)

Install dependencies:

```bash
pip install moviepy
```

### Setup

Clone or download this repository:

```bash
git clone <repository-url>
cd audio_extractor
```

## Usage

Run the script from the command line:

```bash
py audio_extractor.py -i "Path\to\input\<file>.<extension>" -o "Path\to\output\<output_filename>.<extension>"
```

Or using positional arguments (input first, then output):

```bash
py audio_extractor.py "Path\to\input\<file>.<extension>" "Path\to\output\<output_filename>.<extension>"
```

### Arguments

| Argument          | Flag             | Description                    |
| ----------------- | ---------------- | ------------------------------ |
| `input_position`  | `-i`, `--input`  | Path to the input video file   |
| `output_position` | `-o`, `--output` | Path for the output audio file |

You can mix positional arguments and flags. Flags take precedence when both are provided.

### Examples

Extract audio from a video file:

```bash
py audio_extractor.py -i "C:\Videos\vacation.mp4" -o "C:\Audio\vacation.mp3"
```

Using positional arguments:

```bash
py audio_extractor.py "C:\Videos\vacation.mp4" "C:\Audio\vacation.mp3"
```

Mixed usage:

```bash
py audio_extractor.py -o "C:\Audio\vacation.mp3" -i "C:\Videos\vacation.mp4"
```

## How It Works

1. Loads the video file using `moviepy.VideoFileClip`
2. Extracts the audio track and writes it to an MP3 file
3. Releases video resources after extraction

## Requirements

- Python 3.x
- moviepy

Install all requirements:

```bash
pip install moviepy
```

## License

This project is licensed under the terms in the [LICENSE](LICENSE) file.
