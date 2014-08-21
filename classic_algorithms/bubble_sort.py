from random import randint

def bubble_sort(lis):
    swapped = True
    counter = 0
    while(swapped):
        swapped = False
        counter += 1
        for n in range(len(lis) - counter) :
            if lis[n] > lis[n+1]:
                lis[n], lis[n+1] = lis[n+1], lis[n]
                swapped = True

def generate_list(lst, num):
    for n in range(num):
        lst.append(randint(0, 9))
    return lst


def main():
    lst = []
    num = int(raw_input('you are about to generate a list randomly, '+\
           'pick a number to be the length of the list.\n>>'))

    lst = generate_list(lst, num)
    print 'unsorted: ', lst
    bubble_sort(lst)
    print 'sorted: ', lst

if __name__ == '__main__':
    main()
