from tools001 import mark001_decode

def main():
    # 多個郵箱的範例
    src="""
        =?UTF-8?B?b3Jn5ris6Kmm5LqM6JmfbWFpbGJveA==?= <s2@skyrock-casting.org>, 
        =?UTF-8?B?b3Jn5ris6Kmm5LiA?= <s1@skyrock-casting.org>, 
        =?UTF-8?B?5piG5bGx5a+M6YimTWFya+mZsw==?= <mark.chen@fulltech-metal.com>
        """
    # Subject 裡有中英文和空白    
    # src="""
    #     =?UTF-8?B?5Li76aGMIOWwseaYryBTdWJqZXQsIOWcqOa4rOepuueZveeahOWVj+mhjA==?=
    #     """
    print (mark001_decode(src))
if __name__ == "__main__":
    main()
