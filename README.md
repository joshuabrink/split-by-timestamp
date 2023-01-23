# Audio/Video Timestamp Splitter
This is a simple script that splits a video file into multiple files based on a list of timestamps. 

## Requirements
- Python 3
- ffmpeg

## Usage
`python split.py --input_file <input> --timestamps_file <timestamps_file>`

## Example

### Input
Timestamps file:
```txt  
# timestamps.txt
00:00:00 File 1 Title
00:00:30 File 2 Title
00:01:00 File 3 Title
...
```
`python split.py --input_file input.opus --timestamps_file timestamps.txt`

### Output
```bash
ls
File 1 Title.opus
File 2 Title.opus
File 3 Title.opus
...
```