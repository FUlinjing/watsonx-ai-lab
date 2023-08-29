#!/bin/bash

podman rm -f backend
podman rmi backend

PODMANNET="testnet"

if [[ .`podman ps --filter network=${PODMANNET} | wc -l | awk '{print $1}'`. != .2. ]]; then
    podman network rm ${PODMANNET}
fi
