#!/bin/bash

# pipe command

hh="$(date +%s | sha256sum | head -c10)"
echo "${hh}"
