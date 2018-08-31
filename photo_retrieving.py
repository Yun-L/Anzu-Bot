'''
Created on Aug 21, 2018

@author: yun
'''

from pybooru import Danbooru


def dan(tag):
    site = Danbooru(site_name='danbooru')
    tag = tag
    for x in range(len(tag)):
        if (tag[x] == ' ' and (x+1) < len(tag)):
            tag = tag[x:]
            break
    picture = site.post_list(limit = 1, tags = tag, random = True)
    return (picture[0]['file_url'], tag)
    
