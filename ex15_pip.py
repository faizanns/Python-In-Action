"""
Two packages(IMDbPY & IPython) had to be installed.
"""

from imdb import IMDb
from IPython.display import Image
from IPython.core.display import HTML
# create an instance of the IMDb class
ia = IMDb()
# get a movie and print it
holy_grail = ia.get_movie('0071853')
print(holy_grail)
# getting cover and print it
cover = holy_grail.data['cover url']
Image(url = cover)

"""
output: Monty Python and the Holy Grail
"""