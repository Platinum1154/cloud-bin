import time
import requests
import urllib.request

def check_ip_location():
    print("\n" + "="*45)
    print(" 🌐 当前 IP 与位置信息")
    print("="*45)
    try:
        response = requests.get('http://ip-api.com/json/', timeout=10)
        data = response.json()
        if data.get('status') == 'success':
            print(f" 🔹 IP 地址   : {data.get('query', 'N/A')}")
            print(f" 🔹 国家/地区 : {data.get('country', 'N/A')} ({data.get('countryCode', 'N/A')})")
            print(f" 🔹 城市      : {data.get('city', 'N/A')}, {data.get('regionName', 'N/A')}")
            print(f" 🔹 运营商    : {data.get('isp', 'N/A')}")
            print(f" 🔹 机构/ASN  : {data.get('org', '')} / {data.get('as', '')}".strip(" /"))
        else:
            print(" ❌ 获取 IP 信息失败。")
    except Exception as e:
        print(f" ❌ IP 获取异常: {e}")

def ustc_speedtest():
    print("\n" + "="*45)
    print(" ⚡ 中科大 (USTC) 境内路由测速")
    print("="*45)
    url = "https://mirrors.ustc.edu.cn/debian/ls-lR.gz"
    try:
        start_time = time.time()
        response = urllib.request.urlopen(url, timeout=15)
        raw_data = response.read()
        end_time = time.time()
        
        file_size_mb = len(raw_data) / (1024 * 1024)
        duration = end_time - start_time
        speed_mbps = (file_size_mb * 8) / duration
        
        print(f" 🔹 测试文件 : {file_size_mb:.2f} MB")
        print(f" 🔹 下载耗时 : {duration:.2f} 秒")
        print(f" ⬇️  下载速度 : {speed_mbps:.2f} Mbps")  # 已将“等效带宽”更改为更直观的“下载速度”
    except Exception as e:
        print(f" ❌ 中科大测速请求失败: {e}")
def fast_speedtest():
    print("\n" + "="*45)
    print(" 🚀 Fast.com (Netflix) 国际流媒体测速")
    print("="*45)
    try:
        from fastdotcom import fast_com
        print(" ⏳ 正在连接 Netflix 服务器进行测速 (请稍候)...\n")
        speed_data = fast_com()
        
        # 专门解析字典格式的返回值，使其清晰可读
        if isinstance(speed_data, dict) and speed_data.get('success'):
            down_speed = speed_data.get('download_speed', 0)
            up_speed = speed_data.get('upload_speed', 0)
            ping_unloaded = speed_data.get('unloaded_ping', 0)
            ping_loaded = speed_data.get('loaded_ping', 0)
            
            print(f" ⬇️  下载速度   : {down_speed:.2f} Mbps")
            if up_speed > 0:
                print(f" ⬆️  上传速度   : {up_speed:.2f} Mbps")
            print(f" 📶 延迟(空闲) : {ping_unloaded} ms")
            if ping_loaded > 0:
                print(f" 📶 延迟(负载) : {ping_loaded} ms")
                
        elif isinstance(speed_data, (int, float)):
            # 兼容旧版本库可能只返回单一数字的情况
            print(f" ⬇️  下载速度   : {speed_data:.2f} Mbps")
        else:
             print(f" ⚠️ 返回数据格式异常: {speed_data}")

    except ImportError:
        print(" ❌ 缺少依赖库。请在终端执行: pip install fastdotcom")
    except Exception as e:
        print(f" ❌ Fast.com 测速失败: {e}")
    print("="*45 + "\n")

if __name__ == "__main__":
    check_ip_location()
    ustc_speedtest()
    fast_speedtest()