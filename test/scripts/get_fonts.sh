#!/bin/bash

mkdir test/fonts

wget -O test/font_zh.zip https://github.com/adobe-fonts/source-han-sans/releases/download/2.004R/SourceHanSansHWSC.zip
unzip -d test/fonts -o test/font_zh.zip

wget -O test/font_jp.zip https://github.com/adobe-fonts/source-han-sans/releases/download/2.004R/SourceHanSansJ.zip
unzip -d test/fonts -o test/font_jp.zip
