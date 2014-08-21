def count_words(string, file=None):
    num = len(string.split())
    print 'there are: ', num, 'words'

    if file:
        with open(file) as f:
            num = lun(f.read().split())

        print 'there are: ', num, 'words in the file'


def main():
    string = raw_input('type something\n>>')
    count_words(string)

main()
