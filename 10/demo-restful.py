# restful api
# 一种API的设计方式
# http://www.ruanyifeng.com/blog/2011/09/restful.html

# 一般：
@app.route(add)
    sql = 'insert xxx'
    Host().add(sql)
@app.route(list)
    Host().list()
@app.route(del)
    Host().del(id)
@app.route(search)

@app.route(update)


# http method
@app.route('host', method=['get', 'post', 'del', 'put'])
def host():
    if request.method == 'get':
        render_template('host.html')
    elif del:
        # method == 'del'
        # args -- GET  del post 有其他方法
        id = request.args
    elif post:


有两个问题：@狂奔的~蜗牛~~ 
1. 能否介绍一下 RESTful

2. Web 研发模式演变 中提到的Web开发模式，能否讲解一下。MVC SPA和MV*的具体应用场景。
https://github.com/lifesinger/blog/issues/184

http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140262673295076f525af00734a8e924c5fc6ff5b6091000

mvc
    view 展现层

    controller 逻辑层 控制器 (急哦啊哈)

    model 数据层 和数据库交互的
        orm
    
    www
        model


    view层和model严格分开

mvvm (mv*)
    model
    view
    view-model

angular 1.2
前端模板
    baidu template