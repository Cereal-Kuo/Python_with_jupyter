#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Circle_Cal:
    pi = 3.1415926
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * Circle_Cal.pi
