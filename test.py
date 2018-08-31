'''
Created on Aug 21, 2018

@author: ociny
'''

from pybooru import Danbooru

site = Danbooru(site_name = 'danbooru')

amount = 5
items = site.post_list(limit = amount, tags = 'yazawa_nico', random = True)

for x in range(amount):
    print(items[x]['file_url'])