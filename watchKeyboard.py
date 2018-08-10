from pyhooked import Hook, KeyboardEvent
import os,sys

def handle_events(args):
    if isinstance(args, KeyboardEvent):
        print(args.key_code)
        if args.current_key == 'G' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
            print('ok')
            # os.system("python getImgFromClipboard.py")
        if args.current_key == '0' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
            print('exit')
            hk.stop()
            sys.exit(0)

if __name__ == '__main__':
    hk = Hook()  # make a new instance of PyHooked
    hk.handler = handle_events  # add a new shortcut ctrl+a, or triggered on mouseover of (300,400)
    hk.hook()  # hook into the events, and listen to the presses
