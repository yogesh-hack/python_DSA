# Now, we need to sort the objects, not just numbers.

# QUESTION :- Write a function to sort the millions of notebooks in decreasing orders of likes with efficient time.

# USE the custom function to camparision two objects(Notebooks)

class Notebooks:
    # Default constructor
    def __init__(self,title,authors,likes) -> None:
        self.title, self.authors, self.likes = title, authors, likes

    def __repr__(self) -> str:
        return 'notebook <"{}/{}", {} likes>'.format(self.authors, self.title,self.likes)

# Create soe sample object(notebooks)

nb0 = Notebooks('python','Yoegsh',1000)
nb1 = Notebooks('pytorch','sumitra',200)
nb2 = Notebooks('advanced python','rohan',100)
nb3 = Notebooks('Graphics c++','arora',60)
nb4 = Notebooks('c++','vikas',900)
nb5 = Notebooks('java-fundamnetal','yash',300)
nb6 = Notebooks('java-core','abhishek',100)
nb7 = Notebooks('machine-learning','jacobin',20)
nb8 = Notebooks('deep learning','shiv',800)
nb9 = Notebooks('AI','Mayank',500)

notebooks = [nb0,nb1,nb2,nb3,nb4,nb5,nb6,nb7,nb8,nb9]
print(notebooks)
# +++++++++++++++++++ OUTPUT ++++++++++++++++++++
"""
[notebook <"Yogesh/python", 1000 likes>,
 notebook <"sumitra/pytorch", 200 likes>,
 notebook <"rohan/advanced python", 100 likes>,
 notebook <"arora/Graphics c++", 60 likes>,
 notebook <"vikas/c++", 900 likes>,
 notebook <"yash/java-fundamnetal", 300 likes>,
 notebook <"abhishek/java-core", 100 likes>,
 notebook <"jacobin/machine-learning", 20 likes>,
 notebook <"shiv/deep learning", 800 likes>,
 notebook <"Mayank/AI", 500 likes>]

"""

## Custom camparision function for notebook likes

def compare_likes(nb0,nb1):
    if nb0.likes > nb1.likes:
        return "lesser"
    elif nb0.likes == nb1.likes:
        return "Equal"
    elif nb0.likes < nb1.likes:
        return "Greater"

## Sorting with effcient time and space
# * Merge sort * is more efficient and works faster than quick sort in case of larger array size or datasets. 
# Quick sort is more efficient and works faster than merge sort in case of smaller array size or datasets.

## ++++++++++++++ SOLUTION +++++++++++++++++++++

# Custom campare function
def default_campare(x, y):
    if x > y:
        return "less"
    elif x == y:
        return "Equal"
    else:
        return "greater"

# Merge Sort algo
def merge_sort(object, campare = default_campare):
    if len(object) <=1 :
        return object
    mid = len(object)//2
    return merge(merge_sort(object[:mid],campare),merge_sort(object[mid:],campare),campare)

def merge(left , right, campare):
    i ,j ,merged = 0 ,0 ,[]
    while i < len(left) and j < len(right):
        result = campare(left[i],right[j])
        if result  == "lesser" or result ==  "Equal":
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]

sorted_notebook  = merge_sort(notebooks , compare_likes)

print(sorted_notebook)

# +++++++++++++++++++++++++++ OUTPUT ++++++++++++++++++++++++++++++++++

""""
[notebook <"Yogesh/python", 1000 likes>,
 notebook <"vikas/c++", 900 likes>,
 notebook <"shiv/deep learning", 800 likes>,
 notebook <"Mayank/AI", 500 likes>,
 notebook <"yash/java-fundamnetal", 300 likes>,
 notebook <"sumitra/pytorch", 200 likes>,
 notebook <"rohan/advanced python", 100 likes>,
 notebook <"abhishek/java-core", 100 likes>,
 notebook <"arora/Graphics c++", 60 likes>,
 notebook <"jacobin/machine-learning", 20 likes>]
 
"""

