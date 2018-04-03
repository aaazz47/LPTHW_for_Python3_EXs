def counting_download_time(bandwidth, size):
    bandwidth_KByte = bandwidth * 1024
    download_bandwidth_KBs = bandwidth_KByte / 8
    need_time = size / download_bandwidth_KBs / 60
    print("带宽 %d Mbit ,下载 %d MByte 的文件需要用时约： %.2f 小时" % (
        bandwidth, size, need_time))


# 计算 22Mbit 带宽，下载 10GByte 文件所需时间
counting_download_time(22, 1024000)
