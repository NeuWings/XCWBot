import random
# from datetime import timedelta

from nonebot import on_command, CommandSession
from hoshino import util
from hoshino.res import R
from hoshino.service import Service, Privilege as Priv
from nonebot import permission as perm

# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'))
async def say_hello(session):
    await session.send('buzai，cmn')

sv = Service('chat', manage_priv=Priv.SUPERUSER, visible=False)

# @sv.on_command('沙雕机器人', aliases=('沙雕機器人',), only_to_me=False)
# async def say_sorry(session):
#     await session.send('ごめんなさい！嘤嘤嘤(〒︿〒)')


@sv.on_command(
    '老婆',
    aliases=('waifu', 'laopo', 'mua~', '我老婆'),
    only_to_me=True
)
async def chat_waifu(session):
    if not sv.check_priv(session.ctx, Priv.SUPERUSER):
        await session.send(R.img('laopo.jpg').cqcode)
        await session.send('爪巴')
    else:
        await session.send('mua~')


@on_command('sleep_6h', aliases=('晚安', '晚安安'), permission=perm.GROUP)
async def sleep_8h(session: CommandSession):
    if not sv.check_priv(session.ctx, Priv.SUPERUSER):
        await session.send('爪巴')
    else:
        await session.send('晚安mua~')
    await util.silence(session.ctx, 6*60*60, ignore_super_user=True)


@sv.on_command('老公', only_to_me=True)
async def chat_laogong(session):
    await session.send('你给我滚！', at_sender=True)

# @sv.on_command('mua', only_to_me=True)
# async def chat_mua(session):
#     await session.send('笨蛋~', at_sender=True)


@sv.on_command('我有个朋友说他好了', aliases=('我朋友说他好了', ), only_to_me=False)
async def ddhaole(session):
    await session.send('那个朋友是不是你妹妹？')
    await util.silence(session.ctx, 30)


@sv.on_command('我好了', only_to_me=False)
async def nihaole(session):
    await session.send('不许好，憋回去！')
    await util.silence(session.ctx, 30)


@sv.on_command('喷水', aliases=('太虚苍蓝闪', '太虚苍蓝闪！', '宇宙蓝色闪光'))
async def penshui(session):
    await session.send(R.img('喷水.jpg').cqcode)


@sv.on_command('比划比划', aliases=('来比划比划'))
async def bihua(session):
    await session.send(R.img('比划比划.gif').cqcode)

# ============================================ #


@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, R.img('确实.jpg').cqcode)


@sv.on_keyword(('催刀'))
async def chat_clanba(bot, ctx):
    await bot.send(ctx, R.img('我的天啊你看看都几点了.jpg').cqcode)


@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    await bot.send(ctx, R.img('内鬼.png').cqcode)
