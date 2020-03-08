#!/bin/python3

import copy

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    text_file = open(dictionary_file, 'r')
    list1= text_file.readlines()
    list2 = [x[:-1] for x in list1]
    list2[len(list2)-1]='zymes'

    s=Stack()
    s.push(start_word)
    q = Queue()
    q.enqueue(s)
   
    if start_word == end_word:
        return [start_word]
    if len(start_word) > 5 or len(end_word) > 5:
        return 'None'

    while q.isEmpty() == False:
        stack = q.dequeue()
        for i in list2:
            if _adjacent(stack.peek(),i)==True:
                if i == end_word:
                    stack.push(end_word)
                    out = []
                    while stack.isEmpty() == False:
                        out.append(stack.pop())
                    out.reverse()
                cstack = copy.deepcopy(stack)
                cstack.push(i)
                q.enqueue(cstack)
                list2.remove(i)
        if q.isEmpty()==True:
            return 'None'



def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    s = Stack()
    for i in ladder:
        s.push(i)
    if s.size()==0:
        return False
    while s.isEmpty()==False:
        if s.size() == 1:
            return True
        a=s.pop()
        b = s.peek()
        if _adjacent(a,b)==False:
            return False


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1)>5:
        return False
    if len(word2)>5:
        return False

    count = 0
    i = 0
    while i < 5:
        if word1[i]!=word2[i]:
            if count == 1:
                return False
            count +=1
        i+=1
    if count == 1:
        return True
