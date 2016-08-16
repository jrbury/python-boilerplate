import argparse


def build_arg_parser():
    """
    Builds a standard argument parser with arguments
    """
    parser = argparse.ArgumentParser(
        description='Standard Arguments')

    parser.add_argument('-o', '--output_std',
                        required=False,
                        action='store_true',
                        help='Pipe everything to stdout in addition to the log file.')

    return parser


# this is where you would do checks on the values passed as args
# should raise a ValueError if an arg value fails its check
def get_and_check_args():

    parser = build_arg_parser()

    args = parser.parse_args()

    return args


def generate_long_args(arg_dict):
    return ' '.join(['--%s %s' % (k, v) for k, v in arg_dict.iteritems()])
