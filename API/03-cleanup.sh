#!/bin/bash

podman rm -f backend
podman rmi backend

PODMANNET="testnet"

if [[ .`podman ps --filter network=${PODMANNET} | grep ${PODMANNET} | wc -l | awk '{print $1}'`. == .1. ]]; then
    podman network rm ${PODMANNET}
fi
