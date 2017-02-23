#! /bin/bash

python main.py $1 > $1.out
python score.py $1
