# guoyunkaituo

**国运开拓 - 数据追踪与拉格朗日知识库整合仓库**

为《国运开拓》网络小说提供复杂数据管理系统。参考《无尽的拉格朗日》（星际猎人）游戏机制，整合Wiki舰船/装备/资源数据，追踪每位开拓者数据面板、资源变化、开拓币（直播打赏/任务/成就奖励）、蓝图抽取等。

## 仓库结构
- `data/` : 追踪表格与生成脚本
- `wiki_data/` : 从 https://wiki.biligame.com/wjdlglr/ 提取的舰船、装备、资源数据（CC BY-NC-SA 3.0）
- `celestial_knowledge/` : 真实天体与星系探索知识库（真实天文学 + 游戏融合）
- `novel_mechanics/` : 小说特定系统（开拓币、直播观众任务、考核规则等）
- `templates/` : 未来扩展模板

## 如何使用
1. Clone仓库
2. 运行 `data/generate_pioneers_xlsx.py` 生成专业Excel数据面板追踪表（使用openpyxl，包含公式、格式、多sheet）
3. 使用CSV/JSON作为数据源或手动更新
4. 参考wiki_data扩展舰船数据库

**数据来源**：
- 舰船/蓝图数据来自无尽的拉格朗日Wiki（https://wiki.biligame.com/wjdlglr/），遵循CC BY-NC-SA 3.0
- 资源：金属、晶体、重氢（采矿无人机采集）、比邻星币等
- 开拓币：小说原创（万族战场人联高级观众直播打赏/完成任务/成就）

**注意**：此仓库为小说创作辅助工具，非游戏数据爬取。所有游戏数据为公开Wiki总结，用于脑洞融合创作。

创建时间：2026-07-15
作者：Arcandaily + Grok AI协作