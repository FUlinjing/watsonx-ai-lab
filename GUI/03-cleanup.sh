#!/bin/bash

PODMANNET="testnet"

podman rm -f webgui
podman rmi webgui

if [[ .`podman ps --filter network=${PODMANNET} | grep ${PODMANNET} | wc -l | awk '{print $1}'`. == .1. ]]; then
    podman network rm ${PODMANNET}
fi
