

url管理模块
	待抓取的url
	已经抓取的url

url内容下载
	request

html内容解析
	pyquery

	.feed-main下面寻找需要的三个数据
		链接：
			<a class="question_link" target="_blank" href="/question/28626263">哪些素质很重要，却是读书学不来的？</a>
			<a class="zm-item-vote-count js-expand js-vote-count" href="javascript:;" data-votecount="88354">88K</a>

控制器，控制具体的逻辑


	
用class来组织整个代码


url：http://www.zhihu.com/topic/19776749/top-answers
	 http://www.zhihu.com/topic/19776749/top-answers?page=2
	 for page in range(1,6):



画图：
	处理的log，入库，根据http状态画饼图

http://api.map.baidu.com/location/ip
	?
	ak=E4805d16520de693a3fe707cdc962045&
	ip=202.198.16.3&

	coor=bd09ll

大于200，强
10-200 中
10以下 弱

{
	high:[]
	mid:[]
	low:[]
}

作业 实现效果http://echarts.baidu.com/echarts2/doc/example/map11.html

	所有404状态都去上海
	所有的200状态，都去北京

	北京:[116.4551,40.2539]
	上海:[121.4648,31.2891]