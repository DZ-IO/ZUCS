# ZUCS
Zda UTAU Core Server-泽大U核心服务端
## 快速开始
（这次大泽依然在仓库里扔了一枚一毛一样的UST工程）  
前置准备和UC1一样：
#### 0x01 准备本体：
1. 安装git和python  
`# apt-get update \`  
`&& apt-get install -y python3 git python3-pip`
2. 安装python组件：
`$ pip3 install flask configparser`
3. git clone!  
`$ git clone https://github.com/daze456/ZUCS.git && cd ZUCS`
#### 0x02 准备音源：  
1. 从[这里](https://daze456.github.io/zew/data/ZeW_Bata_0.1.0.191225.7z)下载泽小白数据  
2. 解压缩到仓库下的voice文件夹  
ps:也可以使用命令：  
`$ wget https://daze456.github.io/zew/data/ZeW_Bata_0.1.0.191225.7z \`  
`&& 7z x ZeW_Bata_0.1.0.191225.7z -r -o./voice/ZeW_Bata_0.1.0.191225 \`  
`&& rm -rf ZeW_Bata_0.1.0.191225.7z`  
#### 0x03 准备wavtool
1. 安装cmake  
`# apt-get update \`  
`&& apt-get install -y cmake build-essential`
2. 下载并编译wavtool  
`$ git clone https://github.com/m13253/wavtool-yawu.git \`    
`&& cd wavtool-yawu \`  
`&& ./configure \`  
`&& cd build && make \`  
`&& cp ./wavtool-yawu ../ && cd .. \`  
`&& cp ./wavtool-yawu ../wavtool/ && cd .. \`  
`&& rm -rf wavtool-yawu/`
#### 0x04 准备引擎（RUCE） 
~~`$ cd engine \`~~  
~~`&& git clone https://github.com/Rocaloid/RUCE.git \`~~    
~~`&& cd RUCE \`~~  
~~`&& ./configure \`~~  
~~`&& cd build && make \`~~  
~~`&& cd ../ && cd ../ && cd ../`~~  
由于Linux版RUCE存在~~BUG~~特性，所以这里使用Windows版RUCE  
`$ sudo apt-get install wine \`  
`&& wget http://rocaloid.github.io/resources/binaries/RUCE-1.0.0-alpha2.zip \`  
`&& unzip RUCE-1.0.0-alpha2.zip -d ./engine \`  
`&& rm RUCE-1.0.0-alpha2.zip`  
#### 0x05 启动
共需要两个进程：  
`$ python3 loop.py`  
`$ python3 app.py`  

话说各位注意到那个`dockerfile`了吗？（可能有BUG，所以没公开）  
## 配置文件
配置文件:`cfg.ini`,跟UC1差不多  
`;泽大U核心配置文件开始`  
`[zuc]`  
`;设置默认使用的声库`  
`oto=./voice/ZeW_Bata_0.1.0.191225`  
`;设置默认wavtool（工具1）`  
`tool=./wavtool/wavtool-yawu`  
`;设置默认resampler（工具2）`  
`resamp=./engine/RUCE-1.0.0-alpha2/RUCE_Win.sh`  
`;设置默认缓存文件夹`  
`cachedir=./cache`  
`;设置输出文件`  
`output=./output.wav`  
`;泽大U核心配置文件结束`  
注：由于easyust存在~~特性~~BUG，所以在这里没有可选参数，而且参数以配置文件为准，请认真填写
## 使用方法
这就是个web服务器。。。
启动两个python程序就行
## 灵感
UC2的TODO里我表示要加入websocket，于是，它来了！  
（PS：这货也是大泽边学flask边开发的，果然有需求就有动力啊！）  
## TODO
1. 这还不是真正的WebSocket！  
2. 更详细的配置文件