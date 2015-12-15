import argparse


def parse_args():

    parser = argparse.ArgumentParser(description='A terminal based typing tutor')
    parser.add_argument('file', metavar='file', type=str,help='the file you want use for typing')
    parser.add_argument('-s','--silent',action="store_true",default=False,help='show stats at the end')
    return parser.parse_args()
