#!/bin/bash

xin_chao(){
	echo "xin chào bạn!"
}

xin_chao_ten(){
	echo "xin chào $1!"
}

if [ "$1" == "name" ]; then
	xin_chao_ten "$2"
else
	xin_chao
fi
