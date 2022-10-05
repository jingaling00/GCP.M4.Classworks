# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 13:10:05 2022

@author: jingy
"""


import dna_info
from dna_info import bin2text, text2bin

text2bin('jing')
bin2text('0101010')

def dna2bin(dna):
    base = {'G':'11', 'A':'00',
            'T':'01', 'C':'10'}
    seq = ''
    for ele in dna:
        seq+=(base[ele])
    return seq

def bin2dna(binStr):
    base = {'11':'G', '00':'A',
            '01':'T', '10':'C'}
    binStr = [binStr[i:i+2] for i in range(0,len(binStr),2)]
    seq = ''
    for ele in binStr:
        seq+=(base[ele])
    return seq

def dna2text(dna):
    dna_to_bin = dna2bin(dna)
    bin_to_text = bin2text(dna_to_bin)
    return bin_to_text
    
if __name__ == '__main__':
    text_inpt = input('Enter text: ')
    text_to_bin = text2bin(text_inpt)
    bin_to_dna = bin2dna(text_to_bin)
    print(f'{text_inpt} is {text_to_bin} in binary and {bin_to_dna} in DNA')
    