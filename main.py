


'''
Function: Get book from user
Input: book directory
Output: return a list of str of the book

'''
def get_book_text(userDirectory):

    with open(userDirectory) as f:
        
        # read book content
        book_content = f.read()
       
        # typecast to string 
        str(book_content)

        return book_content

''' 
Function: Give total word count of book
Input: Book text
Output: Total word count 
'''
def word_count(texts):

    split = texts.split()  

    print(f"Found {len(split)} total words")



def main():
    
    book_dir = "./books/frankenstein.txt"

    word_count(get_book_text(book_dir))
    
    







main()

