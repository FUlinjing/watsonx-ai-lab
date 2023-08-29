#!/bin/bash
source ./settings.env 

PODMANNET="testnet"

if [[ .`podman network ls | grep demonet | wc -l | awk "{print $1}"`. == .0. ]]; then
    podman network create ${PODMANNET}
fi

podman run --cap-add=NET_RAW --network ${PODMANNET} --name webgui -p 8080:8080 -d \
 -e REACT_APP_WA_INTEGRATIONID=${REACT_APP_WA_INTEGRATIONID} \
 -e REACT_APP_WA_REGION=${REACT_APP_WA_REGION} \
 -e REACT_APP_WA_SERVICEINSTANCEID=${REACT_APP_WA_SERVICEINSTANCEID} \
 -e REACT_APP_BE_APIKEY=${REACT_APP_BE_APIKEY} \
 -e REACT_APP_BE_APIURL=${REACT_APP_BE_APIURL} \
 webgui

sleep 2
podman logs webgui
