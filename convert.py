import requests
import re

# 源文件的URL
SOURCE_URL = 'https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf'
# 转换后生成的文件名
OUTPUT_FILE = 'chinalist.txt'

def main():
    try:
        # 1. 下载源文件
        print(f"正在从 {SOURCE_URL} 下载文件...")
        response = requests.get(SOURCE_URL)
        response.raise_for_status() # 如果下载失败则抛出异常
        content = response.text
        print("文件下载成功。")

        # 2. 解析并转换内容
        print("正在转换文件格式...")
        domains = []
        # 使用正则表达式匹配 server=/.domain.com/ 格式的域名
        pattern = re.compile(r'server=/\.(.*?)/')
        for line in content.splitlines():
            match = pattern.search(line)
            if match:
                domains.append(match.group(1))
        
        # 3. 写入新文件
        print(f"正在生成 {OUTPUT_FILE}...")
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            for domain in sorted(set(domains)): # 使用set去重，然后排序
                f.write(domain + '\n')
        
        print(f"成功！共转换了 {len(domains)} 条规则。")

    except Exception as e:
        print(f"发生错误: {e}")
        exit(1)

if __name__ == '__main__':
    main()
