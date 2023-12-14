# A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the book. They always turn pages one at a time. When they open the book, page  is always on the right side:
# image
# When they flip page , they see pages  and . Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book. If the book is  pages long, and a student wants to turn to page , what is the minimum number of pages to turn? They can start at the beginning or the end of the book.
# Given  and , find and print the minimum number of pages that must be turned in order to arrive at page .

import math
def pageCount(n, p):
    # Write your code here
    counter = 0

    # finding way how to open(from the back or beginign of the book) by finding middle of the book and comparing to needed page
    if p <= n//2:
        #Opening from the begining
        for page in range(1, p): #Starting from 1 since first page will appear as soon as we open the book(book opening doesn't count)
            counter+=1
    else:
        #Finding if last page is even or odd(since if we need page 5 of total 6 pages we still have to flip one page)
        if n % 2 ==0:
            for page in range(n-1, p-1, -1):
                counter+=1
        else:# here if number of pages is odd and we need page 4, of 5 total pages, we don't have to flip a page(book opening doesn't count)
            for page in range(n-1, p, -1):
                counter+=1
    return math.ceil(counter / 2)

print(f"Conter return:{pageCount(5, 4)}")