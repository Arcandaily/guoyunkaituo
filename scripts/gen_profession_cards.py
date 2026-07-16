#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "obsidian_vault" / "09-职业体系" / "职业卡片"

cards = [
    dict(
        file="指挥-舰队总指挥.md",
        title="舰队总指挥",
        cat="指挥与参谋",
        rare="常见",
        src="拉格朗日旗舰/集火指令；SC指挥官；战锤舰长；群星海军将领",
        daily="拆解阶段目标、分配编队、拍板进退",
        battle="集火优先级、撤退线、与政委协同纪律",
        unique="一人定阶段节奏",
        A="A4军事 A5协作",
        B="B1岗位 B2抗压",
        Anote="国运胜负手",
        Bnote="崩指挥最伤编制印象",
        vols="全卷；V03/V05/V10升高",
        license="开拓→猎人线",
        huaguo="ID1 龙旗-总指挥 正式席",
        team="参谋、政委、前排",
    ),
    dict(
        file="指挥-作战参谋.md",
        title="作战参谋",
        cat="指挥与参谋",
        rare="常见",
        src="拉格朗日情报转作战计划；SC推进决策；战锤参谋部",
        daily="敌我对比表、航路与时间窗",
        battle="提供方案不抢指挥权",
        unique="把情报变成可执行命令",
        A="A4 A2",
        B="B1 B3",
        Anote="提升军事与控制决策质量",
        Bnote="协作不抢功",
        vols="全卷",
        license="开拓",
        huaguo="可由侦察/副指挥兼",
        team="总指挥、情报",
    ),
    dict(
        file="战斗-前排舰长.md",
        title="前排舰长",
        cat="舰船战斗",
        rare="常见",
        src="拉格朗日前排护卫（FG300装甲）；站位坦克；SC前线单位",
        daily="护航工程、训练损管",
        battle="挡刀、拉仇恨、护矿护运",
        unique="工程线存活率",
        A="A4 主；间接A3",
        B="B1 B2",
        Anote="护矿=后勤安全",
        Bnote="硬仗岗位",
        vols="V01起刚需",
        license="开拓",
        huaguo="ID3 龙旗-前排",
        team="工程、输出舰",
    ),
    dict(
        file="战斗-输出与防空指挥.md",
        title="输出与防空指挥",
        cat="舰船战斗",
        rare="常见",
        src="拉格朗日中后排投射/防空、反击防空；CAS066/导弹舰",
        daily="弹药与冷却节奏、防空编组",
        battle="清野、反舰载机、护航火力",
        unique="锈环/航路清场",
        A="A4",
        B="B1",
        Anote="战果",
        Bnote="本职输出",
        vols="全卷；V06航路升高",
        license="开拓",
        huaguo="可与前排分岗或中期增设",
        team="前排、航空",
    ),
    dict(
        file="战斗-舰载机联队长.md",
        title="舰载机联队长",
        cat="舰船战斗",
        rare="常见",
        src="拉格朗日战机/护航艇、载机巡洋（KCCP）；SC空中单位",
        daily="联队保养、起降调度",
        battle="对舰突防、防空协同",
        unique="载机体系成型后的弹性火力",
        A="A4",
        B="B1 B5",
        Anote="中后期战果",
        Bnote="载机操作为稀缺操作",
        vols="V01中后；V06/V10",
        license="开拓/猎人",
        huaguo="ID9 龙旗-航空",
        team="KCCP舰长、防空",
    ),
    dict(
        file="工程-采矿总监.md",
        title="采矿总监",
        cat="工程与工业",
        rare="常见",
        src="拉格朗日X8/X10/X20工程舰；SC SCV；群星矿工",
        daily="矿点排班、工程编队路线",
        battle="遇袭时保工程撤退",
        unique="金属/晶体/重氢不断供",
        A="A3 A1",
        B="B1",
        Anote="工业命脉+协议产量",
        Bnote="稳定产出=岗位胜任",
        vols="全卷命脉",
        license="开拓/勘探",
        huaguo="ID8 龙旗-采矿",
        team="船坞、后勤、前排护航",
    ),
    dict(
        file="工程-船坞总工.md",
        title="船坞总工",
        cat="工程与工业",
        rare="常见",
        src="拉格朗日船坞建造与蓝图落地；SC星港；战锤船坞",
        daily="建造队列、模块安装、维修坞",
        battle="抢修返场",
        unique="把资源变成舰队",
        A="A3 A1",
        B="B1",
        Anote="产能=国运底气",
        Bnote="船坞事故最伤信任",
        vols="全卷；V08加工线交叉",
        license="开拓",
        huaguo="ID5 龙旗-工程",
        team="采矿、科研蓝图",
    ),
    dict(
        file="科研-蓝图研究员.md",
        title="蓝图研究员",
        cat="科研与蓝图",
        rare="常见",
        src="拉格朗日蓝图研究、技术档案、武器技术插件",
        daily="研究度推进、插件取舍",
        battle="临时调校建议",
        unique="解锁船型与强度",
        A="A1",
        B="B5 B1",
        Anote="协议科技交付",
        Bnote="稀缺研究能力",
        vols="V01中；V02/V04/V08高",
        license="勘探",
        huaguo="可兼或单列；与ID11交叉",
        team="船坞、开箱策略",
    ),
    dict(
        file="科研-遗迹数据解析官.md",
        title="遗迹数据解析官",
        cat="科研与蓝图",
        rare="稀缺",
        src="拉格朗日数据抢救/遗迹；群星异常研究",
        daily="黑匣与节点数据清洗",
        battle="战场临时破译",
        unique="V02/V05关键交付",
        A="A1 A2",
        B="B5",
        Anote="数据交付=协议分",
        Bnote="人联爱要的稀缺脑",
        vols="V02 V05 主；他卷弱",
        license="勘探/猎人",
        huaguo="可由科研兼；后期升专",
        team="情报、特种渗透",
    ),
    dict(
        file="医疗-舰医.md",
        title="舰医",
        cat="医疗与生命支持",
        rare="常见",
        src="SC医疗兵；战锤药剂师；群星医疗岗；拉格朗日生存/支援",
        daily="伤病、辐射、减压损伤",
        battle="战地急救、减员控制",
        unique="人还在就能再战",
        A="A3",
        B="B2 B3",
        Anote="可持续",
        Bnote="危机救人=抗压+协作",
        vols="全卷；撤离/虫/净化升",
        license="开拓",
        huaguo="ID6 龙旗-医疗",
        team="生命维持、政委心理",
    ),
    dict(
        file="情报-侦察舰长.md",
        title="侦察舰长",
        cat="情报与电战",
        rare="常见",
        src="拉格朗日侦察护卫、空间站/私掠情报；SC扫描",
        daily="矿图、敌情、他国动向",
        battle="引导伏击与反伏击",
        unique="A2控制的前置眼",
        A="A2 A1",
        B="B5 B1",
        Anote="无侦察则盲抢点",
        Bnote="情报稀缺",
        vols="V01起；碎带/净化高",
        license="勘探",
        huaguo="ID4 龙旗-侦察",
        team="总指挥、电战",
    ),
    dict(
        file="情报-电战官.md",
        title="电战官",
        cat="情报与电战",
        rare="稀缺",
        src="拉格朗日干扰/电子类技能；SC干扰；V07智械净网",
        daily="频谱与密钥、反侦察",
        battle="干扰敌火控、破译逻辑",
        unique="V07净网核心",
        A="A4 A1",
        B="B5 B4",
        Anote="特殊战役",
        Bnote="稀缺+守序（不滥黑友军）",
        vols="V07主；V01弱",
        license="猎人",
        huaguo="中期由侦察分化或增援",
        team="科研、特种净网",
    ),
    dict(
        file="后勤-后勤总监.md",
        title="后勤总监",
        cat="后勤与贸易",
        rare="常见",
        src="拉格朗日仓储/维修/交易中心；SC补给；群星行政商人",
        daily="公库四国资源、维修排程",
        battle="弹药与备件前送",
        unique="纪律的数字化",
        A="A3",
        B="B3 B1",
        Anote="不断供",
        Bnote="肯交公库=协作",
        vols="全卷；V03/V04/V08极高",
        license="开拓",
        huaguo="ID2 龙旗-后勤",
        team="采矿、贸易、政委审计",
    ),
    dict(
        file="后勤-贸易与采购官.md",
        title="贸易与采购官",
        cat="后勤与贸易",
        rare="常见",
        src="拉格朗日联络站、星际商队、电子货币；群星贸易",
        daily="中立站采购、卖多余矿",
        battle="战时紧急采购",
        unique="补短板资源",
        A="A3 A5",
        B="B3 B6",
        Anote="贸易可弱协议分",
        Bnote="观察员可见的合规交易",
        vols="V01贸易萌芽起",
        license="对话",
        huaguo="后勤副职或外交兼",
        team="后勤总监、外交",
    ),
    dict(
        file="外交-首席外交官.md",
        title="首席外交官",
        cat="外交交涉",
        rare="常见",
        src="拉格朗日联合体/同盟；群星使节与联邦声誉；SC临时同盟",
        daily="谈判矿权、停火、联防",
        battle="战场临时协定",
        unique="A5协作与背刺防线",
        A="A5",
        B="B3 B6",
        Anote="履约=国运",
        Bnote="人联看你是否可共事",
        vols="全卷；V06/V09/V10高",
        license="对话",
        huaguo="ID7 龙旗-外交",
        team="总指挥、政委",
    ),
    dict(
        file="政工-政委.md",
        title="政委",
        cat="政工法务",
        rare="常见",
        src="战锤政委（纪律与士气，克制移植）；国运团结看点；群星统一",
        daily="纪律、士气、公库监督、防内讧",
        battle="稳住崩溃边缘",
        unique="华国国运戏核心岗",
        A="A5 A6",
        B="B4 B3",
        Anote="团结与克制展示",
        Bnote="守序一票否决相关",
        vols="华国全卷高光",
        license="开拓/对话",
        huaguo="ID10 龙旗-政委 正式席",
        team="总指挥、法务、医疗心理",
    ),
    dict(
        file="政工-考核法务官.md",
        title="考核法务官",
        cat="政工法务",
        rare="常见",
        src="拉格朗日协议合规；群星法律；人联考核规则",
        daily="协议条款解读、控制证明等证据链",
        battle="战场取证、防止违规屠戮",
        unique="参评材料合法",
        A="A1 A5",
        B="B4",
        Anote="协议完成度证据",
        Bnote="守序",
        vols="每卷评定前升高",
        license="对话",
        huaguo="政委兼或外交兼",
        team="政委、后勤审计",
    ),
    dict(
        file="特种-登陆突击队长.md",
        title="登陆突击队长",
        cat="特种作战",
        rare="稀缺",
        src="拉格朗日登陆舰/两栖；SC陆战；V06/V09空间站近战",
        daily="破拆训练、登舰演练",
        battle="站体/残骸近战清理",
        unique="节点近距夺取",
        A="A4 A2",
        B="B5 B2",
        Anote="关键点",
        Bnote="稀缺突击",
        vols="V06 V09 主",
        license="猎人",
        huaguo="由前排转型",
        team="前排、情报",
    ),
    dict(
        file="特种-反虫战术官.md",
        title="反虫战术官",
        cat="特种作战",
        rare="卷限定",
        src="战锤死亡守望感；SC虫族作战；V05碎星坟场",
        daily="生物威胁预案、隔离",
        battle="虫潮薄弱点与火力纪律",
        unique="V05存活关键",
        A="A4 A5",
        B="B5 B2 B4",
        Anote="协同防火",
        Bnote="稀缺+不恐慌屠平民",
        vols="V05 主；V10弱复用",
        license="猎人/预备役",
        huaguo="战斗/医疗/科研临时编制",
        team="医疗防疫、输出",
    ),
    dict(
        file="特种-净网渗透客.md",
        title="净网渗透客",
        cat="特种作战",
        rare="卷限定",
        src="拉格朗日净化协议环境；战锤失控机械感；电战延伸",
        daily="逻辑防火墙、隔离网段",
        battle="关枢纽、清污染源",
        unique="V07胜负手之一",
        A="A1 A4",
        B="B5 B4",
        Anote="净化进度",
        Bnote="抗逻辑腐蚀",
        vols="V07 主",
        license="猎人/预备役",
        huaguo="电战+科研联合",
        team="电战官、蓝图研究员",
    ),
    dict(
        file="特种-亚空间防护专员.md",
        title="亚空间防护专员",
        cat="特种作战",
        rare="卷限定",
        src="战锤亚空间/恶魔防护编制感；V10断界棱堡",
        daily="防护阵列、精神与物理双重隔离规程",
        battle="裂隙出现时的封控",
        unique="B4一票否决相关场景",
        A="A4 A5",
        B="B4 B5 B2",
        Anote="前线不崩",
        Bnote="守序可信核心",
        vols="V10 主；V05-9预兆",
        license="预备役优先",
        huaguo="后期专设或政委+科研共管",
        team="政委、医疗、总指挥",
    ),
    dict(
        file="融合-修科顾问.md",
        title="修科融合顾问",
        cat="特种作战",
        rare="稀缺",
        src="小说原创金手指；对接拉格朗日工程/药剂/插件思路；非游戏单位",
        daily="低灵环境下小优化（无人机路径、修复剂、铭刻散热）",
        battle="救急方案；禁止天天放大招清图",
        unique="B5不可复制",
        A="A3 A6弱",
        B="B5 B1",
        Anote="效率与展示弱",
        Bnote="人联观察焦点",
        vols="全卷；随晶体/遗迹强化",
        license="特例观察→预备役",
        huaguo="ID11 第11席",
        team="工程、医疗、科研",
    ),
]


