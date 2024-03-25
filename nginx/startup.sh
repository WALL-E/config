#!/bin/bash

docker run -itd -v ./nginx.conf:/etc/nginx/nginx.conf --net host openresty:1.0
