#!/bin/bash
PODMANNET="testnet"

if [[ .`podman network ls | grep ${PODMANNET} | wc -l | awk '{print $1}'`. == .0. ]]; then
    podman network create ${PODMANNET}
fi

podman run --cap-add=NET_RAW --network ${PODMANNET} --name  backend -d -p 8000:8000 \
 backend