def render(c: dict) -> str:
    return f"""---
tags: [职业, 卡片]
大类: {c['cat']}
稀缺度: {c['rare']}
---

# 职业 · {c['title']}

## 灵感来源（必填）

- 对标：{c['src']}
- 提取：职能与场景，非照搬专有名词堆砌

## 职责（考核内）

- 日常：{c['daily']}
- 战役：{c['battle']}
- 不可替代点：{c['unique']}

## 双轨评分贡献

| 轨道 | 主要子项 | 说明 |
|------|----------|------|
| A 国运 | {c['A']} | {c['Anote']} |
| B 战友 | {c['B']} | {c['Bnote']} |

## 适配卷次

- {c['vols']}

## 编制与执照

- 易导向：{c['license']}（见 [[执照与编制晋升]]）
- 人联编制：高 B 且守序者优先观察

## 华国席位建议

- {c['huaguo']}
- 常组队：{c['team']}

## 禁止事项

- 勿写成现代办公室岗位；须落到舰/矿/站/协议场景
- 数值与舰船以 `wiki_data` 为准

## 交叉链接

- [[职业总览MOC]] [[选拔与编队逻辑]] [[大类-{c['cat']}]] [[双轨评分逻辑]]
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for c in cards:
        path = OUT / c["file"]
        path.write_text(render(c), encoding="utf-8")
        print("wrote", path.name)
    # index
    lines = [
        "---",
        "tags: [职业, 索引]",
        "---",
        "",
        "# 职业卡片索引（R6）",
        "",
        f"共 {len(cards)} 张。模板：[[_职业卡片模板]]",
        "",
        "## A 批（指挥/战斗/工程/科研/医疗）",
        "",
    ]
    a_prefix = ("指挥-", "战斗-", "工程-", "科研-", "医疗-")
    b_prefix = ("情报-", "后勤-", "外交-", "政工-", "特种-", "融合-")
    for c in cards:
        if c["file"].startswith(a_prefix):
            lines.append(f"- [[{c['file'].replace('.md','')}|{c['title']}]] · {c['cat']} · A:{c['A']} / B:{c['B']}")
    lines += ["", "## B 批（情报/后勤/外交/政工/特种/融合）", ""]
    for c in cards:
        if c["file"].startswith(b_prefix):
            lines.append(f"- [[{c['file'].replace('.md','')}|{c['title']}]] · {c['cat']} · A:{c['A']} / B:{c['B']}")
    lines += ["", "## 交叉", "", "- [[职业总览MOC]] [[选拔与编队逻辑]]", ""]
    # Obsidian links work better with title as filename without path - use title based links
    # Fix: file names have Chinese, link by filename stem
    idx = OUT / "00-职业卡片索引.md"
    # rewrite links properly
    lines = [
        "---",
        "tags: [职业, 索引]",
        "---",
        "",
        "# 职业卡片索引（R6）",
        "",
        f"共 **{len(cards)}** 张。模板：[[_职业卡片模板]]",
        "",
        "## A 批（指挥 / 战斗 / 工程 / 科研 / 医疗）",
        "",
    ]
    for c in cards:
        if c["file"].startswith(a_prefix):
            stem = c["file"][:-3]
            lines.append(f"- [[{stem}]] — {c['cat']}｜A `{c['A']}`｜B `{c['B']}`")
    lines += ["", "## B 批（情报 / 后勤 / 外交 / 政工 / 特种 / 融合）", ""]
    for c in cards:
        if c["file"].startswith(b_prefix):
            stem = c["file"][:-3]
            lines.append(f"- [[{stem}]] — {c['cat']}｜A `{c['A']}`｜B `{c['B']}`")
    lines += ["", "→ [[职业总览MOC]] · [[选拔与编队逻辑]]", ""]
    idx.write_text("\n".join(lines), encoding="utf-8")
    print("index", idx)


if __name__ == "__main__":
    main()
