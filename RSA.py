# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:26:43 2023

@author: cassa

RSA ENCRYPTION
"""
import gcd
import fastExpo
import random

def main():
    p = 7
    q = 3
    phi = (p-1) * (q-1)
    message = "Hello world!"

    e = generateE(phi)
    
    gcd.extended_gcd(e,phi)
    d = gcd.x // phi 
    
    c = encrypt(message, e, phi)
    m = decrypt(c, d, phi)
    
    print(message, m)

    
def generateE(phi):
    x = random.randint(1,10)

    while(gcd.gcd(x,phi) != 1):    #will take log time
        x = random.randint(1,10)
    
    return x
    
def encrypt(message, e, phi):
    c = fastExpo.fastExpo_recursive(message, e, phi)
    return c
    
def decrypt(c, d, phi):
    c = encrypt()
    m = fastExpo.fastExpo_recursive(c, d, phi)
    return m


#main will be executed down here
main()