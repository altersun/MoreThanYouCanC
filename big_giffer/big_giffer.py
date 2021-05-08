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
OUTPUT_LONG_EDGE_SIZE = 480
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
        print('{} is not a valide directory!'.format(vid_dir))
        sys.exit(1)

    # Get list of files in video directory
    vid_files = [''.join([vid_dir,file]) for file in os.listdir(vid_dir) if os.path.isfile(os.path.join(vid_dir, file))]

    # Make the output file
    try:
        output_dir = os.mkdir(os.path.join(vid_dir, OUTPUT_DIR_NAME))
    except FileExistsError:
        # TODO: If an argument is created to check for overwrite, check it here
        pass
    except Exception as e:
        print('Could not make output directory: {}'.format(e))
        sys.exit(1)


    # Do the conversion
    for vid_file in vid_files:
        
        # Craft new file name, see if file already exists
        # Goal here is to replace input format with output format if input is in the name
        # If not, just append the output format to the end
        output_file_name = vid_file[:-3] + OUTPUT_FORMAT if vid_file[-4:] == ('.' + DEFAULT_INPUT_FORMAT) else vid_file + '.' + OUTPUT_FORMAT
        output_file = output_dir + output_file_name
        if skip_existing_files and os.path.isfile(output_file):
            print('Output file {} already exists. Skipping...'.format(output_file_name))

        # Use the probe command to get required video data in json form
        vid_data_cmd = PROBE_CMD.split() + [vid_file,]
        vid_data_json = subprocess.run(vid_data_cmd, capture_output=True).stdout
        
        # subprocess.run produces a weird output format, so fix it and parse!
        vid_data_dict = json.loads(vid_data_json.decode('utf-8'))

        # This looks weird as heck but it's how probe cmd JSONs it's data so ¯\_(ツ)_/¯
        #pprint.pprint(orientationer_json['streams'][1]
        rotated = 'rotate' in vid_data_dict['streams'][1]['tags']
        frame_rate = eval(vid_data_dict['streams'][1]['avg_frame_rate'])
        width = vid_data_dict['streams'][1]['width']
        height = vid_data_dict['streams'][1]['height']
        print('{}:  Frame rate? {}  W/H? {}/{}  Rotated? {}'.format(output_file, frame_rate, width, height, rotated))

        if width/height != aspect_ratio: 
            print('Error parsing {}: actual aspect ratio {} does not match stated {}.'
                'Skipping...'.format(os.path.basename(vid_file), height/width, aspect_ratio))
            continue
        
        # TODO: FFMPEG MAGIC HERE!!!!
               


        







