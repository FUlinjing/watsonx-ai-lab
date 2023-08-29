#!/bin/bash

PODMANNET="testnet"

podman rm -f webgui
podman rmi webgui

if [[ .`podman ps --filter network=${PODMANNET} | wc -l | awk '{print $1}'`. != .2. ]]; then
    podman network rm ${PODMANNET}
fi
