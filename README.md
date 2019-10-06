# Chinese Information Processing Project1

## 繁简转换

运行时，-e参数为STT时表示简转繁，TTS表示繁转简；-f参数表述输入文件，若无输入文件则默认stdin输入；-t参数表示输出文件，若无输出则默认stdout输出。

示例：
 python .\translator.py -e STT -f .\simp.txt -t ans.txt
