#!/bin/bash

for IMAGE in *.jpg
do
	NAME="$(date +%F)-${IMAGE}"
	mv ${IMAGE} ${NAME}
done

ls

