from wxpy import *
from wxpy.api import bot
import re

# 自动添加好友时 好友的验证信息需要包括的关键词
ADD_FRIENDS_VERIFY_KEYWORD = ['招聘', '应聘', '招人', '职位',  '岗位']
# 添加好友之后第一次打招呼
NEW_FRIENDS_CHAT0 = '我接受了您的好友请求'
NEW_FRIENDS_CHAT1 = '为了方便给您发送职位信息，您可以将您的职位信息通过 【职位-期望薪资-姓名-手机号】 的方式发给我么'


class WeChat:
    def __init__(self):
        self.bot = Bot(console_qr=2, cache_path=True)
        self.wx_friends = self.bot.friends()
        self.wx_groups = self.bot.groups()
        self.wx_mps = self.bot.mps()
        self.chats = self.bot.chats()

    # 自动接受加好友请求
    @bot.register(msg_types=FRIENDS):
    # 自动接受认证信息中包含'wxpy'的好友的请求
    def auto_accept_friends(self, msg):
        verify_msg = re.sub('\s', '', msg.text.lower()).strip()
        for verify_keyword in ADD_FRIENDS_VERIFY_KEYWORD:
            if verify_keyword in verify_msg:
                new_friend = msg.card.accept()
                # 接受好友之后要求发送信息
                new_friend.send(NEW_FRIENDS_CHAT0)
                new_friend.send(NEW_FRIENDS_CHAT1)
                new_friend.send_image('emoji/flower_to_you.jpg')

