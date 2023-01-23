import os
import subprocess
import argparse
import re

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)


def cut_by_timestamp(input_file, start_time, end_time, output_file):
    # ffmpeg -ss 00:00:00 -i input.mp4 -t 00:00:10 -c copy output.mp4
    if end_time == 0:
        subprocess.run(
            ['ffmpeg', '-ss', start_time, '-i', input_file, '-c', 'copy', output_file])
    else:
        subprocess.run(['ffmpeg', '-ss', start_time, '-i',
                        input_file, '-t', end_time, '-c', 'copy', output_file])


def main():
    parser = argparse.ArgumentParser(
        description='Cut audio/video by timestamp')
    parser.add_argument('--input_file', help='input file',
                        default="dwarf.opus")
    parser.add_argument('--start_time', help='start time', default="")
    parser.add_argument('--end_time', help='end time', default="")
    parser.add_argument('--output_file', help='output file', default="")
    parser.add_argument('--timestamps_file',
                        help='timestamps file', default="dwarf_text.txt")
    args = parser.parse_args()

    if args.timestamps_file:
        with open(args.timestamps_file) as f:
            lines = f.readlines()
            start_time = 0
            for index, line in enumerate(lines):
                _, output_file = re.match(
                    r'(\d?\d?:?\d?\d:\d\d) (.*)', line).groups()

                # convert start_time to seconds

                # peek at next line to get end_time
                next_line = lines[index + 1] if index + \
                    1 < len(lines) else None
                if next_line:
                    end_time, _ = re.match(
                        r'(\d?\d?:?\d?\d:\d\d) (.*)', next_line).groups()

                    # convert end_time to seconds
                    end_time_array = end_time.split(':')[::-1]
                    end_time = sum(60 ** i * int(x) if i > 0 else int(x)
                                   for i, x in enumerate(end_time_array))
                    cut_by_timestamp(args.input_file, str(start_time),
                                     str(end_time - start_time), str(index + 1) + ". " + output_file + ".opus")
                else:
                    cut_by_timestamp(args.input_file, str(start_time),
                                     0, str(index + 1) + ". " + output_file + ".opus")

                start_time = end_time
    else:
        cut_by_timestamp(args.input_file, args.start_time,
                         args.end_time, args.output_file)


if __name__ == '__main__':
    main()
