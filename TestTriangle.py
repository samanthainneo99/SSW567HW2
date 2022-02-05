# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
Edited by: Samantha Inneo
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(6, 8, 10), 'Right','6,8,10 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleD(self): 
        self.assertEqual(classifyTriangle(10, 8, 6), 'Right','10,8,6 is a Right triangle')
        
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):    
        self.assertEqual(classifyTriangle(12,12,12),'Equilateral','12,12,12 should be equilateral')

    def testNotATriangleTriangleA(self):
        self.assertEqual(classifyTriangle(10,10,20),'NotATriangle','10,10,20 should be NotATriangle')

    def testNotATriangleTriangleB(self):    
        self.assertEqual(classifyTriangle(10,10,100),'NotATriangle','10,10,100 should be NotATriangle')

    def testNotATriangleTriangleC(self):
        self.assertEqual(classifyTriangle(10,15,30),'NotATriangle', '10, 15, 30 should be NotATriangle')   

    def testIsoscelesTriangleA(self):    
        self.assertEqual(classifyTriangle(10,10,18),'Isoceles', '10, 10, 18 should be Isoceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(5.5,5.5,10),'Isoceles', '5.5, 5.5, 10 should be Isoceles')

    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(18,10,10),'Isoceles', '18, 10, 10 should be Isoceles')

    def testIsoscelesTriangleD(self):
        self.assertEqual(classifyTriangle(10,5.5,5.5),'Isoceles', '10, 5.5, 5.5should be Isoceles')

    def testScaleneTriangleA(self):     
        self.assertEqual(classifyTriangle(2,5,6),'Scalene','2,5,6 should be Scalene')

    def testScaleneTriangleB(self):     
        self.assertEqual(classifyTriangle(2.5,5.5,6.5),'Scalene','2.5,5.5,6.5 should be Scalene')
    
    def testScaleneTriangleC(self):     
        self.assertEqual(classifyTriangle(6,5,2),'Scalene','6,5,2 should be Scalene')

    def testScaleneTriangleD(self):     
        self.assertEqual(classifyTriangle(6.5,5.5,2.5),'Scalene','6.5,5.5,2.5 should be Scalene')

    ''' def testInvalidInputA(self):    
        self.assertEqual(classifyTriangle('A','B','C'),'InvalidInput','A,B,C should be InvalidInput')
    '''
   
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

