import sys

def remove_duplicate_character(s):
    if not s:
        return ''

    s_list = [s[i] for i in range(len(s)) if i == 0 or s[i] != s[i-1]]
    result = ''.join(s_list)
    return result

# Usage: python3 remove_ctc_duplicate_character.py <result csv file> <output file name>
f = open(sys.argv[1])
l = [x.strip().split('\t') for x in f.readlines()]
t = [(x[0] + '\t' + remove_duplicate_character(x[1])+'\t'+x[2]+'\n') for x in l]
fw = open(sys.argv[2], 'w')
fw.writelines(t)