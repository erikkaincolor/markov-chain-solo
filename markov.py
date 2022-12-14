"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)
    content_list=[]
    for lines in file:
        content=lines.rstrip() #strip lines of space
        content_list.append(content)
    
    return (str(content_list)) #the type is string but the brackets are still there for some reason


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:
        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:
        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:
        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None] """
    
    chains = {}
    # pairs = ()
    # list_o_str = list(text_string)
    # print(list_o_str)
    # for item_in_list in list_o_str: #for each word in the string....
    #     word1 = item_in_list
    #     word2 =item_in_list
    #     pairs=(word1, word2)
    # chains[pairs]=text_string[2:]
    # print(item_in_list)
    # print(list_o_str)
    
    for items in text_string:
        text_string.rstrip()
        print(items)
    print(text_string)
    # return chains













def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


# input_path = 'green-eggs.txt'

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
