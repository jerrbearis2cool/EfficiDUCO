""" Functions for loading and dumping in json """

from json import dump, load

# currently just a straight up copy of my previous code

deafults = ["Three presidents, all Founding Fathers\u2014John Adams, Thomas Jefferson, and James Monroe\u2014died on July 4. Presidents Adams and Jefferson also died the same year, 1826; President Monroe died in 1831. Coincidence? You decide.", "The Barbie doll\u2019s full name is Barbara Millicent Roberts, from Willows, Wisconsin. Her birthday is March 9, 1959, when she was first displayed at the New York Toy Fair. (barbiemedia.com)", "There actually aren\u2019t \u201c57 varieties\u201d of Heinz ketchup, and never were. Company founder H.J. Heinz thought his product should have a number, and he liked 57. Hint: Hit the glass bottle on the \u201c57,\u201d not the bottom, to get the ketchup to flow. (heinz.com)", "One of President John Tyler\u2019s grandsons is still alive today\u2014and he was born in 1790. How is this possible? President Tyler, the 10th US president, was 63 when his son Lyon Tyler was born in 1853; Lyon\u2019s son was born when he was 75. President Tyler\u2019s living grandson, Harrison Tyler is 92. Lyon\u2019s other son Lyon Jr. passed away in 2020 at the age of 95. The Tyler family still maintains the President\u2019s home, Sherwood Forest Plantation in Virginia. (sherwoodforest.org)", "The tallest man ever recorded was American giant Robert Wadlow (1918\u20131940), who stood 8 feet 11 inches. Wadlow\u2019s size was the result of abnormally enlarged pituitary gland. (guinnessworldrecords.com)", "The tallest living man is 37-year-old Sultan Kosen, from Turkey, who is 8 feet, 2.8 inches, who set the record in 2009. His growth is also due to a pituitary issue. (guinnessworldrecords.com)", "Never gonna give you up"] # change this if you want

def json_put(list1:list, filename:str, reset:bool = False):
    """ Saves list1 into filename. returns 0 if completed """
    if reset:
        list1 = deafults
    with open(filename, 'w') as f:
        dump(list1, f)
    return 0

def json_get(filename:str):
    """ Gets the info from filename and returns it. If there is no filename, returns -1 """
    try:
        with open(filename, 'r') as f:
            return load(f)
    except FileNotFoundError:
        json_put([], filename)
        with open(filename, 'r') as f:
            return load(f)