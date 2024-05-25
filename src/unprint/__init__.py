import time

def unprint(num_lines:int=1, delay:int=0) -> None:
    if delay:
        time.sleep(delay)
    print('\033[1A\x1b[2K'*num_lines, end='')