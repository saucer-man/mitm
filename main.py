import mitmproxy.http
from loguru import logger

# 所有发出的请求数据包都会被这个方法所处理
# 所谓的处理，我们这里只是打印一下一些项；当然可以修改这些项的值直接给这些项赋值即可
def request(flow: mitmproxy.http.HTTPFlow):
    # # 获取请求对象
    # request = flow.request
    #
    # # 打印请求的url
    # logger.info(request.url)
    # # 打印请求方法
    # logger.info(request.method)
    # # 打印host头
    # logger.info(request.host)
    # # 打印请求端口
    # logger.info(str(request.port))
    # # 打印所有请求头部
    # logger.info(str(request.headers))
    # # 打印cookie头
    # logger.info(str(request.cookies))
    pass


# 所有服务器响应的数据包都会被这个方法处理
# 所谓的处理，我们这里只是打印一下一些项
def response(flow: mitmproxy.http.HTTPFlow):
    # # 获取响应对象
    # response = flow.response
    #
    # # 打印响应码
    # logger.info(str(response.status_code))
    # # 打印所有头部
    # logger.info(str(response.headers))
    # # 打印cookie头部
    # logger.info(str(response.cookies))
    # # 打印响应报文内容
    # logger.info(str(response.text))

    # logger.debug(flow.request.url)

    if "lottery/limitcouponcomponent/getTime" in flow.request.url:
        logger.info(flow.response.text)
        flow.response.set_text('{"code":0,"subcode":0,"msg":"success","data":1690707733000}')
        logger.info("已经替换")



