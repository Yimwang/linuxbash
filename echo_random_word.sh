#!/bin/bash

var=/usr/share/dict/words

random_word=$( sort -R $var | head -1 )

echo print a random word :: $random_word 
