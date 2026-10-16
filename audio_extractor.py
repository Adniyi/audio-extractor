import argparse
import os
from moviepy import VideoFileClip 


# Note: This is how to use the tool.
# py audio_extractor.py -i "Path\to\input\<file>.<extension>" -o "Path\to\output\<output_filename>.<extension>" 
# or
# py audio_extractor.py -o "Path\to\output\<output_filename>.<extension>" -i "Path\to\input\<file>.<extension>"

def extract_audio(video_file_path: str, audio_file_path: str):
    # Load the video
    video = VideoFileClip(video_file_path)

    # Extract Audio from video file
    try:
        video.audio.write_audiofile(audio_file_path, codec="mp3") 
        print(f"Audio file succesfully extracted to: {audio_file_path}")
        
        # Close up resources
        video.close()

    except Exception as e:
        print(f"Error: Failed to extract audio from file: {e}")



def main():
    parser = argparse.ArgumentParser("Audio Extractor from Video files")
    
    # This is an implementation that supports my needs
    # When extracting audio file, one can either pass the file location(Path) as a positional argument or by using flags
    # This implementation supports both positions and flags
    # You either pass the Input and Output path(in that order) as arguments or you use flags. 
    
    # First implementation: Positional Arguments
    parser.add_argument("input_position", nargs="?", help= "Input file location (Path)")
    parser.add_argument("output_position", nargs="?", help= "Output file location (Path)")

    # Second implementation: Flags
    parser.add_argument("-i", "--input", help="Input file loaction (flag)")
    parser.add_argument("-o", "--output", help="Ouput file location (flag)")

    args = parser.parse_args()

    # Logic to decide which variable to use (Positions or Flags)
    final_input = args.input_position or args.input
    final_output = args.output_position or args.output

    if not final_input or not final_output:
        print("Error: Please provide both an Input and Output file.")
        return 
    
    extract_audio(final_input, final_output)


if __name__ == "__main__":
    main()
