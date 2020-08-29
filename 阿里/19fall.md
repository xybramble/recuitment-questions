知识库中所有歌曲的列表，所有歌手的列表，其他各种实体的列表。使用这些实体通过以下规则来教会机器识别关键词：  
为了简化问题，我们使用从左到右的最大长度匹配的原则：在本句里面，“周杰”的字符串长度比“周杰伦”小，所以识别“周杰伦“作为歌手。  
输入：  
singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪  
请播放周杰伦的七里香给我听  
输出：  
请播放 周杰伦/actor,singer 的 七里香/song 给我听  
```python
def main():
    s1 = raw_input()
    s2 = raw_input()
    dic = {}
    for sen in s1.split(';'):
        Class, name = sen.split('_')
        dic.setdefault(class,[])
        for k in name.split('|'):
            dic[Class].append(k)
    k = 0
    res = ''
    while k<len(s2):
        rel = ''
        clas = []
        for Class, val in dic.items():
            for i in val:
                l = len(i)
                if s2[k:k+l]==i:
                    if len(rel)<l:
                        rel = i
                        clas = [Class]
```
