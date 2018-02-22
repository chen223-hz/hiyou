#coding: utf-8
from django.db import models

# Create your models here.

found_item = {
    "miqi": {
        "title": u'米奇大街',
        "content": u'''
<h3 class="rich_media_title" style="text-align:center"> 中国定制！  全球首个“米奇大街” 将现上海迪士尼</h3>
<section class=""><section class="" style=" font-family: 微软雅黑;  box-sizing: border-box; border: 0px none;
padding: 0px; margin: 0px; -webkit-transform: none; " data-id="85354" data-color="rgb(89, 195, 249)" data-custom="rgb(89, 195,
249)"><section style="border: none; margin: 5px 0px; padding: 0px 5px; box-sizing: border-box;"><section style="box-sizing:
border-box; color: inherit; border-color: rgb(89, 195, 249); padding: 0px; margin: 0px;"><section class=""
data-style="color:inherit;font-size:16px;text-align:center;line-height:1.5em;" style="border-top-left-radius: 0px;
border-top-right-radius: 0em; border-bottom-right-radius: 0em; border-bottom-left-radius: 0px; box-sizing: border-box; color:
rgb(255, 255, 255); text-align: center; padding: 0.8em 0.5em; border-color: rgb(89, 195, 249); background-color: rgb(89, 195, 249);
margin: 0px;"><p style="text-align: left; text-indent: 2em; line-height: 2em; white-space: normal;"><strong style="text-indent: 2em;
line-height: inherit;"><span style="font-family: 宋体; line-height: 28px; white-space:
pre-wrap;">“这座旋转木马由中国的手工艺师手工打造，同时由一个优秀的团队为其手绘上色，72种绚烂颜色美妙交织。”</span></strong></p></section></section><section
style="margin: -18px 8px 0px; padding: 0px; border-right-width: 90px; border-left-width: 0px; border-right-style: solid;
border-right-color: rgb(89, 195, 249); border-left-color: rgb(89, 195, 249); display: inline-block; max-width: 100%; height: 60px;
width: 50px; vertical-align: top; float: right; -webkit-transform: rotate(-50deg); color: inherit; border-bottom-width: 60px
!important; border-top-style: solid !important; border-bottom-style: solid !important; border-top-color: transparent !important;
border-bottom-color: transparent !important; word-wrap: break-word !important; box-sizing: border-box
!important;"></section></section><section style="width: 0px; height: 0px; clear: both; box-sizing: border-box; padding: 0px; margin:
0px;"></section></section><p style="white-space: normal;"><img width="100%"
data-src="http://mmbiz.qpic.cn/mmbiz/6Ht0iasBR9AzHwNqumrQvZ3f0pB8tCm2Pd1GNts0KmogykSnhwicF0a7goXpbswmKhU89vlPkwpF2gNH2fFypYJw/0?wx_fmt=jpeg"
title="7420a6f5-fc81-4e2b-8145-dbc90978309d.jpg" data-type="jpeg" data-ratio="0.5909090909090909" data-w="" class=""
src="http://mmbiz.qpic.cn/mmbiz/6Ht0iasBR9AzHwNqumrQvZ3f0pB8tCm2Pd1GNts0KmogykSnhwicF0a7goXpbswmKhU89vlPkwpF2gNH2fFypYJw/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1"
style="width: 100% !important; height: auto !important; visibility: visible !important;" data-fail="0">
</p><p style="white-space:
normal;"><br></p><section class="" style="   box-sizing: border-box; border: 0px none; padding: 0px; -webkit-transform: none;
margin: 0px; " data-id="29735" data-color="rgb(89, 195, 249)" data-custom="rgb(89, 195, 249)"><section style="margin-top: 0px;
padding: 0px 5px; line-height: 10px; color: inherit; border: 1px solid rgb(89, 195, 249); box-sizing: border-box;"><section
style="padding: 0px; color: inherit; height: 8px; margin: -8px 0px 0px 140px; width: 50%; background-color: rgb(254, 254, 254);
box-sizing: border-box;" data-width="50%"><section style="width: 8px; height: 8px; border-top-left-radius: 100%;
border-top-right-radius: 100%; border-bottom-right-radius: 100%; border-bottom-left-radius: 100%; line-height: 1; box-sizing:
border-box; font-size: 18px; text-decoration: inherit; border-color: rgb(89, 195, 249); display: inline-block; margin: 0px; color:
inherit; background-color: rgb(89, 195, 249); padding: 0px;"></section></section><section class="" data-style="text-indent: 2em;"
style="padding: 0px; line-height: 2em; color: rgb(62, 62, 62); font-size: 14px; margin: 15px; box-sizing: border-box;"><p
style=""><span style="font-family: 宋体; font-size:
16px;">预计明年开幕的上海迪士尼度假区近日公布乐园内六大园区中“米奇大街”、“奇想花园”的精彩亮点，包括全球首座以迪士尼传奇影片《幻想曲》中的角色及交响乐设计而成的旋转木马。值得一提的是，旋转木马出自中国能工巧匠之手。</span></p><p
style=""><br></p><p style=""><span style="font-family: 宋体; font-size:
16px;">据了解，旋转木马一直是迪士尼乐园历史上的最经典游乐项目，在过去５座乐园中，木马受欢迎程度一直名列前茅。此次，上海迪士尼的木马，融合了中美共同的创意和工艺。</span></p><p
style=""><br></p><p style=""><img
data-src="http://mmbiz.qpic.cn/mmbiz/6Ht0iasBR9AzHwNqumrQvZ3f0pB8tCm2P5F62DpLb2kYzicvKUWkKsu7iaqQhTqvibcMRBnia5KmPtKh7y107PibaePw/0?wx_fmt=jpeg"
title="5160597461.jpg" data-type="jpeg" data-ratio="0.6666666666666666" data-w="450" class=""
src="http://mmbiz.qpic.cn/mmbiz/6Ht0iasBR9AzHwNqumrQvZ3f0pB8tCm2P5F62DpLb2kYzicvKUWkKsu7iaqQhTqvibcMRBnia5KmPtKh7y107PibaePw/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1"
style="width: 100% !important; height: auto !important; visibility: visible !important;" data-fail="0"><br></p><p
style=""><br></p><p style=""><span style="font-family: 宋体; font-size:
16px;">“奇想花园”资深总监、执行制作人伍德沃德介绍，在影片《幻想曲》中一共有62匹马，因此“幻想曲旋转木马”中62匹飞马爸爸、飞马妈妈、飞马宝宝与2辆马车将回旋翱翔。</span></p><p
style=""><br></p><p style=""><span style="font-family: 宋体; font-size:
16px;">“这座旋转木马由中国的手工艺师手工打造，同时由一个优秀的团队为其手绘上色，72种绚烂颜色美妙交织。”伍德沃德说。</span></p><p
style=""><br></p><p style=""><span style="font-family: 宋体; font-size:
16px;">记者了解到，在“奇想花园”中，还有不少景点由迪士尼与中国本地供应商及艺术家共同合作完成，例如全球首创的“十二朋友园”中的十二幅大型马赛克壁画。</span></p><p
style=""><br></p><p style=""><span style="font-family: 宋体; font-size:
16px;">伍德沃德介绍，这些壁画分别展示了化身中国十二生肖的迪士尼动画角色。“2016年是中国的猴年，相信以阿拉丁神灯中可爱的猴子阿布的角色为主题的壁画，将在上海迪士尼开幕后受到中国游客欢迎。”</span></p><p
style=""><br></p><p style=""><img
data-src="http://mmbiz.qpic.cn/mmbiz/6Ht0iasBR9AzHwNqumrQvZ3f0pB8tCm2PnQ2ZS1RzTwt8kNtZJlsDdiaSZg12d7UC39544oVXDs6amlpD2CUHBlw/0?wx_fmt=jpeg"
title="04ebf6a619cb4631bdf83f3616affe3e.jpg" data-type="jpeg" data-ratio="0.8017241379310345" data-w="464" class="img_loading"
src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg=="
style="width: 100% !important;"><br></p><p style=""><br></p><p style=""><span style="font-family: 宋体;
font-size:
16px;">中餐馆“漫月轩”，则以中国建筑风格为基调，配以装饰着山、海、漠、林、河的象征符号，在漫月轩中，将陈列展示不少中国艺术家的书法、绘画、雕塑作品，迪士尼动画角色也将融入布置当中。</span></p><p
style=""><br></p><p style=""><span style="font-family: 宋体; font-size:
16px;">在“米奇大街”园区，为了向华特·迪士尼于1928年创作的动画——正是该动画将米奇介绍给全世界——致敬，“蒸汽船米奇喷泉”将在上海迪士尼乐园首次亮相。</span></p><p
style=""><br></p><p style=""><span style="font-family: 宋体; font-size:
16px;">米奇大街创意总监戴龙瑞介绍，在全球其他迪士尼园区，迎宾大道都是“美国小镇”风格。上海迪士尼建设过程中，通过调查发现，中国游客会更爱讲故事以及故事角色，因此，上海迪士尼把与迪士尼人物见面的环节完全融入“米奇大街”的故事讲述中，以获得中国游客的共鸣。</span></p><p
style=""><br></p><p style=""><span style="font-family: 宋体; font-size:
16px;">游客还能在乐园内买到特别为中国游客设计及专门为上海迪士尼度假区设计的独家商品。其中，有身着中国传统服饰的米奇米妮玩偶、以中国古代食盒为外形包装的点心等等。</span></p></section><section
style="padding: 0px; background-color: rgb(254, 254, 254); color: inherit; text-align: right; height: 10px; margin: 0px 0px -4px
25px; width: 65%; box-sizing: border-box;" data-width="65%"><section style="margin: 0px auto 1px; border-top-left-radius: 100%;
border-top-right-radius: 100%; border-bottom-right-radius: 100%; border-bottom-left-radius: 100%; line-height: 1; box-sizing:
border-box; text-decoration: inherit; background-color: rgb(89, 195, 249); border-color: rgb(89, 195, 249); display: inline-block;
height: 8px; width: 8px; color: inherit; padding: 0px;"></section></section></section><section style="width: 0px; height: 0px;
clear: both; box-sizing: border-box; padding: 0px; margin: 0px;"></section></section><p style="white-space: normal;"><br></p><ul
class="list-paddingleft-2" style=""><li><p><span style="font-size: 14px;">来源：新华网</span></p></li></ul><p style="font-family:
微软雅黑; white-space: normal;"><br></p></section>'''
    },
    "qixiang": {
        "title": "奇想花园",
        "content": u'''<div class="rich_media_content " id="js_content">
                    <p style="line-height: 1.5em;"><a
href="http://triowt3.1to1crm.com.cn/web_service/counter/webmax_ad.aspx?DisneyCN:estorybook:Officialwechat" target="_blank"
send_referrer="false"
data_ue_src="http://triowt3.1to1crm.com.cn/web_service/counter/webmax_ad.aspx?DisneyCN:estorybook:Officialwechat"><img
data-src="http://mmbiz.qpic.cn/mmbiz/6SVj4PS2Kh96o61FvEicDC8brU9deGuRgJYaJQia6AAaKic5YHK67B5gSq3vG25dN5gTjJDvvWs57MQhhqYCq05gg/0?wx_fmt=jpeg"
data-w="" data-ratio="0.6462715105162524" data-type="jpeg" data-s="300,640" class=""
src="http://mmbiz.qpic.cn/mmbiz/6SVj4PS2Kh96o61FvEicDC8brU9deGuRgJYaJQia6AAaKic5YHK67B5gSq3vG25dN5gTjJDvvWs57MQhhqYCq05gg/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1"
style="width: 100% !important; height: auto !important; visibility: visible !important;" data-fail="0"></a><br></p><p
style="text-align: left; line-height: 1.5em;"><span style="line-height: 150%; font-family: 宋体; font-size: 16px;"></span> </p><p
style="text-align: left; line-height: 1.5em;"><span style="line-height: 150%; font-family: 宋体; font-size: 16px;">当<span
style="color: rgb(178, 162, 199); line-height: 150%; font-family: 宋体; font-size: 18px;"><strong>奇</strong></span>妙的<span
style="color: rgb(178, 162, 199); line-height: 150%; font-family: 宋体; font-size: 18px;"><strong>想</strong></span>象力遇见<span
style="color: rgb(178, 162, 199); line-height: 150%; font-family: 宋体; font-size: 18px;"><strong>花</strong></span>繁叶锦的<span
style="color: rgb(178, 162, 199); line-height: 150%; font-family: 宋体; font-size:
18px;"><strong>园</strong></span>林，交织成美妙的故事旋律。在上海迪士尼乐园的<span style="color: rgb(0, 0, 0); line-height: 150%;
font-family: 宋体; font-size:
16px;"><strong>奇想花园</strong></span>，这个采用花园设计的主题园区里，每一个人都能在这里找到欢乐，悠闲，和小而确实的幸福。</span></p><p
style="text-align: left; line-height: 1.5em;"><span style="line-height: 150%; font-family: 宋体; font-size: 16px;"></span><span
style="line-height: 150%; font-family: 宋体; font-size: 16px;"></span><span style="color: rgb(127, 127, 127); line-height: 150%;
font-family: 宋体; font-size: 12px;"></span> </p><p style="text-align: center; line-height: 1.5em;"><span style="color: rgb(127,
127, 127); line-height: 150%; font-family: 宋体; font-size:
12px;"><strong>✿</strong>开始漫步花园，无限畅想<strong>✿</strong></span></p><p style="line-height: 1.5em;"></p><p style="text-align:
left; line-height: 1.5em;"><span style="color: rgb(178, 162, 199); font-size: 20px;"><strong><span style="line-height: 150%;
font-family: 宋体; font-size: 20px;">记忆中的旋转木马</span></strong></span></p><p style="text-align: left; line-height:
150%;"><span style="color: rgb(178, 162, 199); font-size: 20px;"><strong><span style="line-height: 150%; font-family: 宋体;
font-size: 20px;">/span></strong></span></p><p style="text-align: center; line-height: 150%;"><span style="color: rgb(178,
162, 199); font-size: 20px;"><span style="line-height: 150%; font-family: 宋体; font-size: 20px;"><span style="color: rgb(127, 127,
127); line-height: 150%; font-family: 宋体; font-size:
10px;">（上海迪士尼度假区“幻想曲旋转木马”视频，仅供参考）</span></span></span></p><p style="line-height: 150%;"><span style="color:
rgb(178, 162, 199); font-size: 20px;"><span style="line-height: 150%; font-family: 宋体; font-size: 20px;"><span style="color:
rgb(127, 127, 127); line-height: 150%; font-family: 宋体; font-size: 10px;"></span></span></span> </p><p style="text-align: left;
line-height: 1.5em;"><span style="line-height: 150%; font-family: 宋体; font-size:
16px;">伴随《幻想曲》中的美妙旋律，骑上缤纷多彩的<strong>幻想曲旋转木马</strong>，一圈又一圈回旋，感觉整个世界都缤纷起来了。小朋友们，是否迫不及待想要找到一匹心爱的彩色木马，骑着它旋转；长大后的你，又是否忆起儿时对童话的憧憬与期待？</span></p><p
style="text-align: center; line-height: 150%;"><img
data-src="http://mmbiz.qpic.cn/mmbiz/6SVj4PS2Kh96o61FvEicDC8brU9deGuRgeyqmAz0HyQVxOdYUmSTyTibJ1QjvYGhfG4oNKIXDzy8oveiaxMp1aXkg/0?wx_fmt=jpeg"
data-w="" data-ratio="1" data-type="jpeg" data-s="300,640" class="img_loading"
src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg=="
style="width: 100% !important; "></p><p style="text-align: left; line-height: 150%;"></p><p
style="text-align: left; line-height: 150%;"><span style="color: rgb(178, 162, 199); font-size: 20px;"><strong><span
style="line-height: 150%; font-family: 宋体; font-size: 20px;"></span></strong></span> </p><p style="text-align: left; line-height:
150%;"><span style="color: rgb(178, 162, 199); font-size: 20px;"><strong><span style="line-height: 150%; font-family: 宋体;
font-size: 20px;">心中的那只小飞象</span></strong></span></p><p style="text-align: left; line-height: 150%;"><span
style="line-height: 150%; font-family: 宋体; font-size:
16px;">漫步花园，遇见有着大大耳朵的<strong>小飞象</strong>。你也可以像他一样，顺着梦想，找到内心坚定的力量，和他一起翱翔天空。</span></p><p><img
data-src="http://mmbiz.qpic.cn/mmbiz/6SVj4PS2Kh96o61FvEicDC8brU9deGuRgh2dWTwTPDFRGqicqPBndkVofkCvgznK3gjLeibEGcRZqSXkSX0gPAd4A/0?wx_fmt=jpeg"
data-w="" data-ratio="0.5621414913957935" data-type="jpeg" data-s="300,640" class="img_loading"
src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg=="
style="width: 100% !important; "></p><p><img
data-src="http://mmbiz.qpic.cn/mmbiz/6SVj4PS2Kh96o61FvEicDC8brU9deGuRgSekSoROiarMVRqJfETaqGvy2P0hRFtKAExokWzibzkG8KqKqkOcNdgSg/0?wx_fmt=jpeg"
data-w="" data-ratio="0.5621414913957935" data-type="jpeg" data-s="300,640" class="img_loading"
src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg=="
style="width: 100% !important; "></p><p></p><p style="text-align: left; line-height: 150%;"><span
style="color: rgb(178, 162, 199); font-size: 20px;"><strong><span style="line-height: 150%; font-family: 宋体; font-size:
20px;"></span></strong></span> </p><p style="text-align: left; line-height: 150%;"><span style="color: rgb(178, 162, 199);
font-size: 20px;"><strong><span style="line-height: 150%; font-family: 宋体; font-size:
20px;">一生难忘的花车巡游</span></strong></span></p><p style="text-align: left; line-height: 150%;"><span style="line-height: 150%;
font-family: 宋体; font-size: 16px;">魔法火车头缓缓驶来，米奇、米妮和一大群迪士尼朋友开始巡游乐园。</span></p><p style="text-align:
left; line-height: 150%;"><span style="line-height: 150%; font-family: 宋体; font-size: 16px;"><img
data-src="http://mmbiz.qpic.cn/mmbiz/6SVj4PS2Kh96o61FvEicDC8brU9deGuRgnCeBibavxvYIiaap2u1Huwtn1ydtFlgk4jMRUc7rgwicVZp2NyibNrMckQ/0?wx_fmt=jpeg"
data-w="" data-ratio="0.6653919694072657" data-type="jpeg" data-s="300,640" class="img_loading"
src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg=="
style="width: 100% !important; "></span></p><p style="text-align: left; line-height: 150%;"><span
style="line-height: 150%; font-family: 宋体; font-size: 16px;"></span><span style="line-height: 150%; font-family: 宋体; font-size:
16px;"></span> </p><p style="text-align: left; line-height: 150%;"><span style="line-height: 150%; font-family: 宋体; font-size:
16px;">花车驶来，像是打开了一本无限畅想的动人故事书。</span></p><p style="text-align: left; line-height: 150%;"><span
style="line-height: 150%; font-family: 宋体; font-size: 16px;"><img
data-src="http://mmbiz.qpic.cn/mmbiz/6SVj4PS2Kh96o61FvEicDC8brU9deGuRgXRbszDaPmsD8ibiaqGQ6DTNnlX53C1qC8FkXaTMnxXNicbcZcGf26FXGQ/0?wx_fmt=jpeg"
data-w="" data-ratio="0.6653919694072657" data-type="jpeg" data-s="300,640" class="img_loading"
src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg=="
style="width: 100% !important; "></span></p><p style="text-align: left; line-height: 150%;"><span
style="line-height: 150%; font-family: 宋体; font-size: 16px;"></span> </p><p style="text-align: left; line-height: 150%;"><span
style="line-height: 150%; font-family: 宋体; font-size:
16px;">近距离和故事中的朋友们见面。这样的美好，光是想想都这么幸福与满足。</span></p><p><img
data-src="http://mmbiz.qpic.cn/mmbiz/6SVj4PS2Kh96o61FvEicDC8brU9deGuRgps89IOtmLaoYOTz2jOibGaKDmMuB9nU2ux8boj060CsUsMrqcOQg5Dg/0?wx_fmt=jpeg"
data-w="" data-ratio="0.6634799235181644" data-type="jpeg" data-s="300,640" class="img_loading"
src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg=="
style="width: 100% !important; "></p><p><img
data-src="http://mmbiz.qpic.cn/mmbiz/6SVj4PS2Kh96o61FvEicDC8brU9deGuRgRvsxBvF2ecZibzWPZIViaHcIufKnkWDpU0Ink2q2mHLr0GODxn5GGwmw/0?wx_fmt=jpeg"
data-w="" data-ratio="1.4990439770554493" data-type="jpeg" data-s="300,640" class="img_loading"
src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg=="
style="width: 100% !important; "></p><p></p><p style="text-align: left; line-height: 150%;"><span
style="color: rgb(178, 162, 199); font-size: 20px;"><strong><span style="line-height: 150%; font-family: 宋体; font-size:
20px;"></span></strong></span> </p><p style="text-align: left; line-height: 150%;"><span style="color: rgb(178, 162, 199);
font-size: 20px;"><strong><span style="line-height: 150%; font-family: 宋体; font-size:
20px;">恍然大悟的生肖之谜</span></strong></span></p><p style="line-height: 150%;"><span style="line-height: 150%; font-family: 宋体;
font-size: 16px;">属龙的你或许还不知道，自己的生肖伙伴竟然是《花木兰》里的木须龙？<img
data-src="http://mmbiz.qpic.cn/mmbiz/6SVj4PS2Kh96o61FvEicDC8brU9deGuRgNflUKs6GuPYyVhx3RX6PmCq1xaBiaiazyAH7hfNtGOJZic3iaKtibdicS0ZA/0?wx_fmt=jpeg"
data-w="" data-ratio="1.7762906309751434" data-type="jpeg" data-s="300,640" class="img_loading"
src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg=="
style="width: 100% !important; "></span></p><p style="text-align: center; line-height: 150%;"><span
style="color: rgb(127, 127, 127); line-height: 150%; font-family: 宋体; font-size: 12px;">（吼吼~你会在乐园里找到我吗？
&gt;.&lt;）</span></p><p style="line-height: 150%;"><span style="line-height: 150%; font-family: 宋体; font-size: 16px;"><span
style="color: rgb(127, 127, 127); line-height: 150%; font-family: 宋体; font-size: 10px;"></span></span> </p><p style="line-height:
150%;"><span style="line-height: 150%; font-family: 宋体; font-size:
16px;">来<strong>十二朋友园</strong>，找找自己的生肖伙伴，和TA一起合影留念。</span></p><p style="text-align: center; line-height:
150%;"><img
data-src="http://mmbiz.qpic.cn/mmbiz/6SVj4PS2Kh96o61FvEicDC8brU9deGuRgT1H4wic1eZ5O8Isr2C2An408jGaOFYBNEvyfGHYhNhTHKFzFKGBhKVA/0?wx_fmt=jpeg"
data-w="" data-ratio="0.6653919694072657" data-type="jpeg" data-s="300,640" class="img_loading"
src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg=="
style="width: 100% !important; "></p><p style="text-align: left; line-height: 150%;"><strong><span
style="line-height: 150%; font-family: 宋体; font-size: 19px;"></span></strong> </p><p style="text-align: left; line-height:
150%;"><br></p><p style="text-align: left; line-height: 150%;"><span style="color: rgb(178, 162, 199); font-size:
20px;"><strong><span style="line-height: 150%; font-family: 宋体; font-size: 20px;">美食美景，美不胜收</span></strong></span></p><p
style="text-align: left; line-height: 150%;"><span style="line-height: 150%; font-family: 宋体; font-size:
16px;">在<strong>漫月轩</strong>这间超然脱俗的中式餐厅，享用美味佳肴的同时，<strong>奇幻童话城堡</strong>的迷人景致映入眼帘。美食美景，美不胜收。</span></p><p><img
data-src="http://mmbiz.qpic.cn/mmbiz/6SVj4PS2Kh96o61FvEicDC8brU9deGuRgGAMGGicfZx9WAP7YnbiaGicqGds6enFKwouDGRibEbT1vyvjA0K6PpvMPw/0?wx_fmt=jpeg"
data-w="" data-ratio="0.609942638623327" data-type="jpeg" data-s="300,640" class="img_loading"
src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg=="
style="width: 100% !important; "></p><p><img
data-src="http://mmbiz.qpic.cn/mmbiz/6SVj4PS2Kh96o61FvEicDC8brU9deGuRgQSwkhAknCsgthroetse2bgllNicDib6xib3bfUAhew09dKOPQANeIviafQ/0?wx_fmt=jpeg"
data-w="" data-ratio="0.655831739961759" data-type="jpeg" data-s="300,640" class="img_loading"
src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg=="
style="width: 100% !important; "></p><p style="text-align: left; line-height: 150%;"><span
style="line-height: 150%; font-family: 宋体; font-size: 16px;"></span> </p><p style="text-align: left; line-height: 150%;"><a
href="http://triowt3.1to1crm.com.cn/web_service/counter/webmax_ad.aspx?DisneyCN:estorybook:Officialwechat" target="_blank"
send_referrer="false"
data_ue_src="http://triowt3.1to1crm.com.cn/web_service/counter/webmax_ad.aspx?DisneyCN:estorybook:Officialwechat"><strong><span
style="line-height: 150%; font-family: 宋体; font-size: 16px;">点击此处</span></strong></a><span style="line-height: 150%;
font-family: 宋体; font-size: 16px;">，走进<strong>奇想花园</strong></span><span style="line-height: 150%; font-family: 宋体;
font-size: 16px;">，欢乐畅游，感受奇思妙想中的小确幸。</span> </p><p style="text-align: left; line-height: 150%;"><img width="100%"
height="74" style="width: 100% !important;"
data-src="http://mmbiz.qpic.cn/mmbiz/6SVj4PS2Kh96o61FvEicDC8brU9deGuRgK2eicX9bXWWOCNVBmCJNDzNicXO7Gx5yfOoWznhQhtDw2ZGfwiavDNZ0A/0?wx_fmt=gif"
data-w="482" data-ratio="1" data-type="gif" _width="100%" class="img_loading __bg_gif"
src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg=="
data-order="1"></p>
                </div>'''
    },
    "menghuan": {
        "title": u"梦幻乐园",
        "content": u'''<h3 style="text-align:center">梦幻乐了个园</h3>
<p>
<img src="http://mmbiz.qpic.cn/mmbiz/6Ht0iasBR9AzHwNqumrQvZ3f0pB8tCm2P5F62DpLb2kYzicvKUWkKsu7iaqQhTqvibcMRBnia5KmPtKh7y107PibaePw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1" width="100%">
</p>
<p>

伍德沃德介绍，这些壁画分别展示了化身中国十二生肖的迪士尼动画角色。“2016年是中国的猴年，相信以阿拉丁神灯中可爱的猴子阿布的角色为主题的壁画，将在上海迪士尼开幕后受到中国游客欢迎。”
</p>

<p>
游客还能在乐园内买到特别为中国游客设计及专门为上海迪士尼度假区设计的独家商品。其中，有身着中国传统服饰的米奇米妮玩偶、以中国古代食盒为外形包装的点心等等。
</p>'''
    },
    "shiziwang": {
        "title": u"<<狮子王>>演出",
        "content": u'''<h3 style="text-align:center">狮子王演出活动</h3>
<p>
<img src="http://mmbiz.qpic.cn/mmbiz/6Ht0iasBR9AzHwNqumrQvZ3f0pB8tCm2P5F62DpLb2kYzicvKUWkKsu7iaqQhTqvibcMRBnia5KmPtKh7y107PibaePw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1" width="100%">
</p>
<p>

伍德沃德介绍，这些壁画分别展示了化身中国十二生肖的迪士尼动画角色。“2016年是中国的猴年，相信以阿拉丁神灯中可爱的猴子阿布的角色为主题的壁画，将在上海迪士尼开幕后受到中国游客欢迎。”
</p>

<p>
游客还能在乐园内买到特别为中国游客设计及专门为上海迪士尼度假区设计的独家商品。其中，有身着中国传统服饰的米奇米妮玩偶、以中国古代食盒为外形包装的点心等等。
</p>'''
    },
    "shuishang": {
        "title": u"水上游玩",
        "content": u'''<h3 style="text-align:center">水上游玩攻略</h3>
<p>
<img src="http://mmbiz.qpic.cn/mmbiz/6Ht0iasBR9AzHwNqumrQvZ3f0pB8tCm2P5F62DpLb2kYzicvKUWkKsu7iaqQhTqvibcMRBnia5KmPtKh7y107PibaePw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1" width="100%">
</p>
<p>

伍德沃德介绍，这些壁画分别展示了化身中国十二生肖的迪士尼动画角色。“2016年是中国的猴年，相信以阿拉丁神灯中可爱的猴子阿布的角色为主题的壁画，将在上海迪士尼开幕后受到中国游客欢迎。”
</p>

<p>
游客还能在乐园内买到特别为中国游客设计及专门为上海迪士尼度假区设计的独家商品。其中，有身着中国传统服饰的米奇米妮玩偶、以中国古代食盒为外形包装的点心等等。
</p>'''
    }
}
