#!/bin/bash
# use podman? but we have not had the image!
podman run --rm --read-only -ti --cpus 0.01 --memory 2m localhost/busybox
# t -> visual
# i -> communication
