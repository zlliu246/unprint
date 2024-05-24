def unprint(num_lines=1):
    print('\033[1A\x1b[2K'*num_lines, end='')