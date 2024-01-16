#!/bin/bash

# 3rd element 

read -p "ener the filename " name
awk '{print $3}' ${name}
