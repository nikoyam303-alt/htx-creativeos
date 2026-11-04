# Poloniex 插画素材调用

素材库：[GitHub 深色插画目录](https://github.com/nikoyam303-alt/htx-creativeos/tree/main/assets/illustrations/poloniex-dark)。
索引：https://raw.githubusercontent.com/nikoyam303-alt/htx-creativeos/main/assets/illustrations/poloniex-dark/manifest.json

1. 优先从 56 张官方深色素材中检索主题，再决定是否需要新生图。不得混用同仓库的 HTX 素材。
2. 用脚本按中文或英文关键词搜索；选定后下载并查看实际图片，确认符合构图和活动语义。
3. PNG 保留原始 #131316 背景，不是透明素材；不要当透明切图叠在不同底色上。需要透明/矢量版本时回到索引记录的 Figma 节点导出，不用粗暴色键抠除深色主体。
4. 排除白底素材。深底中的白色主体可以使用；黑色版本指本次收录的深色背景版本。
5. 插画中数字、折扣、币种、品牌字样需核对适用性，不能据此编造业务文案。
6. 搜索结果包含 Figma 链接、GitHub 路径与文件校验值；下载时校验 SHA-256。网络失败时明确报告，不宣称素材已下载。

```bash
python3 scripts/poloniex_assets.py --query 礼盒
python3 scripts/poloniex_assets.py --id poloniex-dark-1113-2616 --output /absolute/path/drone.png
```

脚本默认使用随 Skill 附带的索引；用 --refresh 更新远端索引。环境如需代理，使用用户现有 HTTPS_PROXY 配置，不写入凭证或固定个人代理地址。
