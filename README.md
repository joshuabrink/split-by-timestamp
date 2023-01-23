# Audio/Video Timestamp Splitter
This is a simple script that splits a video file into multiple files based on a list of timestamps. 

## Usage
`python split.py --input_file <input> --output_file <output_file> --timestamps_file <timestamps_file>`

## Example
```txt  
# timestamps.txt
00:00:00 File 1 Title
00:00:30 File 2 Title
00:01:00 File 3 Title
...
```

`python split.py --input_file input.mp4 --output_file output.mp4 --timestamps_file timestamps.txt`