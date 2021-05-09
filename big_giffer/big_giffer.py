import argparse
import json
import os
import pprint # for debugging
import sys
import subprocess

PROBE = 'ffprobe'
MPEG  = 'ffmpeg'
REQUIRED_PROGRAMS = (
    PROBE,
    MPEG,
)

PROBE_CMD = '{} -v quiet -print_format json -show_streams'.format(PROBE)

OUTPUT_DIR_NAME = 'output_gifs'
DEFAULT_ASPECT_RATIO = 16/9
OUTPUT_LONG_EDGE_SIZE = 640
DEFAULT_INPUT_FORMAT = 'mp4'
OUTPUT_FORMAT = 'gif'


if __name__ == '__main__':

    # TODO: Add an argparse. Some arguments:
    # TODO: Overwrite files y/n. Y by default
    # TODO: Output file location/name. Default is just video_dir/OUTPUT_DIR_NAME
    # TODO: Fail if dir already exists. Default False
    # TODO: Maybe a long-edge pixel size option?
    # TODO: Maybe an aspect ratio option?
    # TODO: File in type?

    # Check that the necessary programs are installed
    for program in (PROBE, MPEG):
        if len(subprocess.run(['which', program], capture_output=True).stdout) <= 0:
            print('{} must be installed before use!'.format(PROBE))
            sys.exit(1)

    # TODO: Get some argparse up in this
    vid_dir = sys.argv[1]
    aspect_ratio = DEFAULT_ASPECT_RATIO
    skip_existing_files = False

    # Check video directory is LEGIT
    if not (os.path.exists(vid_dir) and os.path.isdir(vid_dir)):
        print('{} is not a valid directory!'.format(vid_dir))
        sys.exit(1)

    # Get list of files in video directory
    vid_files = [''.join([vid_dir,file]) for file in os.listdir(vid_dir) if os.path.isfile(os.path.join(vid_dir, file))]

    # Make the output file
    output_dir = os.path.join(vid_dir, OUTPUT_DIR_NAME) 
    try:
        os.mkdir(output_dir)
    except FileExistsError:
        # TODO: If an argument is created to check for overwrite, check it here
        pass
    except Exception as e:
        print('Could not make output directory: {}'.format(e))
        sys.exit(1)


    # Do the conversion
    for vid_file in vid_files:
        vid_file_name = os.path.basename(vid_file)
        
        # Craft new file name, see if file already exists
        # Goal here is to replace input format with output format if input is in the name
        # If not, just append the output format to the end
        output_file_name = vid_file_name[:-3] + OUTPUT_FORMAT if vid_file_name[-4:] == ('.' + DEFAULT_INPUT_FORMAT) else vid_file_name + '.' + OUTPUT_FORMAT
        output_file = os.path.join(output_dir, output_file_name)
        if skip_existing_files and os.path.isfile(output_file):
            print('Output file {} already exists. Skipping...'.format(output_file_name))

        # Use the probe command to get required video data in json form
        vid_data_cmd = PROBE_CMD.split() + [vid_file,]
        vid_data_json = subprocess.run(vid_data_cmd, capture_output=True).stdout
        
        # subprocess.run produces a weird output format, so fix it and parse!
        vid_data_dict = json.loads(vid_data_json.decode('utf-8'))

        # This looks weird as heck but it's how probe cmd JSONs it's data so ¯\_(ツ)_/¯
        try:
            #pprint.pprint(orientationer_json['streams'][1]
            rotated = 'rotate' in vid_data_dict['streams'][1]['tags']
            frame_rate = round(eval(vid_data_dict['streams'][1]['avg_frame_rate']))
            width = vid_data_dict['streams'][1]['width']
            height = vid_data_dict['streams'][1]['height']
        except IndexError as e:
            print('{} has too few of streams. Is it the right file type? Skipping...'.format(vid_file_name))
            continue
        except KeyError as e:
            print('{} Is missing information "{}". Skipping...'.format(vid_file_name, e))
            continue

        # Might not need this but can't hurt
        if width/height != aspect_ratio: 
            print('Error parsing {}: actual aspect ratio {} does not match stated {}.'
                'Skipping...'.format(os.path.basename(vid_file), height/width, aspect_ratio))
            continue
        
        # Compose the conversion call
        ffmpeg_call = '{} -y -loglevel quiet -i {} -r {} -vf "scale={}" -loop 0 {}'.format(
            MPEG,
            vid_file,
            frame_rate,
            '-1:{}'.format(OUTPUT_LONG_EDGE_SIZE) if rotated else '{}:-1'.format(OUTPUT_LONG_EDGE_SIZE),
            output_file
        )

        # Run it!
        try:
            print('Processing {} --> {}...'.format(vid_file_name, output_file_name))
            subprocess.run(ffmpeg_call, check=True, capture_output=True, shell=True)
        except subprocess.CalledProcessError as e:
            print('Converter call for {} failed with "{}". Skipping...'.format(output_file_name, e.stderr))
            if os.path.isfile(output_file):
                os.remove(output_file)
            continue


    print('All done!')



